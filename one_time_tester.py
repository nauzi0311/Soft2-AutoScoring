
from compile_and_exec import compile_and_exec as tester
from CONST import Const_Value as CONST
import os

def one_user_tester(Cfile_path:str,type:CONST,exec_folder_name:str,output_dir:str,args=None,input_txt=None):
    result = tester(Cfile_path,exec_folder_name,type,args,input_txt)
    user_id = Cfile_path[Cfile_path.rfind('/')+1:-2]
    out_file_path = output_dir + '/' + user_id + '.out'
    f = open(out_file_path, 'w')
    f.write(result)
    
def one_test_case_tester(Times_path:str,type:CONST,exec_folder_name:str,output_dir:str,args=None,input_txt=None):
    Cfile_list = os.listdir(path=Times_path)
    print(Cfile_list)
    if Times_path[-1] != '/':
        Times_path = Times_path + '/'
    for Cfile_name in Cfile_list:
        Cfile_path = Times_path + Cfile_name
        one_user_tester(Cfile_path,type,exec_folder_name,output_dir,args,input_txt)

# def one_time_tester(Times_path:str,type:CONST,exec_folder_name:str,output_dir:str,args=None,input_txt=None):
    