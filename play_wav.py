# -*- coding: utf-8 -*-
# @Author: scottxiong
# @Date:   2021-01-09 05:32:58
# @Last Modified by:   scottxiong
# @Last Modified time: 2021-01-11 15:55:17
import os

# play
def play(wav):
	os.system("aplay "+wav)

def run(filepath):
    wavs =  os.listdir(filepath)
    for wav in wavs:
        fullpath = os.path.join('%s%s' % (filepath, wav))
        # print(fullpath)
        play(fullpath)

# play wav with a loop model
if __name__ == '__main__':
	run("wav/")