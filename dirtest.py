
# Directory - can contain other directories and files. Directory can be empty or can have some elements. Number of elements in the directory should be <= DIR_MAX_ELEMS
# Allowed operations:
# Create directory
# Delete directory
# List files and subdirectories
# Move file or subdirectory to another location



# Create directory
#coding:utf8
import os
import shutil


#Get the current directory with getcwd first 先用getcwd取得当前目录
filewd=os.getcwd()
print(filewd)
#使用相对路径创建目录 Use relative paths to create directories
#path1为要创建目录的目录路径 Is the directory path to which the directory is to be created
path1="testcreate"
#调用OS模块的chdir方法修改程序工作目录 Call the chdir method of the OS module to modify the program working directory
os.chdir("E:/")
#调用OS模块的mkdir方法创建目录 Call the mkdir method of the OS module to create the directory
os.mkdir(path1)
print('新文件夹创建成功！New DIR created successfully!')  #New DIR created successfully!
f=open('E:/testcreate/testp.txt','w')
f.write('Hello World!')
f.close()

# List files and subdirectories

#获取指定目录下的所有文件 Gets all files in the specified directory
listdir1=os.listdir(path1)
print(" 目录下包含的文件和目录：",listdir1)

# Move file or subdirectory to another location


dsc = 'E:/testcreate/movetest.txt'
shutil.move("E:/testcreate/testp.txt","dsc")
print("After moving Where the file is:")

# Delete directory
# Delete the directory through using the rmdir method
#path3 Is the directory path of the directory to be deleted
path3="E:/testcreate"
# Invoke the rmdir method of the os module to delete the directory
os.rmdir(path3)
print('文件夹删除成功！DIR Remove successfully!')  #New DIR created successfully!


