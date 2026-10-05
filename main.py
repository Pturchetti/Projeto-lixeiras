# Ponto de entrada do jogo.
import tkinter as tk
import interface
import jogo

tela = 1

def mudar_tela(nova_tela, dificuldade=None):
    global tela

    if nova_tela == -1:
        interface.janela.destroy()
        return

    primeira_palavra = None

    if nova_tela == 3 and dificuldade is not None:
        primeira_palavra = jogo.iniciar_jogo(dificuldade)

        if primeira_palavra is None:
            print("Erro: nenhum resíduo disponível para esta dificuldade.")
            nova_tela = 1

    tela = nova_tela

    for widget in interface.janela.winfo_children():
        widget.destroy()

    interface.interface(tela,mudar_tela,primeira_palavra,jogo.pontuacao)

# A janela precisa existir antes de carregar as imagens
interface.janela = tk.Tk()
interface.janela.title("Jogo educacional de lixeiras")
interface.carregar_imagens()
interface.janela.geometry(f"{interface.largura}x{interface.altura}")
interface.janela.configure(bg=interface.cor_fundo)

interface.interface(tela, mudar_tela)
interface.janela.mainloop()