"""""
with open("/home/jgarg/Documents/a.txt","r") as rf:
    with open("/home/jgarg/Documents/b.txt","w") as wf:
       wf.write(rf.read())

with open("/home/jgarg/Documents/a.txt", "r") as rf:
    with open("/home/jgarg/Downloads/a.txt", "w") as wf:
        wf.write(rf.read())

with open('/home/jgarg/Documents/a.txt', 'r') as rf:
    with open("/home/jgarg/Documents/c.txt", "a") as wf:
        wf.write(rf.readline())
"""
count = 0
with open('/home/jgarg/Documents/a.txt', 'r+') as f:
        for line in f.readlines():
            f.write(line.replace('jayesh', 'garg'))
            if 'jayesh' in line:
                count +=1
print (count)
