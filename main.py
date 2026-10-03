# Ponto de entrada do jogo.
import interface

def mudar_tela(nova_tela):
    if(nova_tela == -1):
        interface.janela.destroy()
        return

    
    tela = nova_tela


interface.interface(1,0,mudar_tela)