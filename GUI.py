import client
from tkinter import *

con = client.conexao()

class botaoJogo:
            def acao(self):
                if Tela.unlock == True:
                    if self.imagem == self.imgEmpty:
                        self.imagem = Tela.imgSet
                        self.b.config(image=self.imagem, width="60",height="60")
                        con.mandaMsg(self.posicao)
                        Tela.unlock = False
                        msg = con.recebeMsg()
                        Tela.botoes[msg].b.config(image=Tela.imgEnemy, width="60",height="60")
                        Tela.unlock = True

            def __init__(self,master,pos):
                self.estado = False
                self.posicao = pos
                self.imgEmpty = PhotoImage(file='./Assets/empty.png')
                self.imagem = self.imgEmpty
                self.master = master
                self.b = Button(self.master, command=self.acao)
                self.b.config(image=self.imagem, width="60",height="60")
                

class iniciaGUI:
    
    def __init__(self):
        self.base = Tk()
        self.unlock = False
        self.imgEmpty = PhotoImage(file='./Assets/empty.png')
        self.imgSet = None
        self.imgEnemy = None
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
                self.botoes.setdefault(key,botaoJogo(self.Board,key))
        self.btCon = botaoCon(self.title)

    def run(self):
        self.text.pack()
        self.conStateLabel.pack()
        self.btCon.b.pack()
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
        

class botaoCon:
    def acao(self):
        valor = con.conectar()
        if valor:
            msg = con.recebeMsg()
            if msg == "O":
                Tela.conState = "Conectado como O"
                Tela.conStateLabel.config(fg="green", text=Tela.conState)
                Tela.imgSet = PhotoImage(file='./Assets/O.png')
                Tela.imgEnemy = PhotoImage(file='./Assets/X.png')
                msg = con.recebeMsg()
                Tela.botoes[msg].b.config(image=Tela.imgEnemy, width="60",height="60")
                Tela.unlock=True
            
            if msg == "X":
                Tela.conState = "Conectado como X"
                Tela.conStateLabel.config(fg="green", text=Tela.conState)
                Tela.imgSet = PhotoImage(file='./Assets/X.png')
                Tela.imgEnemy = PhotoImage(file='./Assets/O.png')
                Tela.unlock=True
        else:
            Tela.conState = "Não conectado"
            Tela.conStateLabel.config(fg="red", text=Tela.conState)
            

    def __init__(self,master):
            self.master = master
            self.b = Button(self.master, command=self.acao)
            self.b.config(text="Conectar", width="10",height="1")
        
        

Tela = iniciaGUI()
Tela.run()
