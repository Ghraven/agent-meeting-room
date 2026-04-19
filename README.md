
# Agent Meeting Room

A Flask-based multi-agent AI chat app where you summon AI agents by @mentioning them — like a team meeting, but every participant is an AI.

![Agent Meeting Room](<img width="2047" height="1542" alt="agent meeting photo" src="https://github.com/user-attachments/assets/e5a83e30-a3ad-4379-a6c0-15da952027c2" />)

---

## What it does

- **@mention agents** to bring them into the conversation
- **Debate mode** — agents argue in structured rounds, then summarize
- **Free Talk mode** — agents hold a live, streaming group discussion on any topic
- **Memory** — save meeting notes directly to an Obsidian vault
- **Claude on demand** — use `@claude` to bring in the Claude API as the "headmaster"

---

## Agents

The 4 local agents use **any Ollama-compatible model** — just edit the `"model"` field in `agents.py`. The defaults below were chosen because they run well under 8B parameters (low VRAM/RAM), but you can swap in `llama3`, `qwen2`, `phi4`, `mistral-nemo`, or anything else your hardware can handle.

| Agent | Default Model | Personality |
|-------|--------------|-------------|
| Mistral | `mistral` (~4GB) | Sharp analytical thinker |
| Phi3 | `phi3` (~2GB) | Creative, lateral thinker |
| Gemma2 | `gemma2:2b` (~1.5GB) | Careful, balanced summarizer |
| DeepSeek | `deepseek-r1:7b` (~4.7GB) | Deep step-by-step reasoner |
| Claude | `claude-sonnet-4-6` (API) | Collaborative, nuanced advisor |

> **Swapping a model:** open `agents.py`, find the agent dict, change the `"model"` value to any model name from `ollama list`. That's it.

---

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/Ghraven/agent-meeting-room
cd agent-meeting-room
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install and start Ollama
Download from [ollama.com](https://ollama.com), then pull the models:
```bash
ollama pull mistral
ollama pull phi3
ollama pull gemma2:2b
ollama pull deepseek-r1:7b
```

### 4. Set up your .env
```bash
cp .env.example .env
# Edit .env and add your Anthropic API key
```

### 5. Run the app
```bash
python app.py
# OR on Windows: double-click start.bat
```

Open [http://localhost:5000](http://localhost:5000)

---

## Usage

| Command | Action |
|---------|--------|
| `@mistral your question` | Ask only Mistral |
| `@phi3 @gemma2 your question` | Ask specific agents |
| `@all your question` | All local agents respond |
| `@claude your question` | Ask Claude API |
| `@debate your question` | 3-round structured debate |
| *(no mention)* | All local agents respond |

For **Free Talk mode**, click the "Free Talk" button and give the agents a topic — they'll discuss it in real time via Server-Sent Events.

---

## Project Structure

```
agent-meeting-room/
├── app.py              # Flask routes and SSE streaming
├── agents.py           # Agent definitions, Ollama + Claude calls, debate logic
├── memory.py           # Obsidian vault integration
├── templates/
│   └── index.html      # Single-page frontend (Vanilla JS)
├── start.bat           # Windows quick-launch
├── .env.example        # API key template
├── requirements.txt    # Python dependencies
└── README.md
```

---

## Requirements

- Python 3.11+
- [Ollama](https://ollama.com) running locally on port 11434
- Anthropic API key (only needed for `@claude`)
- Optional: Obsidian for memory/note saving

---

## Tech Stack

- **Backend:** Python 3.11, Flask
- **Local AI:** Ollama (Mistral, Phi3, Gemma2, DeepSeek)
- **Cloud AI:** Anthropic Claude API (`claude-sonnet-4-6`)
- **Frontend:** Vanilla JavaScript, Server-Sent Events
- **Memory:** Obsidian Markdown vault

---

## License

MIT — see [LICENSE](LICENSE)
