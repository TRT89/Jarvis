# Jarvis
Personal Voice Assistant (Learning project)

## Setup

Requires [uv](https://docs.astral.sh/uv/) (it installs Python 3.12 if needed).

```bash
uv sync                  # create .venv and install dependencies
cp .env.example .env     # then put your Anthropic API key in .env
uv run jarvis            # start Jarvis
uv run pytest            # run the tests
```
