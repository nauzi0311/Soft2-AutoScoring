from CONST import Const_Value as CONST
from one_time_tester import one_test_case_tester as tester


def main():
    arg_test_path = './in/test_arg/test_arg.in'
    input_txt_test_path = './in/test_input_text/test_input_text.in'
    args = []
    with open(arg_test_path,'r') as f_arg:
        for line in f_arg.readlines():
            args.extend(line.split())
    
    f_input_txt = open(input_txt_test_path, 'r')
    # args = ['Hello world']
    # input_txt = '100 Hello World'
    input_txt = f_input_txt.read()
    print(args)
    print(input_txt)
    
    
    Times_path = './target/test'
    exec_folder_name = 'exec'
    output_dir = './student_out'
    
    tester(Times_path,CONST.TYPE_ARGS,exec_folder_name,output_dir,args=args)


if __name__ == '__main__':
    main()