# 这个程序的作用：
# 可以将A目录下的所有文件以及A目录下的文件夹中的文件复制到另B目录里并且保留所有目录结构
# 这个程序的作用等同于windows下直接将一个文件夹复制到另一个文件夹中（windows的复制也是保留目录结构的）
# 但是不同点是：这个程序复制出的所有文件以及文件夹他们的修改日期、访问日期都是当前系统时间
#               而windows系统的复制之后的文件的修改日期、访问日期都和复制前的时间一样
# 目的：我需要修改一个工程内所有代码文件的创建日期，发现直接在windows下复制实现不了，于是用代码试了试，下面是我
#       实现的python代码（如果文件不多的话，要实现该功能也可以用下面的方法：打开文件，然后随便编辑一个
#       文字->保存->删除刚才编辑的文字->保存。这样做之后修改日期会改为当前时间，创建时间依然不变。）
import os
from shutil import copyfile  # 复制一个文件到另一个文件夹下    copyfile(src,dst)

# 递归函数
def copy_file(path_read, path_write):
    # 将number设置为全局变量
    global number
    # 输出path_read目录下的所有文件包括文件夹的名称
    names = os.listdir(path_read)
    # 循环遍历所有的文件或文件夹
    for name in names:
        # 定义新的读入路径（就是在原来目录下拼接上文件名）
        path_read_new = path_read + "\\" + name
        # 定义新的写入路径（就是在原来目录下拼接上文件名）
        path_write_new = path_write + "\\" + name
        # 判断该读入路径是否是文件夹，如果是文件夹则执行递归，如果是文件则执行复制操作
        if os.path.isdir(path_read_new):
            # 判断写入路径中是否存在该文件夹，如果不存在就创建该文件夹
            if not os.path.exists(path_write_new):
                # 创建要写入的文件夹
                os.mkdir(path_write_new)
            # 执行递归函数，将文件夹中的文件复制到新创建的文件夹中（保留原始目录结构）
            copy_file(path_read_new, path_write_new)
        else:
            # 每复制一次，number+1
            number += 1
            # 将文件path_read_new复制到path_write_new
            copyfile(path_read_new, path_write_new)


if __name__ == "__main__":
    # 定义一个变量，用来记录一共进行了多少次复制（也就是一共有多少个文件）
    number = 0
    # 从该文件夹中复制出来
    path_read = 'D:\Data\笔记'
    # 复制到该文件夹
    path_write = "D:\website\source"
    # 执行递归函数
    copy_file(path_read, path_write)
    # 输出一共有多少个文件
    print(number)