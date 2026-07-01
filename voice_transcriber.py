import whisper

model = whisper.load_model("base")

def transcribe_audio(filename):
    results = model.transcribe(filename)
    text = results["text"].strip()
    return text