from fastmcp import FastMCP
import pyautogui
import subprocess
import time
import os
import platform

mcp = FastMCP("Lecturer-MCP")

PPT_PATH = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"  # Adjust if needed
PPT_FILE = r"A for Apple.pptx"


def ensure_powerpoint_open():
    system = platform.system()
    if system == "Windows":
        # Check if PowerPoint is running, open if not
        for proc in pyautogui.getAllWindows():
            if "PowerPoint" in proc.title:
                proc.activate()
                return True
        # If not open, launch PowerPoint with the file
        subprocess.Popen([PPT_PATH, PPT_FILE])
        time.sleep(3)  # Wait for PowerPoint to open
        return True
    elif system == "Darwin":
        # Check if PowerPoint is running
        check_cmd = [
            "osascript", "-e",
            'tell application \"System Events\" to (name of processes) contains "Microsoft PowerPoint"'
        ]
        result = subprocess.run(check_cmd, capture_output=True, text=True)
        if "true" in result.stdout.lower():
            # Activate PowerPoint
            subprocess.run([
                "osascript", "-e",
                'tell application "Microsoft PowerPoint" to activate'
            ])
            return True
        # If not open, launch PowerPoint with the file
        subprocess.Popen([
            "open", "-a", "Microsoft PowerPoint", PPT_FILE
        ])
        time.sleep(3)
        return True
    else:
        raise NotImplementedError("Only Windows and Mac are supported.")

@mcp.tool
def start_presentation() -> str:
    """Start the PowerPoint presentation from the beginning."""
    ensure_powerpoint_open()
    pyautogui.hotkey('f5')
    return "Presentation started."

@mcp.tool
def next_slide() -> str:
    """Go to the next slide."""
    pyautogui.press('right')
    return "Next slide."

@mcp.tool
def previous_slide() -> str:
    """Go to the previous slide."""
    pyautogui.press('left')
    return "Previous slide."

@mcp.tool
def go_to_slide(slide_number: int) -> str:
    """Go to a specific slide number."""
    pyautogui.typewrite(str(slide_number))
    pyautogui.press('enter')
    return f"Moved to slide {slide_number}."

@mcp.tool
def end_presentation() -> str:
    """End the PowerPoint presentation."""
    pyautogui.press('esc')
    return "Presentation ended."

if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=8000) 