#FUNÇÕES PARA O AUDIO

import os
import subprocess
import sys

import pyttsx3

processo = None        
ultima_palavra = ""    


def escolher_voz(engine):
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


def falar_agora(texto):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)   # velocidade (menor = mais devagar)
    escolher_voz(engine)
    engine.say(texto)
    engine.runAndWait()


def parar():
    """Corta a fala que estiver acontecendo."""
    global processo
    if processo is not None and processo.poll() is None:
        processo.terminate()
    processo = None


def falar_residuo(palavra):
    """Fala a palavra do resíduo. Chamada pela interface."""
    global processo, ultima_palavra

    if not palavra:                   
        return

    ultima_palavra = palavra
    parar()                           

    try:
        processo = subprocess.Popen(
            [sys.executable, os.path.abspath(__file__), palavra],
            
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
    except Exception as erro:
        print("Aviso: não foi possível falar:", erro)


def repetir():
    """Fala de novo a última palavra."""
    falar_residuo(ultima_palavra)


def tocar_acerto():
    pass


def tocar_erro():
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        falar_agora(sys.argv[1])