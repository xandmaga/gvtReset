import time
import subprocess
import socket
from datetime import datetime

def runSikuliScript(path):
    filepath = path
    p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()
    print("Done Running Sikuli - " + str(datetime.now()))

def internet(host="8.8.8.8", port=53, timeout=3):
	"""
	Host: 8.8.8.8 (google-public-dns-a.google.com)
	OpenPort: 53/tcp
	Service: domain(DNS/TCP)
	"""
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True
	except socket.error as ex:
		print(ex)
		return False    

p = "C:\\Users\\xandmaga\\workspace\\sikuli\\gvt.cmd"

#if not(internet()):
#	runSikuliScript(p)

while True:
	if str.find(str(subprocess.check_output(['netsh', 'interface', 'show', 'interface', 'Wi-Fi'])), "Conectado") < 0 or (not internet()):
		print("Sem internet - " + str(datetime.now()))
		runSikuliScript(p)
	else:
		print("Wifi conectada - " + str(datetime.now()))
	time.sleep(360)
