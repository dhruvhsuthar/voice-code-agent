from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def validate(file_path,intent):
    with open(file_path,"r") as f :
        code = f.read()

    prompt = f"""
    You are a professional python code reviewer with 20 years of 
    experience. Review the code given below based on the intent provided
    and determine whether the code is correct or not.
    Code : 
    {code}
    Intent : 
    {intent}
    Rules : 
    - Do not provide any explanations
    - Return only the word PASS OR FAIL 
    - Return FAIL if the code contains plain English sentences instead of Python code
    - Return FAIL if the code would encounter any runtime errors
    - Return FAIL if the code does not correctly implement the user's intent
    - Return PASS only if the code is complete, correct, and matches the intent
"""
    response = client.models.generate_content(
        model = "models/gemini-3.5-flash",
        contents = prompt
    )
    decision = response.text
    print(f'Validator decision : {decision}')
    if "PASS" in decision :
        return True
    else :
        return False
