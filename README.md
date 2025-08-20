# Semantic Kernel Agentic AI Example

This Python script demonstrates an agentic AI workflow using Microsoft's Semantic Kernel with OpenAI's API. The script creates an autonomous agent that generates a short story based on a user-provided prompt and translates the entire story into a user-specified language, orchestrating tasks using automatic function calling. It showcases Semantic Kernel's modularity, extensibility, and future-proof design for building enterprise-grade AI solutions.

## Features
- **Interactive Story Generation**: Accepts user input for a story prompt (e.g., "a hidden cave") and generates a 100-150 word story with a clear beginning, middle, and end.
- **Dynamic Translation**: Translates the full generated story into a user-specified language (e.g., Spanish) using OpenAI's API.
- **Agentic Workflow**: Uses Semantic Kernel's automatic function calling with `FunctionChoiceBehavior.Auto()` to dynamically select and execute functions (`generate_story` and `translate_text`).
- **Modular Design**: Implements a custom `StoryPlugin` to integrate AI capabilities, aligning with Semantic Kernel's plugin architecture.
- **Error Handling**: Includes robust error handling for API and validation failures.

## Prerequisites
- **Python Version**: Python 3.10, 3.11, or 3.12 (required by `semantic-kernel>=1.0.0`).
- **Dependencies**:
  - Install required packages:
    ```bash
    pip install semantic-kernel==1.35.3 openai python-dotenv
    ```
- **OpenAI API Key**: Set as `OPENAI_API_KEY` in a `.env` file or environment variable.
  - Example `.env` file content:
    ```
    OPENAI_API_KEY=your-api-key-here
    ```

## Setup
1. Clone the repository or create a project directory:
   ```bash
   mkdir semantic-kernel-agentic-ai-simple
   cd semantic-kernel-agentic-ai-simple
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # or: .\venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install --upgrade pip
   pip cache purge
   pip install semantic-kernel==1.35.3 openai python-dotenv
   ```
4. Create a `.env` file with your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```

## Usage
1. Run the script:
   ```bash
   python semantic-kernel-agentic-ai.py
   ```
2. Enter the story prompt when prompted (e.g., "a hidden cave").
3. Enter the target language when prompted (e.g., "Spanish").
4. The script will generate a story based on the prompt and translate it into the specified language, displaying the result.

### Example Interaction
```
Enter the story prompt (e.g., 'a hidden cave'): a magical forest
Enter the target language (e.g., 'Spanish'): French
Final Result:
Il était une fois, dans une forêt magique nichée au cœur des montagnes, une jeune exploratrice nommée Élise qui découvrit un sentier lumineux. Les arbres scintillaient d’une lueur dorée, et des fées dansaient dans l’air. Au centre, elle trouva un lac enchanté reflétant des étoiles éternelles. Une voix lui murmura un secret ancien : le lac accordait un vœu. Élise souhaita la paix pour son village, et une brise apaisante balaya les terres. De retour, les villageois la célébrèrent, ignorant la magie qu’elle avait protégée dans la forêt.
```

## Notes
- **Model Choice**: Uses `gpt-3.5-turbo-1106`, which supports function calling. Switch to `gpt-4` by updating `ai_model_id` in the script if available.
- **Rate Limits**: Monitor OpenAI API usage to avoid rate limits. Consider adding retry logic (e.g., with `tenacity`) for production use.
- **Extensibility**: The `StoryPlugin` can be extended with additional functions (e.g., summarizing the story), as per the [Semantic Kernel documentation](https://learn.microsoft.com/en-us/semantic-kernel/agents/plugins?tabs=python).
- **Documentation Alignment**: The script leverages Semantic Kernel's modular plugins, automatic function calling, and chat history, aligning with the latest best practices (as of August 20, 2025) for building robust, future-proof AI solutions, as described in the Semantic Kernel documentation.

## Troubleshooting
- **Verify Installation**: Ensure `semantic-kernel==1.35.3` is installed:
  ```bash
  pip show semantic-kernel
  ```
  If incorrect, force reinstall:
  ```bash
  pip uninstall semantic-kernel -y
  pip install semantic-kernel==1.35.3 --index-url https://pypi.org/simple --no-cache-dir
  ```
- **Test in Terminal**: Run the script outside VS Code to bypass IDE issues:
  ```bash
  python semantic-kernel-agentic-ai.py
  ```
- **Check OpenAI API**: Verify the API key and model:
  ```python
  from openai import OpenAI
  client = OpenAI()
  print(client.models.list())
  ```
- **Environment Issues**: If errors persist, recreate the virtual environment and reinstall dependencies.

## Acknowledgements
- Built using Semantic Kernel, an open-source SDK by Microsoft (version 1.35.3 as of August 20, 2025).
- Documentation references: [Semantic Kernel Official Docs](https://learn.microsoft.com/en-us/semantic-kernel/).