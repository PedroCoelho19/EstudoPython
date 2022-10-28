import tkinter
from tkinter import *
from tkinter import ttk
import random

#import Pillow
from PIL import Image, ImageTk

# cores --------------------------------
co0 = "#FFFFFF"  # white
co1 = "#333333"  # black
co2 = "#fcc058"  # orange
co3 = "#fff873"  # yellow
co4 = "#34eb3d"   # green
co5 = "#e85151"   # red
fundo = "#3b3b3b"

# configurando a janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

# dividindo a janela
frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

# Configurando o frame cima

# Primeiro Jogador
app_primeiroJogador = Label(frame_cima, text="Você", height=1,
                            anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_primeiroJogador.place(x=25, y=70)
app_linha1 = Label(frame_cima, height=10, anchor='center',
                   font=('Ivy 10 bold'), bg=co0, fg=co0)
app_linha1.place(x=0, y=0)
app_pontosJogador1 = Label(frame_cima, text="0", height=1,
                           anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_pontosJogador1.place(x=50, y=20)

#
app_divisor = Label(frame_cima, text=":", height=1,
                    anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_divisor.place(x=125, y=20)

# Segundo Jogador
app_computador = Label(frame_cima, text="PC", height=1,
                       anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_computador.place(x=205, y=70)
app_pontosJogador2 = Label(frame_cima, text="0", height=1,
                           anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_pontosJogador2.place(x=170, y=20)
app_linha2 = Label(frame_cima, text="", height=10,
                   anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_linha2.place(x=255, y=0)

# linha de empate
app_linha = Label(frame_cima, text="", width=255,
                  anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)

app_pontos_pc = Label(frame_baixo, text="", height=1,
                      anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_pontos_pc.place(x=190, y=10)


global player1
global pc
global rodadas
global pontos_player
global pontos_pc


pontos_player = 0
pontos_pc = 0
rodadas = 5

# Função logica do jogo


def jogar(i):
    global rodadas
    global pontos_player
    global pontos_pc

    if rodadas > 0:
        print(rodadas)
        opcoes = ["Pedra", "Papel", "Tesoura"]
        pc = random.choice(opcoes)
        player1 = i

        app_pontos_pc['text'] = pc
        app_pontos_pc['fg'] = co1
        # se as escolhas forem iguais
        if player1 == "Pedra" and pc == "Pedra":
            print('empate')
            app_linha1['bg'] = co0
            app_linha2['bg'] = co0
            app_linha['bg'] = co3

        elif player1 == "Papel" and pc == "Papel":
            print('empate')
            app_linha1['bg'] = co0
            app_linha2['bg'] = co0
            app_linha['bg'] = co3

        elif player1 == "Tesoura" and pc == "Tesoura":
            print('empate')
            app_linha1['bg'] = co0
            app_linha2['bg'] = co0
            app_linha['bg'] = co3

        elif player1 == "Pedra" and pc == "Papel":
            print('Você perdeu!')
            app_linha1['bg'] = co0
            app_linha2['bg'] = co4
            app_linha['bg'] = co0
            pontos_pc += 10

        elif player1 == "Pedra" and pc == "Tesoura":
            print('Você ganhou!')
            app_linha1['bg'] = co4
            app_linha2['bg'] = co0
            app_linha['bg'] = co0
            pontos_player += 10

        elif player1 == "Papel" and pc == "Pedra":
            print('Você ganhou!')
            app_linha1['bg'] = co4
            app_linha2['bg'] = co0
            app_linha['bg'] = co0
            pontos_player += 10

        elif player1 == "Papel" and pc == "Tesoura":
            print('Você perdeu!')
            app_linha1['bg'] = co0
            app_linha2['bg'] = co4
            app_linha['bg'] = co0
            pontos_pc += 10

        elif player1 == "Tesoura" and pc == "Pedra":
            print('Você perdeu!')
            app_linha1['bg'] = co0
            app_linha2['bg'] = co4
            app_linha['bg'] = co0
            pontos_pc += 10

        elif player1 == "Tesoura" and pc == "Papel":
            print('Você ganhou!')
            app_linha1['bg'] = co4
            app_linha2['bg'] = co0
            app_linha['bg'] = co0
            pontos_player += 10

        # Atualiza pontuação
        app_pontosJogador1['text'] = pontos_player
        app_pontosJogador2['text'] = pontos_pc

        # Atualiza rodadas
        rodadas -= 1

    else:
        app_pontosJogador1['text'] = pontos_player
        app_pontosJogador2['text'] = pontos_pc

        fimDoJogo()


# Função de iniciar o jogo


def iniciarJogo():
    global icon_papel
    global icon_pedra
    global icon_tesoura
    global b_icon_papel
    global b_icon_tesoura
    global b_icon_pedra

    b_jogar.destroy()

    icon_pedra = Image.open('images/pedra.png')
    icon_pedra = icon_pedra.resize((50, 50), Image.ANTIALIAS)
    icon_pedra = ImageTk.PhotoImage(icon_pedra)
    b_icon_pedra = Button(frame_baixo, command=lambda: jogar("Pedra"), width=50, image=icon_pedra, compound=CENTER,
                          bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_pedra.place(x=15, y=60)

    icon_papel = Image.open('images/papel.png')
    icon_papel = icon_papel.resize((50, 50), Image.ANTIALIAS)
    icon_papel = ImageTk.PhotoImage(icon_papel)
    b_icon_papel = Button(frame_baixo, command=lambda: jogar("Papel"), width=50, image=icon_papel, compound=CENTER,
                          bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_papel.place(x=95, y=60)

    icon_tesoura = Image.open('images/tesoura.png')
    icon_tesoura = icon_tesoura.resize((50, 50), Image.ANTIALIAS)
    icon_tesoura = ImageTk.PhotoImage(icon_tesoura)
    b_icon_tesoura = Button(frame_baixo, command=lambda: jogar("Tesoura"), width=50, image=icon_tesoura, compound=CENTER,
                            bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_tesoura.place(x=170, y=60)


# Função de termina o jogo
def fimDoJogo():
    global rodadas
    global pontos_player
    global pontos_pc

    # Zerando variaveis
    rodadas = 5
    pontos_pc = 0
    pontos_player = 0

    # destruindo botoes
    b_icon_pedra.destroy()
    b_icon_papel.destroy()
    b_icon_tesoura.destroy()

    # definindo vencedor
    jogador1 = int(app_pontosJogador1['text'])
    jogador2 = int(app_pontosJogador2['text'])

    if jogador1 > jogador2:
        app_vencedor = Label(frame_baixo, text="Parabens você ganhou!!!", height=1,
                               anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co4)
        app_vencedor.place(x=5, y=60)

    elif jogador1 < jogador2:
        app_vencedor = Label(frame_baixo, text="Infelizmente você perdeu!!!", height=1,
                               anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co5)
        app_vencedor.place(x=5, y=60)
    else:
        app_vencedor = Label(frame_baixo, text="Foi um empate!", height=1,
                               anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co5)
        app_vencedor.place(x=5, y=60)

# Reinicia o jogo


    def jogarNovamente():
        app_pontosJogador1['text'] = 0
        app_pontosJogador2['text'] = 0
        app_vencedor.destroy()
    
        b_jogar_denovo.destroy()
    
        iniciarJogo()

    b_jogar_denovo = Button(frame_baixo, command=jogarNovamente, width=30, text='Jogar Novamente', bg=fundo, fg=co0, font=(
    'Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_denovo.place(x=5, y=151)


b_jogar = Button(frame_baixo, command=iniciarJogo, width=30, text='Jogar', bg=fundo, fg=co0, font=(
    'Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=151)


janela.mainloop()
