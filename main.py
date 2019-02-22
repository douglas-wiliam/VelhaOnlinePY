#Servidor Mutltithread
import socket
from threading import Thread

# Teste commit
#Pool
class ClientThread(Thread):

	def __init__(self, ip, port, con, jogadorID):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.con = con
		self.jogadorID = jogadorID
		print('[+] Jogador Conectou ', ip, ' ', port)
	
	def run(self):
		while True:
			try:
				msg = self.con.recv(1024)
				if not(msg): break
				text = msg.decode("utf-8")
				print(text, 'Jogador ', self.jogadorID)
				self.con.send(bytes(self.jogadorID))
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

try:
    tcp.listen(4)
    print('Esperado por jogador...')
    (con, (ip,  port)) = tcp.accept()
    jogadorX = ClientThread(ip, port, con, contJogador)
    contJogador = contJogador+1
    #jogadorX.start()
    jogadorX.con.send(bytes('X','utf-8'))
    
    tcp.listen(4)
    print('Esperado por segundo jogador...')
    (con, (ip,  port)) = tcp.accept()
    jogadorO = ClientThread(ip, port, con, contJogador)
    contJogador = contJogador+1
    #jogadorO.start()
    jogadorO.con.send(bytes('O','utf-8'))
    
    while True:
        msg = jogadorX.con.recv(1024).decode("utf-8")
        jogadorO.con.send(bytes(msg,'utf-8'))
        msg = jogadorO.con.recv(1024).decode("utf-8")
        jogadorX.con.send(bytes(msg,'utf-8'))
        
except KeyboardInterrupt:
    tcp.close()
    
	
