import os
from shutil import copyfile

def cp_file(src, dst):
    pass

file_prefix = 'C:\\Users\\jli21\\Desktop\\aaa'

#for i in range(17, 265):
for i in range(20, 265):
    idx = str(i) if len(str(i)) == 3 else '0' + str(i)
    filename = 'Windows101909x64-with-chef_v14-1.0.0.zip.' + idx
    file_path = os.path.join(file_prefix, filename)
    print('COPY: ', idx)
    try:
        copyfile(file_path, 'Y:\\JackyLi\\' + filename)
    except Exception as e:
        print('xxxxxx ', str(e))
