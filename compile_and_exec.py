import gcc_compile as gc
import exec_with_args as exe_arg
import exec_with_stdin as exe_std
import os
from CONST import Const_Value as CONST

def compile_and_exec(Cfile_PATH:str,exec_folder_name:str,type:CONST,args_list:list = None,stdin_text : str = None):
    path = './' + exec_folder_name
    if not os.path.exists(path):
        os.mkdir(path)
    
    Out_PATH = gc.gcc_compile(Cfile_PATH,exec_folder_name)
    result = None
    if type == CONST.TYPE_ARGS:
        result = exe_arg.exec_with_args(Out_PATH,args_list)
    elif type == CONST.TYPE_STDIN:
        result = exe_std.exec_with_stdin(Out_PATH,stdin_text)
    else:
        print("No type input")
        return -1
    return result

def debug_compile_and_exec(Cfile_PATH:str,exec_folder_name:str,type:CONST,args_list:list = None,stdin_text : str = None):
    print('debug_compile_and_exec')
    path = './out'
    if not os.path.exists(path):
        os.mkdir(path)
    
    Out_PATH = gc.debug_gcc_compile(Cfile_PATH,exec_folder_name,)
    result = None
    if type == CONST.TYPE_ARGS:
        result = exe_arg.debug_exec_with_args(Out_PATH,args_list)
    elif type == CONST.TYPE_STDIN:
        result = exe_std.debug_exec_with_stdin (Out_PATH,stdin_text)
    else:
        print("No type input")
        return -1
    return result