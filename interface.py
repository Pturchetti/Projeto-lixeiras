import sys
import tkinter as tk


#PROPORÇÕES
largura = 1400
altura = 800

botao_largura = 96
botao_altura = 60

lixeira_altura = 100
lixeira_largura = 60
distancia_entre_lixeiras = 150


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


def interface(tela,dificuldade,mudar_tela):
    janela = tk.Tk()
    janela.geometry(f"{largura}x{altura}")
    janela.configure(bg=cor_fundo)

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


    
    #elif tela == 2: #TELA DE SELEÇÃO DE DIFICULDADE

    #elif tela == 3:#TELA DO JOGO

    #elif tela == 4: #TELA DOS RESULTADOS

    #elif tela == 5: #TELA FINAL
    

    janela.mainloop()


