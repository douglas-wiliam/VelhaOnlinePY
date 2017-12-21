#Servidor Mutltithread
import socket
from threading import Thread

#Pool
class ClientThread(Thread):

	def __init__(self, ip, port, con, jogadorID):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.con = con
		self.jogadorID = jogadorID
		self.con.send(bytes(self.jogadorID))
		print('[+] Jogador Conectou ', ip, ' ', port, ' ', jogadorID)
	
	def run(self):
		while True:
			try:
				msg = self.con.recv(1024)
				if not(msg): break
				text = msg.decode("utf-8")
				print(text, 'Jogador ', self.jogadorID)
			except (ConnectionResetError, BrokenPipeError):
				break
		print('[-] Jogador Desconectou' , self.ip, ' ', self.port)
	
#Stub
HOST = ''
PORT = 5001

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
orig = (HOST, PORT)
tcp.bind(orig)
threads = []
contJogador = 1;

while True:
	try:
		tcp.listen(4)
		print('Esperado por jogadores...')
		(con, (ip,  port)) = tcp.accept()
		newthread = ClientThread(ip, port, con, contJogador)
		contJogador = contJogador+1
		newthread.start()
		threads.append(newthread)
		
	except KeyboardInterrupt:
		tcp.close()
		break
	
