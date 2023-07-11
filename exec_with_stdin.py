import subprocess

def exec_with_stdin(executable_path:str,stdin_text:str):
    command = [executable_path]
    try:
        result = subprocess.run(
            command,capture_output=True,text=True,
            check=True,input=stdin_text
        )
    except subprocess.CalledProcessError as e:
        print(e)
        return -1
    return result.stdout

def debug_exec_with_stdin(executable_path:str,stdin_text:str):
    command = [executable_path]
    print('debug_exec_with_stdin')
    print(command)
    try:
        result = subprocess.run(
            command,capture_output=True,text=True,
            check=True,input=stdin_text
        )
    except subprocess.CalledProcessError as e:
        print(e)
        return -1
    print(result.stdout)
    print(result.stderr)
    return result.stdout