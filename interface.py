import sys
import jogo
import tkinter as tk

#PROPORÇÕES
largura = 1400
altura = 800
botao_largura = 96
botao_altura = 60

#PROPORÇÕES
largura = 1600
altura = 900

botao_largura = 96
botao_altura = 60

#FONTES
fonte_titulo = ("Arial",28,"bold")
fonte_botao = ("Comfortaa",28,"bold")
fonte_texto = ("Arial",28)

#CORES

cor_fundo = ("#FFFFFF")
cor_fundo = ("#E5EBE3")
cor_botao = ("#FAFAFA")
cor_texto = ("#000000")
cor_lixeira_papel = ("#1900FF")
cor_lixeira_plastico = ("#FF0C0C")
cor_lixeira_vidro = ("#098100")
cor_lixeira_metal = ("#FFFB00")
cor_lixeira_organicos = ("#331A1A")

def carregar_imagens():

    #imagens

    global imagem_background
    global imagem_dificil
    global imagem_facil
    global imagem_historico
    global imagem_iniciar
    global imagem_medio
    global imagem_metal
    global imagem_organico
    global imagem_papel
    global imagem_plastico
    global imagem_sair
    global imagem_tela_dificuldade
    global imagem_tela_jogo
    global imagem_tela_1
    global imagem_vidro

    imagem_background = tk.PhotoImage(file="imagens/background.png")
    imagem_dificil = tk.PhotoImage(file="imagens/dificil.png")
    imagem_facil = tk.PhotoImage(file="imagens/facil.png")
    imagem_historico = tk.PhotoImage(file="imagens/historico.png")
    imagem_iniciar = tk.PhotoImage(file="imagens/iniciar.png")
    imagem_medio = tk.PhotoImage(file="imagens/medio.png")
    imagem_metal = tk.PhotoImage(file="imagens/metal.png")
    imagem_organico = tk.PhotoImage(file="imagens/organico.png")
    imagem_papel = tk.PhotoImage(file="imagens/papel.png")
    imagem_plastico = tk.PhotoImage(file="imagens/plastico.png")
    imagem_sair = tk.PhotoImage(file="imagens/sair.png")
    imagem_tela_dificuldade = tk.PhotoImage(file="imagens/tela_dificuldade.png")
    imagem_tela_jogo = tk.PhotoImage(file="imagens/tela_jogo.png")
    imagem_tela_1 = tk.PhotoImage(file="imagens/tela_1.png")
    imagem_vidro = tk.PhotoImage(file="imagens/vidro.png")

#LIXEIRA PAPEL - 1
#LIXEIRA PLASTICO - 2
#LIXEIRA VIDRO - 3
#LIXEIRA ORGANICOS - 4
#LIXEIRA METAL - 5

difuculade = -1
janela = None
residuo = None
pontos = None

def mudar_dificuldade(modo,mudar_tela):
    global dificuldade 
    dificuldade = modo
    mudar_tela(3)

def clicar_lixeira(numero):
    nova_palavra,nova_pontuacao = jogo.resposta(numero)

    residuo.config(text =nova_palavra)
    pontos.config(text =f"Pontuação:{nova_pontuacao}")

