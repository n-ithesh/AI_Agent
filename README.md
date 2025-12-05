# AI Agent

A simple command-line AI agent built with LangChain, LangGraph, and OpenAI.

The agent runs in your terminal, accepts free-form questions or commands, and streams back responses from an OpenAI chat model.

## Features

- Command-line chat interface
- Streaming responses
- Environment-based configuration via `.env`
- Built using:
  - `langchain`
  - `langchain-openai`
  - `langgraph`
  - `python-dotenv`

## Requirements

- Python >= 3.13
- An OpenAI API key (or compatible endpoint) configured in your environment

## Installation

1. **Clone the repository**

   ```bash path=null start=null
   git clone <your-repo-url>
   cd AI_Agent
   ```

2. **Create and activate a virtual environment (recommended)**

   ```bash path=null start=null
   python -m venv .venv
   # PowerShell
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**

   This project uses `pyproject.toml` and `uv.lock`. If you are using `uv`:

   ```bash path=null start=null
   uv sync
   ```

   Or, using `pip` (fallback):

   ```bash path=null start=null
   pip install langchain langchain-openai langgraph python-dotenv
   ```

4. **Create a `.env` file**

   In the project root, create a file named `.env` and add your configuration, for example:

   ```bash path=null start=null
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_API_BASE=https://api.openai.com/v1
   ```

   Adjust variable names/values to match how you have configured `langchain-openai` in your environment.

## Running the Agent

From the project root, with your virtual environment activated and `.env` configured:

```bash path=null start=null
python main.py
```

You should see:

```text path=null start=null
Welcome to the AI Agent. Type 'exit' to quit.
You can ask questions or give commands.
```

Then you can type questions or instructions. Type `exit` or `quit` to close the program.

## Project Structure

```text path=null start=null
AI_Agent/
├── .env                # Environment variables (not committed)
├── .gitignore
├── .python-version
├── main.py             # CLI entrypoint for the AI agent
├── pyproject.toml      # Project metadata and dependencies
├── uv.lock             # Lockfile for dependencies
└── .venv/              # Local virtual environment (ignored)
```

## Customization

- **Model and temperature**: edit `main.py` and change the `ChatOpenAI` parameters:

  ```python path=null start=null
  model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
  ```

- **Tools**: extend the `tools` list in `main.py` and register them with `create_react_agent`.

## License

Add your preferred license here (e.g. MIT, Apache 2.0).
