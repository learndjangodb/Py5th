# import pxssh
from pexpect import pxssh

class Client:
	
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.session = self.connect()

	def connect(self):
		try:
			s = pxssh.pxssh()
			s.login(self.host, self.user, self.password)
			return s
		except Exception as e:
			print(e)
			print("[-] Error Connecting")

	def send_command(self, cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before

def botnetCommand(command):
	for client in botnet:
		output = client.send_command(command)
		print("[*] Output from {} ".format(client.host))
		print("[+] {}".format(output))

def addClient(host, user, password):
		client = Client(host, user, password)
		botnet.append(client)

botnet = []

addClient("192.168.2.182", "systebui", "vtech@123")
botnetCommand("cd Desktop")
botnetCommand("ls -la")


