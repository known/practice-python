'''
这是一个备份文件的脚本示例。
'''

import os
import time


def backupzip(source, target):
    '''
    ZIP备份文件函数。
    自动将source目录列表的文件备份打包成zip文件，存放在target目录下的ymdHMS.zip。
    
    source：备份文件路径列表。
    target：备份文件存放路径。
    '''

    target = target + os.sep + time.strftime('%Y%m%d')
    if not os.path.exists(target):
        os.mkdir(target)

    target = target + os.sep + time.strftime('%H%M%S') + '.zip'
    zip_command = 'zip -r {} {}'.format(target, ' '.join(source))

    print('备份命令：', zip_command)
    print('运行：')
    if os.system(zip_command) == 0:
        print('备份成功！', target)
    else:
        print('备份失败！')


source_list = [
    'D:\\Known\\Practices\\python\\byte_of_python\\backup\\notes',
    'D:\\Known\\Practices\\python\\byte_of_python\\backup\\test'
]
target_dir = 'D:\\Known\\Practices\\python\\byte_of_python\\backup'
backupzip(source_list, target_dir)
