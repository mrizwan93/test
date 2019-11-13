import os
import argparse
import shutil

def copy_file(file1, file2):
    if file1 == file2:
        print ("they both are same files")
    else:
        with open(file1, "r") as rf:
            with open(file2, "w") as wf:
                wf.write(rf.read())

def move_file(file1, file2):
    if file1 == file2:
        print("they both are same files")
    else:
        try:
            shutil.move(file1, file2)
        except:
            print ("the file already exist!!")
def replace_word(file1):
    with open(file1, 'r+') as f:
        string1=raw_input("Enter the string to be replaced")
        string2=raw_input("Enter the string to be replaced with")
        for line in f.readlines():
            f.write(line.replace(string1, string2))


def count_string(file1):
    count = 0
    with open(file1, 'r') as f:
        string = raw_input("Enter the string to be counted: ")  # type:
        for line in f.readlines():
            if string in line:
                count += 1
    print ("number of time string came= {}".format(count))

def Main():
    parser=argparse.ArgumentParser()
    parser.add_argument("path", help="enter the file path", type=str)
    parser.add_argument("-c", "--copy", help="copy file", action="store_true")
    parser.add_argument("-m", "--move", help="move file", action="store_true")
    parser.add_argument("-r", "--replace", help="replace string with new string", action="store_true")
    parser.add_argument("-n", "--number", help="count the number of time string occur", action="store_true")
    parser.add_argument("-R", "--Rename", help="rename the file", action="store_true")
    args=parser.parse_args()
    if os.path.exists(args.path):
        if args.copy:
                file2 = raw_input("Enter the path to copy: ")
                copy_file(args.path, file2)
        elif args.move:
            file2 = raw_input("Enter the path to move: ")
            move_file(args.path, file2)
        elif args.replace:
            replace_word(args.path)
        elif args.number:
            count_string(args.path)
        elif args.Rename:
            file2 = raw_input("Enter the new file name")
            os.rename(args.path, file2)
        else:
            pass
    else:
        print ("file not exist")
if __name__ == '__main__':
    task = True
    while task == True:
        Main()
        tasks = raw_input("Do you want to perform more task(y/n): ")
        if tasks == 'y':
            pass
        else:
            task = False
    print ("your job is done")
