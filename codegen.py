import ollama
import re
import os
from google import genai
from dotenv import load_dotenv


'''
=======================================LOCAL MODEL================================================
'''

MODEL = "deepseek-coder:6.7b"

def code_generator(intent,steps,output_path):
    formatted_steps = "\n".join([f'{i+1}.{steps}' for i,steps in enumerate(steps)])

    prompt = f'''
    You are a professional software engineer with more than 2 decades of experience.
    expert in writing clean python code 
    
    Given the following plan, provide a complete,working code file.
    
    Task : {intent['task']}
    Language : {intent['language']}
    Features : {','.join(intent['features'])}
    
    Steps to be followed : 
    {formatted_steps}
    
    Rules : 
    - Return ONLY raw Python code
    - The very first character of your response must be either 'import', 'from', 'def', or '#'
    - No explanations, no descriptions, no markdown fences
    - No sentences in English anywhere in the output
    - If you write anything other than Python code, you have failed
    - return only complete code file, nothing else 
    - no markdown fencies, no explanation and no commentary 
    - the code must be complete and runnable in a single file 
    - follow the plan steps in order 
'''

    response = ollama.chat(
        model = MODEL,
        messages = [{'role':'user','content':prompt}]
    )

    code = response['message']['content'].strip()

    code = re.sub(r'```python|```','',code).strip()

    os.makedirs(os.path.dirname(output_path),exist_ok=True)

    with open(output_path,'w') as f :
        f.write(code)

    print(f'LOCAL MODEL ----- code saved to {output_path}')
    return output_path



'''
=======================================API CLOUD ROUTING===========================================
'''

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_code_cloud(intent,steps,output_path):
    formatted_steps = "\n".join([f'{i}.{steps}' for i, steps in enumerate(steps,1)])
    prompt = f'''
You are a professional software engineer with more than 2 decades of experience, expert in writing clean
python code. Given the following plan, write a complete, working code file.

Task : {intent['task']}
Language : {intent['language']}
Features : {','.join(intent['features'])}

Plan to follow : 
{formatted_steps}

Rules : 
- Return only raw python code file 
- The very first character of your response must be either 'import','from','def' or '#'
- no explanations, no descriptions, no markdown fences
- no sentences in english anywhere in the output 
- The code must be complete and runnable in a single file 
- Follow the plan in order
'''
    response = client.models.generate_content(
        model = "models/gemini-3.5-flash",
        contents = prompt
    )
    code = response.text

    code = re.sub(r'```python|```', '', code).strip()

    os.makedirs(os.path.dirname(output_path),exist_ok=True)

    with open(output_path,"w") as f :
        f.write(code)

    print(f'CLOUD MODEL ------- code saved to {output_path}')
    return output_path
