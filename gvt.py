import subprocess
import socket

def runSikuliScript(path):
    filepath = path
    p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()
    print("Done Running Sikuli")

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

if str.find(str(subprocess.check_output(['netsh', 'interface', 'show', 'interface', 'Wi-Fi'])), "Conectado") < 0 and internet():
	runSikuliScript(p)