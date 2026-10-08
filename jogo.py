import random
import materiais

dificuldade = 1
pontuacao = 0
acertos = 0
erros = 0
residuo_atual = None    
ultimo_acertou = None 
disponiveis = []
jogados = []  

def iniciar_jogo(nivel): #função para inciar o jogo com as variáveis zeradas e padronizadas
    global dificuldade, pontuacao, acertos, erros, ultimo_acertou, disponiveis, residuo_atual, jogadas, limite, jogados

    dificuldade = nivel
    pontuacao = 0
    acertos = 0
    erros = 0
    ultimo_acertou = None
    residuo_atual = None
    jogadas = 0
    limite = jogadas_dificuldade(nivel)
    disponiveis = materiais.materiais_por_dificuldade(nivel)
    jogados = []

    return novo_residuo()

def jogadas_dificuldade(nivel): #função para definir o limite de jogadas por dificuldade
    if nivel == 1: 
        return 10
    elif nivel == 2:
        return 15
    elif nivel == 3:
        return 20
    else:
        return 0

def novo_residuo(): #função para sempre atualizar o próximo residuo durante o jogo
    global residuo_atual, disponiveis, jogados

    if not disponiveis:
        residuo_atual = None
        return None

    opcoes = [m for m in disponiveis if m["palavra"] not in jogados]

    if not opcoes:
        residuo_atual = None
        return None

    residuo_atual = random.choice(opcoes) #aleatorização do novo residuo a ser printado
    jogados.append(residuo_atual["palavra"])

    return residuo_atual["palavra"]


def palavra_atual():
    #Palavra do resíduo que está na tela (útil para a interface).
    if residuo_atual is None:
        return ""
    return residuo_atual["palavra"]


def resposta(numero): #função que atualiza as estatísticas e a pontuação durante o jogo 
    global pontuacao, acertos, erros, ultimo_acertou, jogadas

    if residuo_atual is None:
        return "", pontuacao

    if numero == residuo_atual["lixeira"]:
        pontuacao += 1
        acertos += 1
        ultimo_acertou = True
    else:
        erros += 1
        ultimo_acertou = False

    jogadas += 1
    if jogadas >= limite:
        return None, pontuacao

    return novo_residuo(), pontuacao


def estatisticas(): #funcao util para contabilidade das estatísticas e inserção no histórico
    total = acertos + erros
    percentual = (acertos / total * 100) if total > 0 else 0
    return {
        "Dificuldade": dificuldade,
        "Pontuação": pontuacao,
        "Acertos": acertos,
        "Erros": erros,
        "Percentual": round(percentual, 1),
    }