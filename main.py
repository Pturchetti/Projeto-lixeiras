# Ponto de entrada do jogo.
import tkinter as tk
from tkinter import messagebox
import interface
import jogo
import historico

tela = 1

def mudar_tela(nova_tela, dificuldade=None):
    global tela

    if nova_tela == 6 and tela != 6:
        try:
            historico.registrar_partida(jogo.estatisticas())
        except (OSError, ValueError) as erro:
            messagebox.showerror(
                "Erro no histórico",
                f"Não foi possível salvar a partida:\n{erro}",
                parent=interface.janela,
            )

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

interface.janela = tk.Tk()
interface.carregar_imagens()
interface.janela.geometry(f"{interface.largura}x{interface.altura}")
interface.janela.configure(bg=interface.cor_fundo)

interface.interface(tela, mudar_tela)
interface.janela.mainloop()