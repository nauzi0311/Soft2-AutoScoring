import gcc_compile as gc
from exec_with_args import exec_with_args as exe_arg
from exec_with_stdin import exec_with_stdin as exe_std
import os
from CONST import Const_Value as CONST

def compile_and_exec(Cfile_PATH:str,exec_folder_path:str,type:CONST,args_list:list = None,stdin_text : str = None):
    path = exec_folder_path
    if not os.path.exists(path):
        os.mkdir(path)
    Out_PATH = gc.gcc_compile(Cfile_PATH,exec_folder_path)
    result = None
    if type == CONST.TYPE_ARGS:
        result = exe_arg(Out_PATH,args_list)
    elif type == CONST.TYPE_STDIN:
        result = exe_std(Out_PATH,stdin_text)
    else:
        print("No type input")
        return -1
    return result

def debug_compile_and_exec(Cfile_PATH:str,exec_folder_path:str,type:CONST,args_list:list = None,stdin_text : str = None):
    print("debug compile and exec")
    path = exec_folder_path
    if not os.path.exists(path):
        os.mkdir(path)
    
    Out_PATH = gc.gcc_compile(Cfile_PATH,exec_folder_path)
    result = None
    if type == CONST.TYPE_ARGS:
        result = exe_arg(Out_PATH,args_list)
    elif type == CONST.TYPE_STDIN:
        result = exe_std(Out_PATH,stdin_text)
    else:
        print("No type input")
        return -1
    print(result)
    return result

# debug_compile_and_exec('./target/test2/test4.c','exe',CONST.TYPE_STDIN,stdin_text='100 HelloWorld')