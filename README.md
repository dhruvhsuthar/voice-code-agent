# Voice Code Agent 🎙️

A voice-controlled, agentic code generation pipeline that converts spoken instructions into working, debugged Python code.

> Speak a requirement. Get working code.

---

## The Story Behind This Project

This project started with one goal — build a **fully local** coding agent. No cloud, no API keys, no subscriptions. Just your voice, a local LLM running on your machine via Ollama, and a complete agentic pipeline that generates, runs, and auto-debugs code automatically.

The local-first pipeline worked well for simple Python scripts. But when tested on complex tasks like GUI applications, the local 6.7B model (DeepSeek-Coder) showed a clear limitation — it would generate syntactically valid code that failed at runtime, or write explanation text instead of code entirely. This isn't a bug in the pipeline — it's a fundamental capability ceiling of smaller local models.

Rather than accepting broken output or abandoning the local-first principle, a hybrid approach was added:

- **Local model first** — always tried first, free, private, no internet needed
- **Gemini API as fallback** — only triggered when the local model fails after 3 attempts
- **Validator step** — Gemini reviews local model output before execution, catching semantic errors that syntax checking can't

This means the system stays private and free for simple tasks, and only calls the cloud when it genuinely needs better capability. That's not a compromise — it's a smarter architecture.

---

## How It Works

```
Your Voice
    ↓
Speech-to-Text (Whisper — local)
    ↓
Intent Understanding (DeepSeek-Coder via Ollama — local)
    ↓
Task Planning (DeepSeek-Coder via Ollama — local)
    ↓
Code Generation (DeepSeek-Coder via Ollama — local)
    ↓
Code Validation (Gemini API — reviews for runtime errors)
    ↓
PASS → Execute code directly
FAIL → Regenerate with Gemini API
    ↓
Auto Debugging Loop (max 3 attempts)
    ↓
Working Code + Spoken Result
```

---

## Tech Stack

| Component | Tool |
|---|---|
| Speech-to-Text | OpenAI Whisper (local) |
| Local LLM Engine | Ollama |
| Local Code Model | DeepSeek-Coder 6.7B |
| Cloud Model | Gemini 3.5 Flash (fallback only) |
| Audio Recording | SoundDevice |
| Voice Output | pyttsx3 |
| Code Execution | Python subprocess |

---

## Project Phases

| Phase | What Gets Built | Status |
|---|---|---|
| 1 | Voice input — mic recording + Whisper transcription | ✅ Complete |
| 2 | Intent parsing — raw text → structured JSON | ✅ Complete |
| 3 | Task planner — intent → ordered step-by-step plan | ✅ Complete |
| 4 | Code generation — plan → working Python file | ✅ Complete |
| 5 | Code executor — run code, capture output + errors | ✅ Complete |
| 6 | Auto debugger — error → LLM fix → re-run loop | ✅ Complete |
| 7 | Voice output — speak result back to user | ✅ Complete |
| 8 | Full pipeline integration + continuous session loop | ✅ Complete |
| 9 | API routing — local-first with Gemini fallback | ✅ Complete |

---

## Project Structure

```
voice-code-agent/
│
├── voice_recorder.py       # Mic recording → .wav file
├── voice_transcriber.py    # Whisper transcription
├── voice_listen.py         # Voice input test module
├── intent_parser.py        # LLM-based intent extraction → JSON
├── planner.py              # Task breakdown → ordered steps
├── codegen.py              # Code generation (local + cloud)
├── executor.py             # Code runner + output capture
├── debugger.py             # Auto error fixing loop
├── validator.py            # Gemini code review before execution
├── speaker.py              # TTS voice output
├── main.py                 # Full pipeline entry point
│
└── output/                 # Generated code files per session
    ├── project_1.py
    ├── project_2.py
    └── ...
```

---

## Setup

### Prerequisites

