# -*- coding: utf-8 -*-
# @Author: scottxiong
# @Date:   2021-01-09 05:32:58
# @Last Modified by:   scottxiong
# @Last Modified time: 2021-01-09 07:01:38
import os


# paly
def play(wav):
	os.system("aplay "+wav)

# 遍历指定目录，显示目录下的所有文件名
def run(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        # print(child)
        play(child)


run("wav/")