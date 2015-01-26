# coding=utf-8

import telnetlib
import time
import sys

def loginToPtt(id, pw):
	tn = telnetlib.Telnet("ptt.cc")
	time.sleep(1)
	s = tn.read_very_eager().decode("big5", "ignore")
	print s

	time.sleep(1)
	tn.write(id+"\r\n")
	s = tn.read_very_eager().decode("big5", "ignore")
	print s

	time.sleep(1)
	tn.write(pw+"\r\n")
	s = tn.read_very_eager().decode("big5", "ignore")
	print s

	time.sleep(1)
	s = tn.read_very_eager().decode("big5", "ignore")
	print s

	time.sleep(1)
	s = tn.read_very_eager().decode("big5", "ignore")
	print s

	# "您想刪除其他重複登入的連線嗎"
	time.sleep(1)
	s = tn.read_very_eager().decode("big5", "ignore")
	print s

	tn.write("y\r\n")
	time.sleep(1)
	s = tn.read_very_eager().decode("big5", "ignore")
	print s

	tn.close()

if __name__ == '__main__':
	start = 1
	end = len(sys.argv)-1

	passwd = sys.argv[end]

	# range(start, end) means [start <= x < end]
	for i in range(start, end):
		loginToPtt(sys.argv[i], passwd)
