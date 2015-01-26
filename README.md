# PTT.CC-AutoLogin
PTT.CC AutoLogin

Usage: 

1. From CLI:
	python telnet.ph userid_1 userid_2 ... password

2. From Python Interpreter:
	* First, go to python interpreter:

		`python`

	* Second, type them:
		`import sys`
		`import subprocess`

		`subprocess.call([sys.executable, 'telnet.py', 'userid_1', ('userid_2'), ..., 'password'])`

Every userid's password should be same.
