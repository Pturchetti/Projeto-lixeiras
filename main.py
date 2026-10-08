#main.py: nada especifico, apenas o coração do código
import tkinter as tk
from tkinter import messagebox
import interface
import jogo
import historico

tela = 1 #primeira tela padrão
def mudar_tela(nova_tela, dificuldade=None):
    global tela

    if nova_tela == 6 and tela != 6: #tela do histórico
        try:
            historico.registrar_partida(jogo.estatisticas())
        except (OSError, ValueError) as erro:
            messagebox.showerror(
                "Erro no histórico",
                f"Não foi possível salvar a partida:\n{erro}",
                parent=interface.janela,
            )

    if nova_tela == -1: #se o usuário clicar para sair, a janela deve ser fechada
        interface.janela.destroy()
        return

    primeira_palavra = None

    if nova_tela == 3 and dificuldade is not None: #inicio do jogo se estiver na tela 3
        primeira_palavra = jogo.iniciar_jogo(dificuldade)

    tela = nova_tela #para sempre atualizar a tela

    for widget in interface.janela.winfo_children():
        widget.destroy()

    interface.interface(tela,mudar_tela,primeira_palavra,jogo.pontuacao)

interface.janela = tk.Tk()
interface.carregar_imagens()
interface.janela.geometry(f"{interface.largura}x{interface.altura}")
interface.janela.configure(bg=interface.cor_fundo)

interface.interface(tela, mudar_tela)
interface.janela.mainloop()