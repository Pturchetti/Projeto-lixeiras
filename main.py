# Ponto de entrada do jogo.
import tkinter as tk
import interface
import jogo
import materiais

tela = 1

def mudar_tela(nova_tela, dificuldade=None):
    global tela

    if nova_tela == -1:
        interface.janela.destroy()
        return

    # Ao entrar na tela do jogo com uma dificuldade escolhida, começa uma nova partida
    if nova_tela == 3 and dificuldade is not None:
        primeira_palavra = jogo.iniciar_jogo(dificuldade)

        # Se não carregou nenhum resíduo,volta ao menu
        if primeira_palavra is None:
            print("Erro: nenhum resíduo disponível para esta dificuldade.")
            nova_tela = 1

    tela = nova_tela

    # Limpa a tela atual antes de desenhar a nova
    for widget in interface.janela.winfo_children():
        widget.destroy()

    interface.interface(tela, mudar_tela)


# A janela precisa existir antes de carregar as imagens
interface.janela = tk.Tk()
interface.janela.title("Jogo educacional de lixeiras")
interface.carregar_imagens()
interface.janela.geometry(f"{interface.largura}x{interface.altura}")
interface.janela.configure(bg=interface.cor_fundo)

interface.interface(tela, mudar_tela)
interface.janela.mainloop()