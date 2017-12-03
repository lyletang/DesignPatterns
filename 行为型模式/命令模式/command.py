# -*- coding: utf-8 -*-
# author: lyletang
# date: 2017-12-02


import os

# 全局标记，被激活时，能像用户反馈执行的操作
verbose = True


class RenameFile:
    """重命名命令"""
    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest

    def execute(self):
        """执行部分"""
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        """撤销操作"""
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dest, self.src))
        os.rename(self.dest, self.src)


class CreateFile:
    """创建文件命令"""
    def __init__(self, path, txt='hello, world\n'):
        self.path, self.txt = path, txt

    def execute(self):
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile:
    """读取文件命令"""
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


def delete_file(path):
    """文件删除命令"""
    if verbose:
        print("deleting file '{}'".format(path))
    os.remove(path)


def main():
    orig_name, new_name = 'file1', 'file2'

    commands = []
    for cmd in [CreateFile(orig_name), ReadFile(orig_name),
                RenameFile(orig_name, new_name)]:
        commands.append(cmd)

    [c.execute() for c in commands]

    answer = input('reverse the executed commands? [y/n] ')

    if answer not in 'yY':
        print("the result is {}".format(new_name))
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass


if __name__ == '__main__':
    main()
