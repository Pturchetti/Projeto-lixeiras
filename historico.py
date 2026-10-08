"""Persistência das partidas em dados/historico.json."""
import json
from datetime import datetime
from pathlib import Path


CAMINHO_HISTORICO = Path("dados/historico.json")


def carregar_partidas():
    if not CAMINHO_HISTORICO.exists():
        return []

    with open(CAMINHO_HISTORICO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def registrar_partida(estatisticas):

    partidas = carregar_partidas()

    partida = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "dificuldade": estatisticas["Dificuldade"],
        "pontuacao": estatisticas["Pontuação"],
        "acertos": estatisticas["Acertos"],
        "erros": estatisticas["Erros"],
        "percentual": estatisticas["Percentual"]
    }

    partidas.append(partida)

    CAMINHO_HISTORICO.parent.mkdir(parents=True, exist_ok=True)

    with open(CAMINHO_HISTORICO, "w", encoding="utf-8") as arquivo:
        json.dump(partidas, arquivo, ensure_ascii=False, indent=2)
