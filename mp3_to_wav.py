# -*- coding: utf-8 -*-
# @Author: apple
# @Date:   2021-01-09 05:24:17
# @Last Modified by:   scottxiong
# @Last Modified time: 2021-01-11 15:53:36
import os

'''
For the name of song, we should remove the extra space, 
otherwise it will affect ffmpeg command
'''
def rename(name):
	# remove unnessary space
	return os.rename(name,name.replace(" ",""))

def updateName(filepath):
    mp3s =  os.listdir(filepath)
    for mp3 in mp3s:
        fullpath = os.path.join('%s%s' % (filepath, mp3))
        rename(fullpath)

'''
mp3 to wav: if you want to play music via 'aplay' through terminal in respberry pi, 
you should use .wav format instead rather than .mp3 
'''
def mp3_to_wav(mp3):
	if mp3[4:]==".mp3":
		name=mp3[:-3]
		new_name = name+"wav"
		cmd = "ffmpeg -i "
		cmd += mp3 +" -f wav wav/"+new_name[4:]
		info = "[info]: "+mp3 +" ==> " +new_name
		# print(cmd)
		os.system(cmd)

def do(filepath):
    mp3s =  os.listdir(filepath)
    for mp3 in mp3s:
        fullpath = os.path.join('%s%s' % (filepath, mp3))
        mp3_to_wav(fullpath)

# convert mp3 to wav
if __name__ == '__main__':
	updateName("mp3/")
	do("mp3/")