# Binary file - just an immutable file that contains some information.
# Allowed operations:
# Create file
# Delete file
# Move file
# Readfile (returns file content)
#coding:utf8

import os
import shelve
import shutil

studentinfo1={'name':'WeiYirui','sex':'Female','Country':'China','City':'Shanghai'}
# Create /open file
with shelve.open('test02.bin') as fp: #创建或打开二进制文件 Create or open a binary file
    fp['1']=studentinfo1  #以字典形式把数据写入文件 Write data to a file in dictionary form
    # Readfile (returns file content)
    print(fp['1'])

#Get the current directory with getcwd first 先用getcwd取得当前目录
shutil.copy("test02.bin.dat","test02.bin")
shutil.move("test02.bin.dat","movetest02.bin")
# Delete file
os.remove('test02.bin')



