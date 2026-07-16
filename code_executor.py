import subprocess
import os


def is_valid_python(file_path):
    with open(file_path,"r") as f :
        first_line = f.read().split("\n")[0].strip()

    valid_starts = ('import','from','def','class','#','tk','root')
    return any(first_line.startswith(s) for s in valid_starts)

def code_executor(file_path):
    if not os.path.exists(file_path):
        return {"success": False, "stdout":"","stderr":"file not found"}

    if not is_valid_python(file_path):
        return {
            "success":False,
            "stdout":"",
            "stderr":"Generated code contains explanation text instead of code"
    }
    try :
        results = subprocess.run(
            ['python',file_path],
            capture_output=True,
            text=True,
            timeout=30
        )
    except subprocess.TimeoutExpired as e :
        if e.stderr :
            return {"success":False,"stdout":"","stderr":e.stderr}
        else :
            return {"success":True,"stdout":"program ran successfully with GUI","stderr":""}
    if results.returncode == 0 :
        return {"success":True,"stdout":results.stdout,"stderr":""}
    else :
        return {"success":False,"stdout":"","stderr":results.stderr}
