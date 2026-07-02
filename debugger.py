import ollama
import re
from code_executor import code_executor

MAX_RETRIES = 3

def auto_debugger(file_path, stderr):
    count = 0

    while count < MAX_RETRIES :
        count += 1
        print(f'debug attempt {count} out of {MAX_RETRIES}')

        with open(file_path,'r') as f :
            broken_code = f.read()

        prompt = f'''You are a professional code debugger specialised
    in python debugging. Given the broke code and the error message
    your responsibility is to fix the code.
    
    Rules : 
    - only change the lines causing the error 
    - do not touch the any code that is working correctly 
    - do not add any comments or explanations after the fix 
    - return only the complete fixed code, nothing else 
    - no markdown fences, no commentary 
    - The fixed code must contain every line from the original file
    - Do not remove or drop any lines that are not causing the error
    - Make sure the file is complete from start to finish
    Broken code : 
    {broken_code}
    Error message : 
    {stderr}
'''
        response = ollama.chat(
            model = "deepseek-coder:6.7b",
            messages = [{'role':'user','content':prompt}]
        )
        fixed_code = response['message']['content'].strip()
        fixed_code = re.sub(r'```python|```','',fixed_code).strip()

        with open(file_path,'w') as f :
            f.write(fixed_code)

        print(f'Fix applied.....re-running the code')

        result = code_executor(file_path)

        if result['success']:
            print(f'Code fixed and running successfully after {count} attempts')
            return {'success':True,'stdout':result['stdout'],'stderr':'','attempts':count}
        else :
            print(f"Still failing:{result['stderr']}")
            stderr = result['stderr']

    print(f'could not fix after {MAX_RETRIES} attempts.Please check manually')
    return {'success':False,'stdout':'','stderr':stderr,'attempts':count}