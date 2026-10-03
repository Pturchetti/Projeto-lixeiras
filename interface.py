import sys
import jogo
import tkinter as tk


#PROPORÇÕES
largura = 1400
altura = 800

botao_largura = 96
botao_altura = 60



#FONTES
fonte_titulo = ("Arial",28,"bold")
fonte_botao = ("Comfortaa",28,"bold")
fonte_texto = ("Arial",28)

#CORES
cor_fundo = ("#FFFFFF")
cor_botao = ("#FAFAFA")
cor_texto = ("#000000")
cor_lixeira_papel = ("#1900FF")
cor_lixeira_plastico = ("#FF0C0C")
cor_lixeira_vidro = ("#098100")
cor_lixeira_metal = ("#FFFB00")
cor_lixeira_organicos = ("#331A1A")


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

        botao_jogar = tk.Button(botoes,text = "INICIAR",font = fonte_botao,width = 15,command = lambda:mudar_tela(2))

        botao_historico = tk.Button(botoes,text = "HISTÓRICO",font = fonte_botao,width = 15,command = lambda:mudar_tela(3))

        botao_sair = tk.Button(botoes,text = "SAIR",font = fonte_botao,width = 15,command= lambda:mudar_tela(-1))

        botao_jogar.pack(pady = 50)
        botao_historico.pack(pady = 50)
        botao_sair.pack(pady = 50)


    
    elif tela == 2: #TELA DE SELEÇÃO DE DIFICULDADE
        titulo = tk.Label(janela,text = "SELECIONE A DIFICULDADE",font = fonte_titulo,bg = cor_fundo)
        titulo.pack(pady = 80)


        botoes = tk.Frame(janela,bg=cor_fundo)
        botoes.pack()

        facil = tk.Button(botoes, text = "FÁCIL", font = fonte_botao,width=15,command = lambda:mudar_dificuldade(1,mudar_tela))
        medio = tk.Button(botoes, text = "MÉDIO", font = fonte_botao,width=15,command = lambda:mudar_dificuldade(2,mudar_tela))
        dificil = tk.Button(botoes, text = "DIFÍCIL", font = fonte_botao,width=15,command = lambda:mudar_dificuldade(3,mudar_tela))


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

            lixeira_papel = tk.Button(lixeiras,text = "PAPEL",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(1),bg = cor_lixeira_papel)
            lixeira_plastico= tk.Button(lixeiras,text = "PLÁSTICO",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(2),bg=cor_lixeira_plastico)
            lixeira_vidro = tk.Button(lixeiras,text = "VIDRO",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(3),bg = cor_lixeira_vidro)

            

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

            lixeira_papel = tk.Button(lixeiras,text = "PAPEL",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(1),bg = cor_lixeira_papel)
            lixeira_plastico= tk.Button(lixeiras,text = "PLÁSTICO",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(2),bg=cor_lixeira_plastico)
            lixeira_vidro = tk.Button(lixeiras,text = "VIDRO",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(3),bg = cor_lixeira_vidro)
            lixeira_organica = tk.Button(lixeiras,text = "ORGÂNICO",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(4),bg = cor_lixeira_organicos)
            

            

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

            lixeira_papel = tk.Button(lixeiras,text = "PAPEL",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(1),bg = cor_lixeira_papel)
            lixeira_plastico= tk.Button(lixeiras,text = "PLÁSTICO",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(2),bg=cor_lixeira_plastico)
            lixeira_vidro = tk.Button(lixeiras,text = "VIDRO",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(3),bg = cor_lixeira_vidro)
            lixeira_organica = tk.Button(lixeiras,text = "ORGÂNICO",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(4),bg = cor_lixeira_organicos)
            lixeira_metal = tk.Button(lixeiras,text = "METAL",font = fonte_texto,width=7,height=3,command = lambda:clicar_lixeira(5),bg = cor_lixeira_metal)
            

            

            lixeira_papel.pack(side = "left",padx=30)
            lixeira_plastico.pack(side = "left",padx=30)
            lixeira_vidro.pack(side="left",padx=30)
            lixeira_organica.pack(side ="left",padx=30)
            lixeira_metal.pack(side="left",padx=30)


    #elif tela == 4: #TELA DOS RESULTADOS

    #elif tela == 5: #TELA FINAL
    

    janela.mainloop()


