import jogo
import audio
import tkinter as tk
import historico



#PROPORÇÕES
largura = 1600
altura = 900

#FONTES
fonte_titulo = ("Arial",28,"bold")
fonte_botao = ("Comfortaa",28,"bold")
fonte_texto = ("Arial",28)
fonte_palavras = ("Adigiana Toybox", 60)

#CORES
cor_fundo = ("#FFFFFF")
cor_fundo_bg = ("#e4f2de")
cor_verde_botao = "#396C44"

cor_botao = ("#FAFAFA")
cor_texto = ("#000000")
cor_lixeira_papel = ("#1900FF")
cor_lixeira_plastico = ("#CD0505")
cor_lixeira_vidro = ("#098100")
cor_lixeira_metal = ("#EFEB20")
cor_lixeira_organicos = ("#331A1A")
cor_palavras = ("#5E3F3F")



def carregar_imagens():
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
    global imagem_como_jogar
    global imagem_lixeiras
    global imagem_botao_como_jogar
    global imagem_fundo_palavras
    global imagem_tela_final
    global imagem_jogar_novamente
    global imagem_menu
    global imagem_botao_som

    imagem_botao_som = tk.PhotoImage(file = "imagens/botao_som.png")
    imagem_menu = tk.PhotoImage(file= "imagens/menu.png")
    imagem_jogar_novamente = tk.PhotoImage(file= "imagens/jogar_novamente.png")
    imagem_tela_final = tk.PhotoImage(file = "imagens/tela_final.png")
    imagem_fundo_palavras = tk.PhotoImage(file ="imagens/fundo_palavras.png")
    imagem_lixeiras = tk.PhotoImage(file = "imagens/lixeiras.png")
    imagem_botao_como_jogar = tk.PhotoImage(file = "imagens/como_jogar.png")
    imagem_como_jogar = tk.PhotoImage(file = "imagens/regras.png")
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


#TELAS
#tela 1 inicio
#tela 2 selecao de dificuldade
#tela 3 jogo
#tela 4 como jogar
#tela 5 histórico
#tela 6 parabens por ter jogado
#tela 7 lixeiras


dificuldade = -1
janela = None
residuo = None
pontos = None

def mudar_dificuldade(modo,mudar_tela):
    global dificuldade 
    dificuldade = modo
    mudar_tela(3,modo)

def clicar_lixeira(numero, mudar_tela):
    nova_palavra,nova_pontuacao = jogo.resposta(numero)

    if nova_palavra is None:
        audio.parar()
        mudar_tela(6)
        return

    print("RESIDUO:", residuo)
    residuo.config(text =nova_palavra)
    pontos.config(text =nova_pontuacao)
    audio.falar_residuo(nova_palavra)

