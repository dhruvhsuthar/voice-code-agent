import pyttsx3

engine = pyttsx3.init()

def speak_results(result,attempts=1):

    if result['success']:
        if attempts>1 :
            msg = f'Code fixed and running successfully after {attempts} attempts'
        elif result['stdout']:
            msg = f"Code fixed and running successfully. Output : {result['stdout']}"
        else :
            msg = f'Code run successfully'
    else :
        msg = 'Could not fix the code after 3 attempts, please check it manually'

    print(msg)
    engine.say(msg)
    engine.runAndWait()


