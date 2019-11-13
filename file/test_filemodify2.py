import subprocess

command = 'python /home/jgarg/Documents/python/programs/filemodify2.py'
def p1():#for all
    p1= subprocess.call('{} -H'.format(command), shell=True)
    p2= subprocess.call('{} -i'.format(command), shell=True)
    p3= subprocess.call('{} -p'.format(command), shell=True)
    p4= subprocess.call('{} -c'.format(command), shell=True)
    p5 = subprocess.call('{} -m'.format(command), shell=True)
    p6 = subprocess.call('{} -r'.format(command), shell=True)
    p7 = subprocess.call('{} -n'.format(command), shell=True)
    p8 = subprocess.call('{} -R'.format(command), shell=True)
    p9 = subprocess.call('{} -d'.format(command), shell=True)
    p10 = subprocess.call('{} -l'.format(command), shell=True)
    p11=subprocess.call('echo $?', shell=True)
    # p6=subprocess.Popen('{} -c'.format(command), shell=True)
    return p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11

#trial
# def p2():
#     filemodify2.copy_file('/home/jgarg/Documents/a.txt', '/home/jgarg/Downloads/a.txt')
#     return 0

def test_hostname():#hostname
    p = subprocess.call('{} -H'.format(command), shell=True)
    assert p==0

def test_ip():#ip
    p = subprocess.call('{} -i'.format(command), shell=True)
    assert p==0


def test_pwd():#present working directory
    p = subprocess.call('{} -p'.format(command), shell=True)
    assert p == 0

def test_copy():#copy file
    p = subprocess.call('{} -c'.format(command), shell=True)
    assert p == 0

def test_move():#move file
    p = subprocess.call('{} -m'.format(command), shell=True)
    assert p==0

def test_replace():#replace word
    p = subprocess.call('{} -r'.format(command), shell=True)
    assert p==0


def test_number():#count the string
    p = subprocess.call('{} -n'.format(command), shell=True)
    assert p == 0

def test_rename():#rename the file
    p = subprocess.call('{} -R'.format(command), shell=True)
    assert p==0


def test_delete():#delete the file
    p = subprocess.call('{} -d'.format(command), shell=True)
    assert p == 0

def test_list():#list all file and directory
    p = subprocess.call('{} -l'.format(command), shell=True)
    assert p==0

def test_filemodify2():
    assert p1()== (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    #trial
    # assert p2()== 0
    # assert filemodify2.copy_file('/home/jgarg/Documents/a.txt', '/home/jgarg/Downloads/a.txt')== 0
# print (type(filemodify2.copy_file('/home/jgarg/Documents/a.txt', '/home/jgarg/Downloads/a.txt')))