def interface(tela,mudar_tela,palavra= None,pontuacao = None):
    global residuo,pontos
    if tela == 1: #TELA INICIAL
        fundo = tk.Label(janela, image=imagem_tela_1)
        fundo.place(x=0, y=0)

        botao_jogar = tk.Button(janela,image= imagem_iniciar,command = lambda:mudar_tela(2))
        botao_como_jogar = tk.Button(janela,image=imagem_botao_como_jogar,command = lambda:mudar_tela(4))
        botao_historico = tk.Button(janela,image=imagem_historico,command=lambda:mudar_tela(5))
        botao_sair = tk.Button(janela,image=imagem_sair,command= lambda:mudar_tela(-1))

        botao_jogar.place(relx=0.5, rely=0.35, anchor="center")
        botao_como_jogar.place(relx=0.5, rely=0.50, anchor="center")
        botao_historico.place(relx=0.5, rely=0.65, anchor="center")
        botao_sair.place(relx=0.5, rely=0.80, anchor="center")
    
    elif tela == 2: #TELA DE SELEÇÃO DE DIFICULDADE
        fundo = tk.Label(janela, image=imagem_tela_dificuldade)
        fundo.place(x=0, y=0)

        facil = tk.Button(janela, image=imagem_facil,command = lambda:mudar_dificuldade(1,mudar_tela))
        medio = tk.Button(janela, image=imagem_medio,command = lambda:mudar_dificuldade(2,mudar_tela))
        dificil = tk.Button(janela,image=imagem_dificil,command = lambda:mudar_dificuldade(3,mudar_tela))

        facil.place(relx=0.5, rely=0.35, anchor="center")
        medio.place(relx=0.5, rely=0.50, anchor="center")
        dificil.place(relx=0.5, rely=0.65, anchor="center")

    elif tela == 3:
        fundo = tk.Label(janela, image=imagem_tela_jogo)
        fundo.place(x=0, y=0)
        print("PALAVRA NA INTERFACE:", palavra)

        fundo_palavra = tk.Label(janela,image = imagem_fundo_palavras, bg = cor_fundo_bg)
        fundo_palavra.place(relx = 0.49, rely = 0.32, anchor = "center")
        residuo = tk.Label(janela,text=palavra,font=fonte_palavras,bg=cor_fundo_bg,fg = cor_palavras)
        residuo.place(relx = 0.5, rely = 0.30,anchor= "center")
        audio.falar_residuo(palavra)
        botao_ouvir = tk.Button(janela,image= imagem_botao_som, command=audio.repetir)
        botao_ouvir.place(relx=0.78, rely=0.30, anchor="center")

        pontos = tk.Label(janela,text=f"{pontuacao}",font=fonte_palavras,bg=cor_fundo_bg, fg = cor_palavras)
        pontos.place(relx=0.23, rely=0.09, anchor="center")

        if dificuldade == 1:
            

            lixeira_papel = tk.Button(janela,image=imagem_papel,command = lambda:clicar_lixeira(1,mudar_tela))
            lixeira_plastico= tk.Button(janela,image=imagem_plastico,command = lambda:clicar_lixeira(2,mudar_tela))
            lixeira_vidro = tk.Button(janela,image=imagem_vidro,command = lambda:clicar_lixeira(3,mudar_tela))

            lixeira_papel.place(relx=0.30, rely=0.65, anchor="center")
            lixeira_plastico.place(relx=0.50, rely=0.65, anchor="center")
            lixeira_vidro.place(relx=0.70, rely=0.65, anchor="center")

        elif dificuldade == 2:
            lixeira_papel = tk.Button(janela,image=imagem_papel,command = lambda:clicar_lixeira(1,mudar_tela))
            lixeira_plastico= tk.Button(janela,image=imagem_plastico,command = lambda:clicar_lixeira(2,mudar_tela))
            lixeira_vidro = tk.Button(janela,image=imagem_vidro,command = lambda:clicar_lixeira(3,mudar_tela))
            lixeira_organica = tk.Button(janela,image=imagem_organico,command = lambda:clicar_lixeira(4,mudar_tela))

            lixeira_papel.place(relx=0.20, rely=0.65, anchor="center")
            lixeira_plastico.place(relx=0.40, rely=0.65, anchor="center")
            lixeira_vidro.place(relx=0.60, rely=0.65, anchor="center")
            lixeira_organica.place(relx=0.80, rely=0.65, anchor="center")

        elif dificuldade == 3:

            lixeira_papel = tk.Button(janela,image=imagem_papel,command = lambda:clicar_lixeira(1,mudar_tela))
            lixeira_plastico= tk.Button(janela,image=imagem_plastico,command = lambda:clicar_lixeira(2,mudar_tela))
            lixeira_vidro = tk.Button(janela,image=imagem_vidro,command = lambda:clicar_lixeira(3,mudar_tela))
            lixeira_organica = tk.Button(janela,image=imagem_organico,command = lambda:clicar_lixeira(4,mudar_tela))
            lixeira_metal = tk.Button(janela,image=imagem_metal,command = lambda:clicar_lixeira(5,mudar_tela))

            lixeira_papel.place(relx=0.10, rely=0.65, anchor="center")
            lixeira_plastico.place(relx=0.30, rely=0.65, anchor="center")
            lixeira_metal.place(relx=0.50, rely=0.65, anchor="center")
            lixeira_vidro.place(relx=0.70, rely=0.65, anchor="center")
            lixeira_organica.place(relx=0.90, rely=0.65, anchor="center")


    elif tela == 4: #TELA DE COMO JOGAR
        fundo = tk.Label(janela,image = imagem_como_jogar, bg = cor_fundo)
        fundo.place(x = 0, y = 0)

        botao_voltar = tk.Button(janela,image=imagem_sair,command = lambda:mudar_tela(1))
        botao_voltar.place(relx = 0.2,rely = 0.8, anchor= "center")

    elif tela == 5:  # TELA DO HISTÓRICO

        fundo = tk.Label(janela, image=imagem_background, bg=cor_fundo_bg)
        fundo.place(x=0, y=0, relwidth=1, relheight=1)

        titulo = tk.Label(janela,text="Histórico de Partidas",font=("Adigiana Toybox", 44),bg=cor_verde_botao,fg=cor_fundo_bg)
        titulo.place(relx=0.5, rely=0.08, anchor="center")

        partidas = historico.carregar_partidas()

        lista = tk.Listbox(janela,font=("Adigiana Toybox", 16),bg=cor_verde_botao,fg=cor_fundo_bg,activestyle="none",bd=0)

        for partida in reversed(partidas):

            if partida["dificuldade"] == 1:
                nome_dificuldade = "Fácil"
            elif partida["dificuldade"] == 2:
                nome_dificuldade = "Médio"
            else:
                nome_dificuldade = "Difícil"

            texto = (f'{partida["data"]} | {nome_dificuldade} | 'f'Pontos: {partida["pontuacao"]} | 'f'Erros: {partida["erros"]} | 'f'{partida["percentual"]:.1f}%')

            lista.insert(tk.END, texto)

        lista.place(relx=0.5,rely=0.48,anchor="center",relwidth=0.78,relheight=0.66)

        botao_voltar = tk.Button(janela,image=imagem_sair,command=lambda: mudar_tela(1))
        botao_voltar.place(relx=0.5, rely=0.88, anchor="center")

    elif tela == 6: #TELA DO PARABENS POR TER JOGADO
        fundo = tk.Label(janela, image=imagem_tela_final)
        fundo.place(x=0, y=0)


        pontos = tk.Label(janela,text=f"{pontuacao}",font=fonte_palavras,bg=cor_fundo_bg, fg = cor_palavras)
        pontos.place(relx=0.64, rely=0.30, anchor="center")

        botao_jogar_novamente = tk.Button(janela, image=imagem_jogar_novamente,command=lambda: mudar_tela(2))
        botao_menu = tk.Button(janela, image=imagem_menu,command=lambda: mudar_tela(1))

        botao_jogar_novamente.place(relx=0.52, rely=0.50, anchor="center")
        botao_menu.place(relx=0.52, rely=0.70, anchor="center")
    #elif tela == 7:



