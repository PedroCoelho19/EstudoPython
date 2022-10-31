from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk


# cores ------------------------------------
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha


# criando janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)


ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use('clam')

# criandro frame

frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

# nome
pok_nome = Label(frame_pokemon, text='Pikachu', relief='flat',
                 anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pok_nome.place(x=12, y=15)

# categoria
pok_tipo = Label(frame_pokemon, text='Eletrico', relief='flat',
                 anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=50)

# id
pok_id = Label(frame_pokemon, text='#025', relief='flat',
               anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_id.place(x=12, y=75)

# Image do pokemon
image_pokemon = Image.open('images/pikachu.png')
image_pokemon = image_pokemon.resize((238, 238))
image_pokemon = ImageTk.PhotoImage(image_pokemon)

pok_imagem = Label(frame_pokemon, image=image_pokemon,
                   relief='flat', bg=co1, fg=co0)
pok_imagem.place(x=60, y=50)

pok_tipo.lift()

# status
pok_status = Label(janela, text='Status', relief='flat',
                   anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

# HP
pok_hp = Label(janela, text='HP: 100', relief='flat',
               anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_hp.place(x=15, y=360)

# atack
pok_atack = Label(janela, text='Ataque: 600', relief='flat',
                  anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_atack.place(x=15, y=385)

# defesa
pok_defesa = Label(janela, text='Defesa: 100', relief='flat',
                   anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_defesa.place(x=15, y=410)

# velocidade
pok_velocidade = Label(janela, text='Velociade: 100', relief='flat',
                       anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_velocidade.place(x=15, y=435)

# total
pok_total = Label(janela, text='Total: 100', relief='flat',
                  anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_total.place(x=15, y=460)


# habilidade
pok_habilidade = Label(janela, text='Habilidades', relief='flat',
                       anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_habilidade.place(x=180, y=310)

pok_hb_1 = Label(janela, text='Choque do trovão', relief='flat',
                 anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_hb_1.place(x=195, y=360)

pok_hb_2 = Label(janela, text='Investida', relief='flat',
                 anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_hb_2.place(x=195, y=385)


# Criando botoes para pokemon

# Image do pikachu
image_pokemon_pikachu = Image.open('images/cabeca-pikachu.png')
image_pokemon_pikachu = image_pokemon_pikachu.resize((40, 40))
image_pokemon_pikachu = ImageTk.PhotoImage(image_pokemon_pikachu)

pok_imagem_pikachu = Button(janela, image=image_pokemon_pikachu,text='Pikachu', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
pok_imagem_pikachu.place(x=375, y=10)

# Image do bulbasaur
image_pokemon_bulbasaur = Image.open('images/cabeca-bulbasaur.png')
image_pokemon_bulbasaur = image_pokemon_bulbasaur.resize((40, 40))
image_pokemon_bulbasaur = ImageTk.PhotoImage(image_pokemon_bulbasaur)

pok_imagem_bulbasaur = Button(janela, image=image_pokemon_bulbasaur,text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
pok_imagem_bulbasaur.place(x=375, y=65)

# Image do charmander
image_pokemon_charmander = Image.open('images/cabeca-charmander.png')
image_pokemon_charmander = image_pokemon_charmander.resize((40, 40))
image_pokemon_charmander = ImageTk.PhotoImage(image_pokemon_charmander)

pok_imagem_charmander = Button(janela, image=image_pokemon_charmander,text='Charmander', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
pok_imagem_charmander.place(x=375, y=120)

# Image do gyarados
image_pokemon_gyarados = Image.open('images/cabeca-gyarados.png')
image_pokemon_gyarados = image_pokemon_gyarados.resize((40, 40))
image_pokemon_gyarados = ImageTk.PhotoImage(image_pokemon_gyarados)

pok_imagem_gyarados = Button(janela, image=image_pokemon_gyarados,text='Gyaradoschu', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
pok_imagem_gyarados.place(x=375, y=175)

# Image do gengar
image_pokemon_gengar = Image.open('images/cabeca-gengar.png')
image_pokemon_gengar = image_pokemon_gengar.resize((40, 40))
image_pokemon_gengar = ImageTk.PhotoImage(image_pokemon_gengar)

pok_imagem_Gengar = Button(janela, image=image_pokemon_gengar,text='Gengar', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
pok_imagem_Gengar.place(x=375, y=230)

# Image do dragonite
image_pokemon_dragonite = Image.open('images/cabeca-dragonite.png')
image_pokemon_dragonite = image_pokemon_dragonite.resize((40, 40))
image_pokemon_dragonite = ImageTk.PhotoImage(image_pokemon_dragonite)

pok_imagem_dragonite = Button(janela, image=image_pokemon_dragonite,text='Dragonite', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
pok_imagem_dragonite.place(x=375, y=285)

janela.mainloop()
