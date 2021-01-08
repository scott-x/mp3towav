# -*- coding: utf-8 -*-
# @Author: apple
# @Date:   2021-01-09 05:24:17
# @Last Modified by:   apple
# @Last Modified time: 2021-01-09 06:38:12
import os

def rename(name):
	return os.rename(name,name.replace(" ",""))

def updateName(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        # print(child)
        rename(child)	

# mp3 to wav
def mp3_to_awv(mp3):
	# 删除空格
	mp3=mp3.replace(" ","")
	name=mp3[:-3]
	new_name = name+"wav"
	cmd = "ffmpeg -i "
	cmd += mp3 +" -f wav wav/"+new_name[4:]
	print(cmd)
	os.system(cmd)

# 遍历指定目录，显示目录下的所有文件名
def listFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        # print(child)
        mp3_to_awv(child)

updateName("mp3/")
listFile("mp3/")


