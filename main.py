# Ponto de entrada do jogo.
import tkinter as tk
import interface

tela = 1

def mudar_tela(nova_tela):
    global tela

    if nova_tela == -1:
        interface.janela.destroy()
        return

    tela = nova_tela

    for widget in interface.janela.winfo_children():
        widget.destroy()


    interface.interface(tela, mudar_tela)


    interface.interface(tela, mudar_tela)

interface.janela = tk.Tk()
interface.carregar_imagens()
interface.janela.geometry(f"{interface.largura}x{interface.altura}")
interface.janela.configure(bg=interface.cor_fundo)

interface.interface(tela, mudar_tela)

interface.janela.mainloop()