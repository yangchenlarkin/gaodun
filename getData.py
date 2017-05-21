
# File: readline-example-1.py
import os
import serverIP

MAIN_URL = serverIP.MAIN_URL

def getM3u8(name):
	url = 'http://vod.gaodun.com/' + name + '/SD/1.m3u8'
	os.system('wget ' + url + ' -O static/m3u8/' + name + '.m3u8')

def getKey(name):
	url = 'http://vod.gaodun.com/player/authorize?id=' + name
	os.system('wget ' + url + ' -O static/key/' + name + '')

def handleM3u8(name):
	afile = open("static/m3u8/" + name + '.m3u8', 'r')
	os.system('touch static/fixedm3u8/' + name + '.m3u8')
	resfile = open("static/fixedm3u8/" + name + '.m3u8', 'w+')
	tsindex = 0
	while 1:
		line = afile.readline()[0: -1]
		if not line:
			break
		if '#EXT-X-KEY:' in line:
			key_url = MAIN_URL + '/static/key/' + name
			resfile.write('#EXT-X-KEY:METHOD=AES-128,URI="' + key_url + '",IV=0x1bf14ec97aeb0f0a18132c8679586c60,KEYFORMAT="identity"\n')
		elif '#' in line:
			resfile.write(line + '\n')
		else:
			downloadTs(line, name, tsindex)
			ts_url = MAIN_URL + '/static/ts/' + name + '_' + str(tsindex) + '.ts\n'
			resfile.write(ts_url)
			tsindex += 1;

	afile.close()
	resfile.close()

def downloadTs(url, name, index):
	os.system('wget ' + url + ' -O static/ts/' + name + '_' + str(index) + '.ts')

def main():
	afile = open("names.txt")
	while 1:
		name = afile.readline()[0: -1].replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')
		if not name:
			break
		getM3u8(name)
		getKey(name)
		handleM3u8(name)
	afile.close()

main()


