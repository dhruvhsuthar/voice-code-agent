# Voice Code Agent 🎙️

A fully local, agentic code generation pipeline that converts spoken instructions into working, debugged Python code — with zero cloud dependency.

> Speak a requirement. Get working code.

---

## What This Is

Most AI coding tools (Cursor, Claude Code, Codex) are cloud-dependent, closed-source black boxes. This project builds the same concept from scratch, locally, with every stage of the pipeline visible, controllable, and privacy-first.

Your code never leaves your machine.

---

## How It Works

```
Your Voice
    ↓
Speech-to-Text (Whisper)
    ↓
Intent Understanding (DeepSeek-Coder via Ollama)
    ↓
Task Planning
    ↓
Code Generation
    ↓
Execution + Error Detection
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
| LLM Engine | Ollama |
| Code + Intent Model | DeepSeek-Coder 6.7B |
| Audio Recording | SoundDevice |
| Voice Output | pyttsx3 |
| Code Execution | Python subprocess |

Everything runs locally. No API keys. No subscriptions. No internet required after setup.

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
| 9 | API routing — intelligent local/cloud model switching | 🔨 In Progress |

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
├── codegen.py              # Code generation → Python file
├── executor.py             # Code runner + output capture
├── debugger.py             # Auto error fixing loop
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

### Install Dependencies

```bash
pip install openai-whisper sounddevice scipy numpy ollama pyttsx3
```

### Pull the Model

```bash
ollama pull deepseek-coder:6.7b
```

### Run

```bash
# Start Ollama in a separate terminal
ollama serve

# Run the assistant
python main.py
```

---

## Session Flow

Once running, the assistant works like this:

1. System announces it is ready — spoken and printed
2. Press **Enter** when ready to give a command
3. System says *"Ready for your command, speak now"*
4. Speak your coding request (5 second window)
5. Pipeline runs automatically — intent, plan, code, execute, debug
6. Result is spoken back to you
7. Press **Enter** for the next command
8. Say *"stop"*, *"exit"*, or *"end session"* to quit

Each session generates numbered output files — `project_1.py`, `project_2.py` — so nothing gets overwritten between commands.

---

## Example

You say:
> *"Create a Python function that sorts a list of numbers"*

Pipeline output:
```
🎯 Understood intent: {'task': 'sort a list of numbers', 'language': 'python', 'features': ['sorting']}

📋 Plan:
  1. Define a function that accepts a list as input
  2. Use Python's built-in sorted() or .sort() method
  3. Return the sorted list
  4. Test with a sample list

✅ Code ran successfully
```

---

## What Makes This Different From ChatGPT/Cursor

| Feature | This Project | ChatGPT / Cursor |
|---|---|---|
| Fully local | ✅ | ❌ Cloud dependent |
| No API key needed | ✅ | ❌ Paid subscription |
| Privacy — code stays on device | ✅ | ❌ Sent to servers |
| Auto debugging loop | ✅ | ❌ Manual copy-paste |
| Voice controlled | ✅ | Partial |
| Open pipeline — every stage visible | ✅ | ❌ Black box |

---

## Current Limitations

- Local 6.7B model is reliable for simple scripts but inconsistent for complex GUI applications
- The executor detects startup crashes only — runtime interaction errors in GUI apps are not caught automatically
- Non-deterministic output — the same voice command may generate slightly different code each session due to LLM temperature
- Audio bleed — a small delay is needed between TTS output and the next recording to prevent the system's own voice being transcribed
- No multi-file project support yet — all generated code is single-file only

These limitations are understood and being addressed in Phase 9 via intelligent API routing.

---

## Upcoming — Phase 9: API Routing

The next extension adds intelligent model routing:

```
Simple task → local DeepSeek-Coder (fast, free, private)
Complex task → cloud API (reliable, high quality)
```

A config flag will allow switching between fully local and hybrid mode:

```python
USE_LOCAL_MODEL = True   # fully local, always free
USE_LOCAL_MODEL = False  # cloud fallback for complex tasks
```

Target API: Gemini Flash (free tier — 1M tokens/day, no credit card required)

---

## Why Build This?

- Understand how agentic AI pipelines are actually architected
- Work with local LLMs — no vendor lock-in, no API costs
- Learn how STT, LLM reasoning, code execution, and error feedback loops connect in a real system
- Discover real capability boundaries of local models through hands-on testing
- Build something that goes beyond tutorials

---

## Status

Core pipeline complete across all 8 phases. Phase 9 (API routing) actively in development.

---

## Author

Dhruv Suthar 
