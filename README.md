# Lecturer-MCP

An AI agent using the Model Context Protocol (MCP) to control Microsoft PowerPoint presentations via tool calls. Built with FastMCP and pyautogui.

## Features
- Accepts slide content or instructions via MCP tool calls
- Automatically opens a PowerPoint file
- Controls presentation:
  - Start presentation (F5)
  - Next/Previous slide (→, ←)
  - Go to specific slide number
  - End presentation (ESC)
- Responds to commands like:
  - "Start presentation"
  - "Go to slide 3"
  - "Next slide"
  - "Previous slide"
  - "End presentation"
- Safety checks: ensures PowerPoint is open before sending commands
- FastMCP SSE server for LLM/agent integration


## Setup
1. (Recommended) Create a Python 3.13 virtual environment using [uv](https://github.com/astral-sh/uv):
   ```sh
   uv venv .venv --python=3.13
   uv pip install -r requirements.txt
   ```
2. Adjust `PPT_PATH` and `PPT_FILE` in `server.py` if needed:
   - `PPT_PATH`: Path to PowerPoint executable
   - `PPT_FILE`: Path to your `.pptx` file

## Running the Server
```sh
uv run python server.py
```
- The server runs at `http://127.0.0.1:8000/sse` (SSE transport)

## Testing
A test client is provided:
```sh
uv run python test_client.py
```
This will:
- List available tools
- Start the presentation
- Go to next/previous slides
- Jump to slide 3
- End the presentation

## Customization
- Add or modify tools in `server.py` as needed
- Integrate with LLMs or other MCP clients for automation

## Notes
- pyautogui simulates keyboard input; ensure PowerPoint is in the foreground
- Timing and transitions are handled with short delays for reliability
