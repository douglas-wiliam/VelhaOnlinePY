#Servidor Mutltithread
import socket
from threading import Thread
from socketserver import ThreadingMixIn

#Pool
class ClientThread(Thread):

	def __init__(self, ip, port, jogadorID):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.jogadorID = jogadorID
		print('[+] Jogador Conectou ', ip, ' ', port)
	
	def run(self):
		while True:
			try:
				msg = con.recv(1024)
				if not(msg): break
				text = msg.decode("utf-8")
				print(text, 'Jogador ', self.jogadorID)
				con.send(bytes(self.jogadorID))
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
		newthread = ClientThread(ip, port, contJogador)
		contJogador = contJogador+1
		newthread.start()
		threads.append(newthread)
		
	except KeyboardInterrupt:
		tcp.close()
		break
	
