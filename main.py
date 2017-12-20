#Servidor
import socket

HOST = ''
PORT = 5001
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print('Conectado por', cliente)
    while True:
        msg = con.recv(1024)
        if not(msg): break
        text = msg.decode("utf-8")
        print(text)
    print('Finalizando conexao do cliente', cliente)
    con.close()