def interface(tela,mudar_tela,palavra= None,pontuacao = None):

    #TESTANDO

    if tela == 1: #TELA INICIAL
        titulo = tk.Label(janela,text = ("QUAL A LIXEIRA?"),font = fonte_titulo,bg=cor_fundo)
        titulo.pack(pady =80)

        botoes = tk.Frame(janela,bg=cor_fundo)
        botoes.pack()

        botao_jogar = tk.Button(botoes,text = "INICIAR",
        font = fonte_botao,width = 15,command = lambda:mudar_tela(2))

        botao_historico = tk.Button(botoes,text = "HISTÓRICO",
        font = fonte_botao,width = 15,command = lambda:mudar_tela(3))

        botao_sair = tk.Button(botoes,text = "SAIR",
        font = fonte_botao,width = 15,command= lambda:mudar_tela(-1))

        botao_jogar.pack(pady = 50)
        botao_historico.pack(pady = 50)
        botao_sair.pack(pady = 50)

    
    elif tela == 2: #TELA DE SELEÇÃO DE DIFICULDADE
        titulo = tk.Label(janela,text = "SELECIONE A DIFICULDADE",font = fonte_titulo,bg = cor_fundo)
        titulo.pack(pady = 80)

        botoes = tk.Frame(janela,bg=cor_fundo)
        botoes.pack()

        facil = tk.Button(botoes, text = "FÁCIL", 
        font = fonte_botao,width=15,command = lambda:mudar_dificuldade(1,mudar_tela))
        medio = tk.Button(botoes, text = "MÉDIO", 
        font = fonte_botao,width=15,command = lambda:mudar_dificuldade(2,mudar_tela))
        dificil = tk.Button(botoes, text = "DIFÍCIL", 
        font = fonte_botao,width=15,command = lambda:mudar_dificuldade(3,mudar_tela))

        facil.pack(pady=30)
        medio.pack(pady=30)
        dificil.pack(pady=30)


    elif tela == 3:#TELA DO JOGO

        global residuo,pontos 

        if dificuldade == 1:
            residuo = tk.Label(janela,text = palavra,font=fonte_titulo,bg=cor_fundo)
            residuo.pack(pady=80)

            pontos = tk.Label(janela,text = f"Pontuacao:{pontuacao}",font = fonte_texto,bg =cor_fundo)
            pontos.place(relx = 0.15,rely=0.13,anchor="center")

            lixeiras = tk.Frame(janela,bg = cor_fundo)
            lixeiras.place(relx=0.5,rely=0.65,anchor="center")

            lixeira_papel = tk.Button(lixeiras,text = "PAPEL",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(1),bg = cor_lixeira_papel)
            lixeira_plastico= tk.Button(lixeiras,text = "PLÁSTICO",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(2),bg=cor_lixeira_plastico)
            lixeira_vidro = tk.Button(lixeiras,text = "VIDRO",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(3),bg = cor_lixeira_vidro)

            lixeira_papel.pack(side = "left",padx=30)
            lixeira_plastico.pack(side = "left",padx=30)
            lixeira_vidro.pack(side="left",padx=30)

        elif dificuldade == 2:
            residuo = tk.Label(janela,text = palavra,font=fonte_titulo,bg=cor_fundo)

            residuo.pack(pady=80)

            pontos = tk.Label(janela,text = f"Pontuacao:{pontuacao}",font = fonte_texto,bg =cor_fundo)
            pontos.place(relx = 0.15,rely=0.13,anchor="center")

            lixeiras = tk.Frame(janela,bg = cor_fundo)
            lixeiras.place(relx=0.5,rely=0.65,anchor="center")

            lixeira_papel = tk.Button(lixeiras,text = "PAPEL",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(1),bg = cor_lixeira_papel)
            lixeira_plastico= tk.Button(lixeiras,text = "PLÁSTICO",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(2),bg=cor_lixeira_plastico)
            lixeira_vidro = tk.Button(lixeiras,text = "VIDRO",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(3),bg = cor_lixeira_vidro)
            lixeira_organica = tk.Button(lixeiras,text = "ORGÂNICO",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(4),bg = cor_lixeira_organicos)

            lixeira_papel.pack(side = "left",padx=30)
            lixeira_plastico.pack(side = "left",padx=30)
            lixeira_vidro.pack(side="left",padx=30)
            lixeira_organica.pack(side ="left",padx=30)

        elif dificuldade == 3:
            residuo = tk.Label(janela,text = palavra,font=fonte_titulo,bg=cor_fundo)

            residuo.pack(pady=80)

            pontos = tk.Label(janela,text = f"Pontuacao:{pontuacao}",font = fonte_texto,bg =cor_fundo)
            pontos.place(relx = 0.15,rely=0.13,anchor="center")

            lixeiras = tk.Frame(janela,bg = cor_fundo)
            lixeiras.place(relx=0.5,rely=0.65,anchor="center")

            lixeira_papel = tk.Button(lixeiras,text = "PAPEL",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(1),bg = cor_lixeira_papel)
            lixeira_plastico= tk.Button(lixeiras,text = "PLÁSTICO",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(2),bg=cor_lixeira_plastico)
            lixeira_vidro = tk.Button(lixeiras,text = "VIDRO",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(3),bg = cor_lixeira_vidro)
            lixeira_organica = tk.Button(lixeiras,text = "ORGÂNICO",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(4),bg = cor_lixeira_organicos)
            lixeira_metal = tk.Button(lixeiras,text = "METAL",
            font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(4),bg = cor_lixeira_metal)
            

            lixeira_papel.pack(side = "left",padx=30)
            lixeira_plastico.pack(side = "left",padx=30)
            lixeira_vidro.pack(side="left",padx=30)
            lixeira_organica.pack(side ="left",padx=30)
            lixeira_metal.pack(side="left",padx=30)


    #elif tela == 4: #TELA DOS RESULTADOS
    #elif tela == 5: #TELA FINAL


