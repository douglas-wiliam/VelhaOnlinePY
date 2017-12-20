import socket


class conexao:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 5001
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dest = (self.HOST, self.PORT)
    def conectar(self):
        try:
            self.tcp.connect(self.dest)
        except ConnectionRefusedError:
            return False
        return True

    def mandaMsg(self,msg):
        self.tcp.send(bytes(msg, 'utf-8'))

"""    
msg = input()
tcp.send(bytes(msg, 'utf-8'))
msg = input()
"""
"""
img = './Assets/X.png'
Tela = iniciaGUI(img)
Tela.run()
tcp.close()"""





