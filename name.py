#!python3
import os

"""
it will change the name.
like form 'a.txt' to 'a1.txt'
"""
path=os.getcwd()
files=os.listdir(path)
print(path)
for f in files:
    print(f)
    path1=path + f
    print(path1)
    files1=os.listdir(path1)
    i=1
    for a in files1:
        if "txt" in a:     # now is used to change txt file, 
            print("original file name:{}".format(a))
            old_file=os.path.join(path1,a)
            print("old_file is {}".format(old_file))
            j=f + str(i) +".txt"
            new_file=os.path.join(path1,j)
            print("File will be renamed as:{}".format(new_file))
            os.rename(old_file,new_file)
            print("changed file name:{}".format(new_file))
            i = i + 1