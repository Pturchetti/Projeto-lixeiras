"""Persistência das partidas em dados/historico.json."""

import json
from datetime import datetime
from pathlib import Path
from typing import TypedDict


CAMINHO_HISTORICO = Path(__file__).resolve().parent / "dados" / "historico.json"


class Partida(TypedDict):
    data: str
    dificuldade: int
    pontuacao: int
    acertos: int
    erros: int
    percentual: float


def carregar_partidas() -> list[Partida]:
    try:
        with CAMINHO_HISTORICO.open("r", encoding="utf-8") as arquivo:
            partidas = json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as erro:
        raise ValueError("O arquivo de histórico contém JSON inválido.") from erro

    if not isinstance(partidas, list):
        raise ValueError("O arquivo de histórico possui um formato inválido.")

    partidas_validas: list[Partida] = []
    for partida in partidas:
        if not isinstance(partida, dict):
            raise ValueError("O arquivo de histórico possui uma partida inválida.")

        data = partida.get("data")
        dificuldade = partida.get("dificuldade")
        pontuacao = partida.get("pontuacao")
        acertos = partida.get("acertos")
        erros = partida.get("erros")
        percentual = partida.get("percentual")

        if (
            not isinstance(data, str)
            or not isinstance(dificuldade, int)
            or isinstance(dificuldade, bool)
            or not isinstance(pontuacao, int)
            or isinstance(pontuacao, bool)
            or not isinstance(acertos, int)
            or isinstance(acertos, bool)
            or not isinstance(erros, int)
            or isinstance(erros, bool)
            or not isinstance(percentual, (int, float))
            or isinstance(percentual, bool)
        ):
            raise ValueError("O arquivo de histórico possui uma partida inválida.")

        partidas_validas.append(
            {
                "data": data,
                "dificuldade": dificuldade,
                "pontuacao": pontuacao,
                "acertos": acertos,
                "erros": erros,
                "percentual": float(percentual),
            }
        )

    return partidas_validas


def registrar_partida(estatisticas: dict[str, int | float]) -> None:
    partidas = carregar_partidas()
    partidas.append(
        {
            "data": datetime.now().astimezone().strftime("%d/%m/%Y %H:%M"),
            "dificuldade": int(estatisticas["Dificuldade"]),
            "pontuacao": int(estatisticas["Pontuação"]),
            "acertos": int(estatisticas["Acertos"]),
            "erros": int(estatisticas["Erros"]),
            "percentual": float(estatisticas["Percentual"]),
        }
    )

    CAMINHO_HISTORICO.parent.mkdir(parents=True, exist_ok=True)
    with CAMINHO_HISTORICO.open("w", encoding="utf-8") as arquivo:
        json.dump(partidas, arquivo, ensure_ascii=False, indent=2)
