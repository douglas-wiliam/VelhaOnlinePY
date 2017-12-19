from tkinter import *


base = Tk()

imgX = PhotoImage(file='./Assets/X.png')
imgO = PhotoImage(file='./Assets/O.png')
imgEmpty = PhotoImage(file='./Assets/empty.png')


class botaoJogo(Button):
    def acao(self):
        if self.imagem == imgEmpty:
            self.imagem = imgX
            self.b.config(image=self.imagem, width="60",height="60")
    
        elif self.imagem == imgX:
            self.imagem = imgO
            self.b.config(image=self.imagem, width="60",height="60")
        
        else:
            self.imagem = imgEmpty
            self.b.config(image=self.imagem, width="60",height="60")
            
    def __init__(self,master):
        self.imagem = imgEmpty
        self.master = master
        self.b = Button(self.master, command=self.acao)
        self.b.config(image=self.imagem, width="60",height="60")
        
    

TR = botaoJogo(base) 
TC = botaoJogo(base) 
TL = botaoJogo(base)
MR = botaoJogo(base)
MC = botaoJogo(base)
ML = botaoJogo(base)
BR = botaoJogo(base)
BC = botaoJogo(base)
BL = botaoJogo(base)

TL.b.grid(row=0, column=0)
TC.b.grid(row=0, column=1)
TR.b.grid(row=0, column=2)
ML.b.grid(row=1, column=0)
MC.b.grid(row=1, column=1)
MR.b.grid(row=1, column=2)
BL.b.grid(row=2, column=0)
BC.b.grid(row=2, column=1)
BR.b.grid(row=2, column=2)

base.mainloop()

