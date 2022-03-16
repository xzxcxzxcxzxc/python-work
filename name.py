#!python3
import os

"""
it will change the name.
like form 'a.txt' to 'a1.txt'
"""
path=os.getcwd()
files=os.listdir(path)
c = input('输入要更改的格式的后缀名')
print(path)
for f in files:
    print(f)
    path1=path + '\\' + f
    print(path1)
    if '.' in f :
        continue
    files1=os.listdir(path1)
    i=1
    for a in files1:
        if c.lower() in a.lower():     # now is used to change txt file, 
            print("original file name:{}".format(a))
            old_file=os.path.join(path1,a)
            print("old_file is {}".format(old_file))
            j=f + str(i) +"." + c
            new_file=os.path.join(path1,j)
            print("File will be renamed as:{}".format(new_file))
            try:
                os.rename(old_file,new_file)
            except FileExistsError:
                continue
            print("changed file name:{}".format(new_file))
            i = i + 1