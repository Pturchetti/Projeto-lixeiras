# audio.py
# Lê em voz alta a palavra do resíduo (Windows e Linux), usando pyttsx3.
#
# Como funciona: cada palavra é falada por um processo novo do Python,
# que roda este mesmo arquivo, fala e termina. Isso evita o bug do pyttsx3
# de só falar a primeira vez.

import os
import subprocess
import sys

import pyttsx3

_processo = None        # processo que está falando agora
_ultima_palavra = ""    # última palavra (para o botão "repetir")


# ---------------------------------------------------------------
# PARTE 1: roda dentro do processo novo (quem realmente fala)
# ---------------------------------------------------------------
def _escolher_voz(engine):
    """Procura uma voz em português (do Brasil, de preferência)."""
    vozes = engine.getProperty("voices")
    textos = [(v, f"{v.name} {v.id} {v.languages}".lower()) for v in vozes]

    for voz, texto in textos:
        if any(chave in texto for chave in ("pt-br", "pt_br", "brazil", "brasil", "maria")):
            engine.setProperty("voice", voz.id)
            return

    for voz, texto in textos:
        if "portug" in texto or "pt-pt" in texto:
            engine.setProperty("voice", voz.id)
            return

    print("Aviso: nenhuma voz em português encontrada; usando a voz padrão.")


def _falar_agora(texto):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)   # velocidade (menor = mais devagar)
    _escolher_voz(engine)
    engine.say(texto)
    engine.runAndWait()


# ---------------------------------------------------------------
# PARTE 2: funções que o jogo usa
# ---------------------------------------------------------------
def parar():
    """Corta a fala que estiver acontecendo."""
    global _processo
    if _processo is not None and _processo.poll() is None:
        _processo.terminate()
    _processo = None


def falar_residuo(palavra):
    """Fala a palavra do resíduo. Chamada pela interface."""
    global _processo, _ultima_palavra

    if not palavra:                   # ignora None / texto vazio (fim do jogo)
        return

    _ultima_palavra = palavra
    parar()                           # corta a palavra anterior, se ainda falando

    try:
        _processo = subprocess.Popen(
            [sys.executable, os.path.abspath(__file__), palavra],
            # no Windows, evita abrir uma janelinha preta; no Linux vale 0
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
    except Exception as erro:
        print("Aviso: não foi possível falar:", erro)


def repetir():
    """Fala de novo a última palavra."""
    falar_residuo(_ultima_palavra)


# Funções vazias, só para o interface.py poder chamá-las sem erro.
def tocar_acerto():
    pass


def tocar_erro():
    pass


# ---------------------------------------------------------------
# Quando este arquivo é rodado pelo processo novo, ele fala e acaba.
# ---------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        _falar_agora(sys.argv[1])