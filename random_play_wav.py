# -*- coding: utf-8 -*-
# @Author: scottxiong
# @Date:   2021-01-09 07:06:03
# @Last Modified by:   scottxiong
# @Last Modified time: 2021-01-11 15:54:49
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
	while True:
		x=random.randint(1,len(songs))-1
		song = songs[x]
		play(song)

# play wav with a random、loop model
if __name__ == '__main__':
	initial("wav/")
	run()