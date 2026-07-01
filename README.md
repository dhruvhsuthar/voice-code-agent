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
Auto Debugging Loop
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
| 3 | Task planner — intent → ordered step-by-step plan | 🔨 In Progress |
| 4 | Code generation — plan → working Python file | ⏳ Upcoming |
| 5 | Code executor — run code, capture output + errors | ⏳ Upcoming |
| 6 | Auto debugger — error → LLM fix → re-run loop | ⏳ Upcoming |
| 7 | Voice output — speak result back to user | ⏳ Upcoming |
| 8 | Full pipeline integration + polish | ⏳ Upcoming |

---

## Project Structure

```
voice-code-agent/
│
├── voice_recorder.py       # Mic recording → .wav file
├── voice_transcriber.py    # Whisper transcription
├── voice_listen.py         # Ties recording + transcription together
├── intent_parser.py        # LLM-based intent extraction → JSON
│
├── planner.py              # (Phase 3) Task breakdown
├── codegen.py              # (Phase 4) Code generation
├── executor.py             # (Phase 5) Code runner
├── debugger.py             # (Phase 6) Auto error fixing
├── speaker.py              # (Phase 7) TTS output
│
└── main.py                 # (Phase 8) Full pipeline
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
python voice_listen.py
```

---

## Example

You say:
> *"Create a Python calculator with a modern GUI"*

The system outputs:
```json
{
  "task": "build a python-based GUI calculator",
  "language": "python",
  "features": ["GUI"]
}
```

*(Full code generation and execution coming in Phase 4+)*

---

## Why Build This?

- Understand how agentic AI pipelines are actually architected
- Work with local LLMs — no vendor lock-in, no API costs
- Learn how STT, LLM reasoning, code execution, and error feedback loops connect
- Build something that goes beyond tutorials

---

## Status

Actively in development. Phases 1 and 2 complete. Updated regularly as new phases are built.

---

## Author

Dhruv Suthar — Third year engineering student
