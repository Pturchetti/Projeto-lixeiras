# Projeto Lixeiras

Jogo educativo de reciclagem desenvolvido em Python.

## Objetivo

Ensinar crianças a identificar em qual categoria de lixeira diferentes resíduos devem ser descartados.

## Estrutura

- `main.py` — ponto de entrada.
- `jogo.py` — mecânica, respostas, pontuação e progresso.
- `materiais.py` — resíduos e categorias.
- `interface.py` — telas, botões e elementos visuais.
- `audio.py` — recursos de áudio.
- `imagens/` — imagens das lixeiras e materiais.
- `dados/` — histórico das tentativas.

## Equipe

O desenvolvimento é dividido em quatro duplas:

1. Interface e imagens
2. Resíduos e armazenamento em JSON
3. Áudio
4. Mecânica do jogo e integração

## Fluxo

Tela inicial → jogo → resultado final.

Durante o jogo, o usuário recebe um resíduo e escolhe a lixeira correspondente. O sistema informa se a resposta está correta, atualiza a pontuação e apresenta o próximo item.
