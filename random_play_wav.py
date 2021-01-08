# -*- coding: utf-8 -*-
# @Author: scottxiong
# @Date:   2021-01-09 07:06:03
# @Last Modified by:   scottxiong
# @Last Modified time: 2021-01-09 07:19:27
import random
import os

songs = []

def initial(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        if ".wav" in child:
        	songs.append(child)


# paly
def play(wav):
	os.system("aplay "+wav)

def run():
	while True:
		x=random.randint(1,len(songs))-1
		song = songs[x]
		play(song)

initial("wav/")
run()