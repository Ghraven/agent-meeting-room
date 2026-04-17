import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

OBSIDIAN_VAULT = os.getenv(
    "OBSIDIAN_VAULT_PATH",
    "C:/Users/Administrator/Documents/ObsidianVault/AgentMeetings"
)
MEMORY_FILE = "meeting_memory.md"


def save_to_obsidian(title, content):
    """Save a note to Obsidian vault."""
    try:
        os.makedirs(OBSIDIAN_VAULT, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        safe_title = title.replace(" ", "_").replace("/", "-")[:50]
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M')}_{safe_title}.md"
        filepath = os.path.join(OBSIDIAN_VAULT, filename)

        note_content = f"""# {title}
*Saved: {timestamp}*

{content}

---
#agent-meeting #auto-saved
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(note_content)

        # Also append to rolling memory file
        memory_path = os.path.join(OBSIDIAN_VAULT, MEMORY_FILE)
        with open(memory_path, "a", encoding="utf-8") as f:
            f.write(f"\n## {title} — {timestamp}\n{content}\n\n")

        print(f"[Memory] Saved to {filepath}")
        return True

    except Exception as e:
        print(f"[Memory] Error saving: {e}")
        return False


def get_recent_memory(max_chars=1500):
    """
    Read recent memory from Obsidian vault.
    Agents use this as context for their answers.
    """
    try:
        memory_path = os.path.join(OBSIDIAN_VAULT, MEMORY_FILE)
        if not os.path.exists(memory_path):
            return ""

        with open(memory_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Return last max_chars of memory
        if len(content) > max_chars:
            content = "..." + content[-max_chars:]

        return content

    except Exception as e:
        print(f"[Memory] Error reading: {e}")
        return ""


def clear_memory():
    """Clear the rolling memory file."""
    try:
        memory_path = os.path.join(OBSIDIAN_VAULT, MEMORY_FILE)
        if os.path.exists(memory_path):
            os.remove(memory_path)
        return True
    except Exception:
        return False