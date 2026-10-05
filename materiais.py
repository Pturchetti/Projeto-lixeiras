
# Lista de resíduos e suas respectivas categorias.

#Lista de resíduos e suas respectivas categorias
import json
import os

#Caminho da pasta do projeto e do arquivo de resíduos
PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_RESIDUOS = os.path.join(
    PASTA_PROJETO,
    "dados",
    "residuos.json"
)

#Carrega os resíduos do JSON
def carregar_materiais():
    try:
        with open(CAMINHO_RESIDUOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Erro: arquivo residuos.json não encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: dados inválidos no residuos.json.")
        return []

#Lista carregada do residuos.json
MATERIAIS = carregar_materiais()

#Retorna materiais da lixeira
def materiais_por_lixeira(numero_lixeira):
    resultado = []
    for material in MATERIAIS:
        if material["lixeira"] == numero_lixeira:
            resultado.append(material)
    return resultado

#Retorna materiais conforme o nível de dificuldade
def materiais_por_dificuldade(dificuldade):
    #Fácil: papel, plástico e vidro
    if dificuldade == 1:
        lixeiras_disponiveis = [1, 2, 3]
    #Médio: adiciona orgânico
    elif dificuldade == 2:
        lixeiras_disponiveis = [1, 2, 3, 4]
    #Difícil: todas lixeiras
    elif dificuldade == 3:
        lixeiras_disponiveis = [1, 2, 3, 4, 5]
    else:
        return []
    resultado = []
    for material in MATERIAIS:
        if material["lixeira"] in lixeiras_disponiveis:
            resultado.append(material)
    return resultado

#Busca um material pela palavra
def buscar_material(palavra):
    for material in MATERIAIS:
        if material["palavra"].lower() == palavra.lower():
            return material
    return None
