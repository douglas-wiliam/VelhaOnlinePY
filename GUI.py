import client
from tkinter import *

con = client.conexao()

class botaoJogo:
            def acao(self):
                if self.imagem == self.imgEmpty:
                    self.imagem = self.imgSet
                    self.estado = True
                    con.mandaMsg(self.posicao)
                    self.b.config(image=self.imagem, width="60",height="60")

            def __init__(self,master,imgSet,pos):
                self.estado = False
                self.posicao = pos
                self.imgEmpty = PhotoImage(file='./Assets/empty.png')
                self.imgSet = imgSet
                self.imagem = self.imgEmpty
                self.master = master
                self.b = Button(self.master, command=self.acao)
                self.b.config(image=self.imagem, width="60",height="60")


class iniciaGUI:
    def conectar(self):
        valor = con.conectar()
        if valor:
            self.conState = "Conectado"
            self.conStateLabel.config(fg="green", text=self.conState)
        else:
            self.conState = "Não conectado"
            self.conStateLabel.config(fg="red", text=self.conState)
    
    def __init__(self,imgSet):
        self.base = Tk()
        self.imgSet = PhotoImage(file=imgSet)
        self.imgEmpty = PhotoImage(file='./Assets/empty.png')
        self.title = PanedWindow(orient=VERTICAL, bd="10px")
        self.text = Label(self.title, font=("Arial Bold", 16), text="JOGO DA VELHA")
        self.conState = "Aguardando conexão..."
        self.conStateLabel = Label(self.title, font=("Arial",12), fg="gray", text=self.conState)
        self.Board = PanedWindow(orient=VERTICAL)
        self.botoes = {}
        linhas = ['T','M','B']
        colunas = ['R','C','L']
        for l in linhas:
            for c in colunas:
                key = str(l)+str(c)
                self.botoes.setdefault(key,botaoJogo(self.Board,self.imgSet,key))
        self.conectar()

    def run(self):
        self.text.pack()
        self.conStateLabel.pack()
        self.title.pack()
        self.botoes['TR'].b.grid(row=0, column=0)
        self.botoes['TC'].b.grid(row=0, column=1)
        self.botoes['TL'].b.grid(row=0, column=2)
        self.botoes['MR'].b.grid(row=1, column=0)
        self.botoes['MC'].b.grid(row=1, column=1)
        self.botoes['ML'].b.grid(row=1, column=2)
        self.botoes['BR'].b.grid(row=2, column=0)
        self.botoes['BC'].b.grid(row=2, column=1)
        self.botoes['BL'].b.grid(row=2, column=2)
        self.Board.pack()
        self.base.mainloop()
        
        
img = './Assets/X.png'
Tela = iniciaGUI(img)
Tela.run()
