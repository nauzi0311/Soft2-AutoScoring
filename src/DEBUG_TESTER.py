from CONST import Const_Value as CONST
from config_reader import config_reader
from tester import tester
import os


def main():
    toml_path = '../config.toml'
    toml = config_reader(toml_path)
    tester(toml)
    # arg_test_path = './in/test_arg/test_arg.in'
    # input_txt_test_path = './in/test_input_text/test_input_text.in'
    # args = []
    # with open(arg_test_path,'r') as f_arg:
    #     for line in f_arg.readlines():
    #         args.extend(line.split())
    # f_input_txt = open(input_txt_test_path, 'r')
    # input_txt = f_input_txt.read()
    # print(args)
    # print(input_txt)
    
    
    # Times_path = './target/test'
    # exec_folder_name = 'exec'
    # output_dir = './out'
    
    # tester(Times_path,CONST.TYPE_ARGS,exec_folder_name,output_dir,args=args)

def toml_parser():
    arg_test_path = './in/test_arg'
    input_txt_test_path = './in/test_input_text'
    arg_list = os.listdir(arg_test_path)
    arg_list.sort()
    print(arg_list)
    input_txt_list = os.listdir(input_txt_test_path)
    input_txt_list.sort()
    print(input_txt_list)
    
    toml = config_reader('./config.toml')
    for item in toml['configs']:
        print(item)
if __name__ == '__main__':
    main()
    # toml_parser()