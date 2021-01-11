# -*- coding: utf-8 -*-
# @Author: scottxiong
# @Date:   2021-01-11 15:50:13
# @Last Modified by:   scottxiong
# @Last Modified time: 2021-01-11 15:55:07
import random
import os

songs = []

def initial(filepath):
    wavs =  os.listdir(filepath)
    for wav in wavs:
        song = os.path.join('%s%s' % (filepath, wav))
        if ".wav" in song:
        	songs.append(song)

# play
def play(wav):
	os.system("aplay "+wav)

def run():
	x=random.randint(1,len(songs))-1
	song = songs[x]
	play(song)

# play wav with a random model
if __name__ == '__main__':
	initial("wav/")
	run()