import os
import argparse
import shutil
import socket
import sys

def copy_file(file1, file2):
    if file1 == file2:
        print ("they both are same files")
    else:
        with open(file1, "r") as rf:
            with open(file2, "w") as wf:
                wf.write(rf.read())

def move_file(**Kwargs):
    print(type(Kwargs))
    if os.path.isdir(Kwargs[ 'file' ]):
        if Kwargs['file1'] == Kwargs[ 'file' ]:
           print("they both are same files")
        else:
            try:
                shutil.move(Kwargs['file1'], Kwargs['file'])
            except:
                print ("the file already exist!!")
    else:
        print ("{} is a file".format(Kwargs['file']))
    sys.exit(0)

def replace_word(file1):
    with open(file1, 'r+') as f:
        string1=raw_input("Enter the string to be replaced")
        string2=raw_input("Enter the string to be replaced with")
        for line in f.readlines():
            f.write(line.replace(string1, string2))
    sys.exit(0)

def count_string(file1):
    count = 0
    with open(file1, 'r') as f:
        string = raw_input("Enter the string to be counted: ")  # type:
        for line in f.readlines():
            if string in line:
                count += 1
    print ("number of time string came= {}".format(count))
    sys.exit(0)

def Main():
    parser=argparse.ArgumentParser()
  # parser.add_argument("path", help="enter the file path", type=str)
    parser.add_argument("-c", "--copy", help="copy file", action="store_true")
    parser.add_argument("-m", "--move", help="move file", action="store_true")
    parser.add_argument("-r", "--replace", help="replace string with new string", action="store_true")
    parser.add_argument("-n", "--number", help="count the number of time string occur", action="store_true")
    parser.add_argument("-R", "--Rename", help="rename the file", action="store_true")
    parser.add_argument("-d", "--delete", help="delete the file", action="store_true")
    parser.add_argument("-l", "--list", help="list all the content in the directory", action="store_true")
    parser.add_argument("-p", "--pwd", help="this will show path for present working directory", action="store_true")
    parser.add_argument("-H", "--Hostname", help="this will display hostname", action="store_true")
    parser.add_argument("-i", "--ipaddress", help="provide ip address", action="store_true")
    args=parser.parse_args()

    if args.pwd:
        print (os.getcwd())
    elif args.Hostname:
        print ("host name is: {}".format(socket.gethostname()))
    elif args.ipaddress:
        print ("ip address is: {}".format(socket.gethostbyname(socket.gethostname())))
    else:
        path=raw_input("enter the file path: ")
        if os.path.exists(path):
            if args.copy:
                file2 = raw_input("Enter the path to copy: ")
                copy_file(path, file2)
            elif args.move:
                file2 = raw_input("Enter the path to move: ")
                move_file(file1=path, file=file2)
            elif args.replace:
                replace_word(path)
            elif args.number:
                count_string(path)
            elif args.Rename:
                file2 = raw_input("Enter the new file name")
                os.rename(path, file2)
            elif args.delete:
                os.remove(path)
            elif args.list:
                print (os.listdir(path))
            else:
                pass
        else:
            print ("file not exist!!")
            sys.exit(1)

if __name__ == '__main__':
    Main()

