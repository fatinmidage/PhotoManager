# 写一个python程序，如果当前文件夹内扩展名为raw的文件没有同名的jpg文件，则将raw文件移动至当前目录的“待删除的RAW文件”文件夹内

import os
import shutil

# 获取当前目录下的所有文件
files = os.listdir(os.getcwd())

# 判断是否存在“待删除的RAW文件”文件夹
if not os.path.exists('待删除的RAW文件'):
    # 创建“待删除的RAW文件”文件夹
    os.mkdir('待删除的RAW文件')
    print('“待删除的RAW文件”文件夹已创建')

# 遍历所有文件
for file in files:
    # 判断文件是否为raw文件
    if file.endswith('.raw'):
        # 获取文件名
        filename = file.split('.')[0]
        # 判断是否存在同名jpg文件
        if not os.path.exists(filename + '.jpg'):
            # 移动文件至“待删除的RAW文件”文件夹
            shutil.move(file, '待删除的RAW文件')
            print('文件%s已移动至“待删除的RAW文件”文件夹' % file)

# 判断是否存在“待删除的JPG文件”文件夹
if not os.path.exists('待删除的JPG文件'):
    # 创建“待删除的JPG文件”文件夹
    os.mkdir('待删除的JPG文件')
    print('“待删除的JPG文件”文件夹已创建')

# 遍历所有文件
for file in files:
    # 判断文件是否为jpg文件
    if file.endswith('.jpg'):
        # 获取文件名
        filename = file.split('.')[0]
        # 判断是否存在同名raw文件
        if not os.path.exists(filename + '.raw'):
            # 移动文件至“待删除的JPG文件”文件夹
            shutil.move(file, '待删除的JPG文件')
            print('文件%s已移动至“待删除的JPG文件”文件夹' % file)
