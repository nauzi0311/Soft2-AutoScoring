
from compile_and_exec import compile_and_exec as tester
from CONST import Const_Value as CONST
import os

def one_test_case_tester(Cfile_path:str,test_file_path:str,type:CONST,exe_folder_path:str,output_folder_path:str):
    args = []
    input_txt = None
    if type == CONST.TYPE_ARGS:
        with open(test_file_path, 'r') as f:
            args = f.read().split()
    elif type == CONST.TYPE_STDIN:
        with open(test_file_path, 'r') as f:
            input_txt = f.read()
    result = tester(Cfile_path,exe_folder_path,type,args,input_txt)
    if result == -1:
        print("Compile and execute is failed")
        exit(1)
    else:
        result = result + '\n\n'
    student_id = Cfile_path[Cfile_path.rfind('/')+1:-2]
    output_file_path = output_folder_path + '/' + student_id + '.out'
    if os.path.isfile(output_file_path):
        with open(output_file_path,'a') as f:
            f.write(result)
    else:
        with open(output_file_path,'w') as f:
            f.write(result)