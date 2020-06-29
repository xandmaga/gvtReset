import time
import random
from pathlib import Path
import subprocess
import socket
from SMWinservice import SMWinservice

class GVTService(SMWinservice):
	_svc_name_ = "GVTService"
	_svc_display_name_ = "GVT Service"
	_svc_description_ = "Reboots GVT"

	def start(self):
		self.isrunning = True

	def stop(self):
		self.isrunning = False

	def main(self):
		while self.isrunning:
			if str.find(str(subprocess.check_output(['netsh', 'interface', 'show', 'interface', 'Wi-Fi'])), "Conectado") < 0:
				p = subprocess.Popen("C:\\Users\\xandmaga\\workspace\\sikuli\\gvt.cmd", shell=True, stdout = subprocess.PIPE)
				stdout, stderr = p.communicate()
			time.sleep(120)

if __name__ == '__main__':
	GVTService.parse_command_line()
