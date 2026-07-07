import os
import pyttsx3
from voice_recorder import record_audio
from voice_transcriber import transcribe_audio
from intent_parsing import understand_intent
from planner import create_plan
from codegen import code_generator
from code_executor import code_executor
from debugger import auto_debugger
from speaker import speak_results
import time

engine = pyttsx3.init()


def main():
    msg = "Voice code agent is ready !!!"
    print(msg)
    engine.say(msg)
    engine.runAndWait()

    session_count = 0

    while True :
        input("Press the enter key when ready for the next command...")

        engine.say("Ready for your next command, speak now")
        engine.runAndWait()
        time.sleep(1)
        audio_file = record_audio(duration = 7)
        text = transcribe_audio(audio_file)
        print(f'Done. You said : {text}')

        exit_words = ['stop','end session','quit','exit']

        if any(word in text.lower() for word in exit_words):
            goodbye = "Ending session..Goodbye"
            print(goodbye)
            engine.say(goodbye)
            engine.runAndWait()
            break

        intent = understand_intent(text)
        print(f'Understood the intent : {intent}')

        if not intent :
            engine.say(f"Sorry, i did not understand that. Please try again")
            engine.runAndWait()
            continue

        plan = create_plan(intent)
        print(f'Plan : ')
        for i,step in enumerate(plan):
            print(f'{i}.{step}')


        session_count += 1
        output_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "output",
            f"project_{session_count}.py"
        )
        code_generator(intent,plan,output_path)

        print(f'Running the code.......')
        result = code_executor(output_path)

        if not result["success"]:
            error_msg = f"Error detected.....starting auto debugging"
            print(error_msg)
            engine.say(error_msg)
            engine.runAndWait()
            result = auto_debugger(output_path,result['stderr'])

        speak_results(result, attempts = result.get('attempts',1))

if __name__ == "__main__":
    main()