- Python 3.11+
- [Ollama](https://ollama.ai) installed and running
- ffmpeg installed (`brew install ffmpeg` on Mac)
- A free Gemini API key from [aistudio.google.com](https://aistudio.google.com)

### Install Dependencies

```bash
pip install openai-whisper sounddevice scipy numpy ollama pyttsx3 google-genai python-dotenv
```

### Pull the Local Model

```bash
ollama pull deepseek-coder:6.7b
```

---

## Configuration

### 1. Set Your Ollama Model Name

The local model name needs to be set in these files — search for `deepseek-coder:6.7b` and replace with your preferred Ollama model if different:

- `intent_parser.py`
- `planner.py`
- `codegen.py`
- `debugger.py`

If you're using `deepseek-coder:6.7b` as pulled above, no changes needed.

### 2. Set Your Gemini API Key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

Get a free API key from [aistudio.google.com](https://aistudio.google.com) — no credit card required. The free tier allows 1,500 requests per day which is more than enough for personal use.

**Important:** Never commit your `.env` file to GitHub. It is already listed in `.gitignore`.

### 3. Set Your Gemini Model Name

The Gemini model name is set in `validator.py` and `codegen.py`. The default is `models/gemini-3.5-flash`. To check which models are available for your API key:

```python
from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
for model in client.models.list():
    print(model.name)
```

Update the model name in both files if needed.

---

## Running the Agent

```bash
# Terminal 1 — start Ollama
ollama serve

# Terminal 2 — run the agent
python main.py
```

### Session Flow

1. System announces it is ready — spoken and printed
2. Press **Enter** when ready to give a command
3. System says *"Ready for your command, speak now"*
4. Speak your coding request (5 second window)
5. Pipeline runs automatically — intent, plan, generate, validate, execute, debug
6. Result is spoken back to you
7. Press **Enter** for the next command
8. Say *"stop"*, *"exit"*, or *"end session"* to quit

Each session generates numbered output files — `project_1.py`, `project_2.py` — so nothing gets overwritten.

---

## Example

You say:
> *"Create a Python calculator with a modern GUI"*

Pipeline output:
```
🎯 Understood intent: {'task': 'build a python calculator with gui', 'language': 'python', 'features': ['gui']}

📋 Plan:
  1. Set up tkinter window
  2. Create display label
  3. Add button grid
  ...

🖥️ Local model code saved to output/project_1.py
🔍 Validator decision: FAIL
☁️ Escalating to Gemini Flash...
☁️ Cloud code saved to output/project_1.py
✅ Code ran successfully
```

Result: A working GUI calculator, generated entirely from your voice command.

---

## What Makes This Different

| Feature | This Project | ChatGPT / Cursor |
|---|---|---|
| Local-first execution | ✅ | ❌ Cloud only |
| No subscription needed | ✅ | ❌ Paid plans |
| Privacy — code stays on device | ✅ | ❌ Sent to servers |
| Auto debugging loop | ✅ | ❌ Manual copy-paste |
| Voice controlled | ✅ | Partial |
| Open pipeline — every stage visible | ✅ | ❌ Black box |
| Intelligent model routing | ✅ | ❌ |

---

## Current Limitations

- Local 6.7B model is reliable for simple scripts but inconsistent for complex GUI applications
- The executor detects startup crashes only — runtime interaction errors in GUI apps are not caught automatically
- Non-deterministic output — the same voice command may generate slightly different code each session
- Audio bleed — a small delay is needed between TTS output and the next recording
- No multi-file project support — all generated code is single-file only
- 5 second recording window is fixed — long commands may get cut off

---

## Why Build This?

- Understand how agentic AI pipelines are actually architected
- Work with local LLMs — no vendor lock-in, no API costs
- Learn the real capability boundaries of local models through hands-on testing
- Build something that goes beyond tutorials and demonstrates real engineering judgment

---

## Status

All 9 phases complete. Fully working end to end.

---

## Author

Dhruv Suthar — Third year engineering student, building toward AI Engineering with a focus on Computer Vision, AR, and VR.
