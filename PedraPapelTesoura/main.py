import tkinter 
from tkinter import *
from tkinter import ttk

# cores --------------------------------
co0 = "#FFFFFF"  # white
co1 = "#333333"  # black 
co2 = "#fcc058"  # orange
co3 = "#fff873"  # yellow
co4 = "#34eb3d"   # green
co5 = "#e85151"   # red
fundo = "#3b3b3b"

#configurando a janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

#dividindo a janela
frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column= 0, sticky = NW)
frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column= 0, sticky = NW)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#Configurando o frame cima

#Primeiro Jogador
app_primeiroJogador = Label(frame_cima, text="Você", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_primeiroJogador.place(x=25, y=70)
app_linha = Label(frame_cima, height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=0)
app_pontosJogador1 = Label(frame_cima, text="0",height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_pontosJogador1.place(x=50, y=20)

#
app_divisor = Label(frame_cima, text=":",height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_divisor.place(x=125, y=20)

#Segundo Jogador
app_computador = Label(frame_cima, text="PC", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_computador.place(x=205, y=70)
app_pontosJogador2 = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_pontosJogador2.place(x=170, y=20)
app_linha2 = Label(frame_cima, text="",height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_linha2.place(x=255, y=0)

#linha de empate
app_linha2 = Label(frame_cima, text="",width=255, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)


app_linha2.place(x=0, y=95)

 


janela.mainloop()
