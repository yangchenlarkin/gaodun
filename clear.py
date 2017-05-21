import os

def clear():
	os.system('rm static/m3u8/*')
	os.system('rm static/key/*')
	os.system('rm static/ts/*')
	os.system('rm static/fixedm3u8/*')

clear()