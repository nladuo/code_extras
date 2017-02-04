#!/usr/bin/env python
# coding=utf-8
""" 代码行数统计 """

import sys
import os  

def help():
    print("usage\t: ./code_sumup.py [path] [suffix(s)]")
    print("example\t: ./code_sumup.py ./ cpp-c-h")
    exit()


def line_count(filename):
    count = len(open(filename, "rU").readlines())
    return count


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "error parameters."
        help()
    _dir = sys.argv[1]
    types = sys.argv[2].split("-")
    results = {}
    for t in types:
        results[t] = 0

    # 递归遍历
    def count(path):
        files =  os.listdir(path)  
        for filename in files:  
            filepath = os.path.join(path, filename)  
            if os.path.isdir(filepath):  
                count(filepath)  
            else:  
                ext = os.path.splitext(filepath)[1][1:]
                if ext in types:
                    line_num = line_count(filepath)
                    results[ext] = results[ext] + line_num

    count(_dir)
    total = 0
    for t in types:
        total = total + results[t]
        print t, "\t:", results[t], "行"

    print "total\t:", total, "行"
