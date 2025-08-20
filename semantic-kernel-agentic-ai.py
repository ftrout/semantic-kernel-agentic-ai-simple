import asyncio
import os
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, OpenAIPromptExecutionSettings
from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.prompt_template import PromptTemplateConfig
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Semantic Kernel
kernel = Kernel()

# Configure the OpenAI service
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

chat_completion = OpenAIChatCompletion(
    ai_model_id="gpt-4o",
    api_key=api_key
)
kernel.add_service(chat_completion)

# Define a custom plugin for story generation and translation
class StoryPlugin:
    @kernel_function(
        description="Generates a short story based on a prompt",
        name="generate_story"
    )
    async def generate_story(self, prompt: str) -> str:
        story_prompt = """
        Write a short story (100-150 words) based on the following prompt: {{ $prompt }}.
        The story should have a clear beginning, middle, and end.
        """
        prompt_config = PromptTemplateConfig(
            template=story_prompt,
            execution_settings=OpenAIPromptExecutionSettings(
                max_tokens=300,
                temperature=0.7
            )
        )
        story_function = kernel.add_function(
            plugin_name="story",
            function_name="generate_story_internal",
            prompt_template_config=prompt_config
        )
        result = await kernel.invoke(story_function, prompt=prompt)
        return str(result)

    @kernel_function(
        description="Translates text into a specified language",
        name="translate_text"
    )
    async def translate_text(self, text: str, target_language: str) -> str:
        translation_prompt = """
        Translate the following text into {{ $target_language }}: {{ $text }}
        """
        prompt_config = PromptTemplateConfig(
            template=translation_prompt,
            execution_settings=OpenAIPromptExecutionSettings(
                max_tokens=500,
                temperature=0.3
            )
        )
        translation_function = kernel.add_function(
            plugin_name="story",
            function_name="translate_text_internal",
            prompt_template_config=prompt_config
        )
        result = await kernel.invoke(translation_function, text=text, target_language=target_language)
        return str(result)

# Register the custom plugin
kernel.add_plugin(StoryPlugin(), plugin_name="story")

# Define the main async function to run the agentic workflow
async def run_agentic_workflow(prompt: str, target_language: str):
    user_query = f"Generate a short story about '{prompt}' and translate it into {target_language}."
    
    try:
        # Create chat history
        history = ChatHistory()
        history.add_user_message(user_query)

        # Enable automatic function calling
        execution_settings = OpenAIPromptExecutionSettings(
            function_choice_behavior=FunctionChoiceBehavior.Auto()
        )

        # Get the chat completion service
        chat_completion_service = kernel.get_service(type=OpenAIChatCompletion)

        # Get response with automatic function calling
        result = await chat_completion_service.get_chat_message_content(
            chat_history=history,
            settings=execution_settings,
            kernel=kernel,
        )

        # Print the final result
        print("\nFinal Result:")
        print(result.content)

        # Add the result to chat history for context
        history.add_message(result)

    except Exception as e:
        print(f"Error during execution: {str(e)}")

# Run the async function with user input
if __name__ == "__main__":
    # Take input from the user
    prompt = input("Enter the story prompt (e.g., 'a hidden cave'): ")
    target_language = input("Enter the target language (e.g., 'Spanish'): ")
    asyncio.run(run_agentic_workflow(prompt, target_language))