def interface(tela,mudar_tela,palavra= None,pontuacao = None):

    #TESTANDO
  
    if tela == 1: #TELA INICIAL
        fundo = tk.Label(janela, image=imagem_tela_1)
        fundo.place(x=0, y=0)


        botao_jogar = tk.Button(janela,image= imagem_iniciar,command = lambda:mudar_tela(2))

        botao_historico = tk.Button(janela,image=imagem_historico,command = lambda:mudar_tela(3))

        botao_sair = tk.Button(janela,image=imagem_sair,command= lambda:mudar_tela(-1))


        botao_jogar.place(relx=0.5, rely=0.35, anchor="center")
        botao_historico.place(relx=0.5, rely=0.50, anchor="center")
        botao_sair.place(relx=0.5, rely=0.65, anchor="center")

    
    elif tela == 2: #TELA DE SELEÇÃO DE DIFICULDADE
        fundo = tk.Label(janela, image=imagem_tela_dificuldade)
        fundo.place(x=0, y=0)



        facil = tk.Button(janela, image=imagem_facil,command = lambda:mudar_dificuldade(1,mudar_tela))
        medio = tk.Button(janela, image=imagem_medio,command = lambda:mudar_dificuldade(2,mudar_tela))
        dificil = tk.Button(janela,image=imagem_dificil,command = lambda:mudar_dificuldade(3,mudar_tela))


        facil.place(relx=0.5, rely=0.35, anchor="center")
        medio.place(relx=0.5, rely=0.50, anchor="center")
        dificil.place(relx=0.5, rely=0.65, anchor="center")





    elif tela == 3:#TELA DO JOGO
        fundo = tk.Label(janela, image=imagem_tela_jogo)
        fundo.place(x=0, y=0)
        global residuo,pontos 

        if dificuldade == 1:


            lixeira_papel = tk.Button(janela,image=imagem_papel,command = lambda:clicar_lixeira(1))
            lixeira_plastico= tk.Button(janela,image=imagem_plastico,command = lambda:clicar_lixeira(2))
            lixeira_vidro = tk.Button(janela,image=imagem_vidro,command = lambda:clicar_lixeira(3))

            
            lixeira_papel.place(relx=0.30, rely=0.65, anchor="center")
            lixeira_plastico.place(relx=0.50, rely=0.65, anchor="center")
            lixeira_vidro.place(relx=0.70, rely=0.65, anchor="center")

        elif dificuldade == 2:


            lixeira_papel = tk.Button(janela,image=imagem_papel,command = lambda:clicar_lixeira(1))
            lixeira_plastico= tk.Button(janela,image=imagem_plastico,command = lambda:clicar_lixeira(2))
            lixeira_vidro = tk.Button(janela,image=imagem_vidro,command = lambda:clicar_lixeira(3))
            lixeira_organica = tk.Button(janela,image=imagem_organico,command = lambda:clicar_lixeira(4))
            

            

            lixeira_papel.place(relx=0.20, rely=0.65, anchor="center")
            lixeira_plastico.place(relx=0.40, rely=0.65, anchor="center")
            lixeira_metal.place(relx=0.60, rely=0.65, anchor="center")
            lixeira_vidro.place(relx=0.80, rely=0.65, anchor="center")

        elif dificuldade == 3:

            lixeira_papel = tk.Button(janela,image=imagem_papel,command = lambda:clicar_lixeira(1))
            lixeira_plastico= tk.Button(janela,image=imagem_plastico,command = lambda:clicar_lixeira(2))
            lixeira_vidro = tk.Button(janela,image=imagem_vidro,command = lambda:clicar_lixeira(3))
            lixeira_organica = tk.Button(janela,image=imagem_organico,command = lambda:clicar_lixeira(4))
            lixeira_metal = tk.Button(janela,image=imagem_metal,command = lambda:clicar_lixeira(5))
            

            
            lixeira_papel.place(relx=0.10, rely=0.65, anchor="center")
            lixeira_plastico.place(relx=0.30, rely=0.65, anchor="center")
            lixeira_metal.place(relx=0.50, rely=0.65, anchor="center")
            lixeira_vidro.place(relx=0.70, rely=0.65, anchor="center")
            lixeira_organica.place(relx=0.90, rely=0.65, anchor="center")


    #elif tela == 4: #TELA DOS RESULTADOS

    #elif tela == 5: #TELA FINAL
    
    janela.mainloop()


