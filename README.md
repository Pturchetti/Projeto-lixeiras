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

## Como executar o projeto

### 1. Abrir o terminal

Abra o terminal e entre na pasta do projeto utilizando `cd`.

Exemplo:

```bash
cd "/caminho/para/Projeto-lixeiras"
```

> **Importante:** execute o projeto a partir da pasta principal do repositório, onde estão `main.py`, `interface.py`, `jogo.py` e a pasta `imagens/`.

### 2. Executar o programa

Depois de entrar na pasta do projeto, execute:

```bash
python3 main.py
```

No Windows, caso `python3` não funcione, tente:

```bash
python main.py
```

### 3. Caso seja necessário instalar as bibliotecas

As dependências do projeto estão no arquivo `requirements.txt`.

Execute:

```bash
pip install -r requirements.txt
```

Depois, execute novamente:

```bash
python3 main.py
```

### Observação sobre o VS Code

O projeto pode ser executado diretamente pelo terminal. Caso o VS Code apresente problemas relacionados ao interpretador Python ou ao Tkinter, recomenda-se executar os comandos acima pelo terminal do sistema.


## Interface.py

A interface do projeto está sendo desenvolvida utilizando **Python e Tkinter**. Ela é responsável pela apresentação visual do jogo e pela interação do usuário com as opções disponíveis.

### Funcionalidades implementadas

* Criação da janela principal do jogo com tamanho definido de **1400 × 800 pixels**.
* Definição de fontes, cores e proporções utilizadas pelos elementos da interface.
* Criação da **tela inicial**, contendo:

  * Botão **Iniciar**;
  * Botão **Histórico**;
  * Botão **Sair**.
* Criação da **tela de seleção de dificuldade**, contendo:

  * Fácil;
  * Médio;
  * Difícil.
* Armazenamento da dificuldade selecionada para utilização nas demais telas.
* Criação da **tela principal do jogo**.
* Exibição do resíduo que deve ser classificado.
* Exibição da pontuação atual.
* Criação das lixeiras como botões interativos.
* Organização das lixeiras horizontalmente e posicionamento dos elementos na tela.
* Diferenciação visual das lixeiras por meio de cores.
* Quantidade de lixeiras relacionada à dificuldade selecionada:

  * **Fácil:** 3 lixeiras;
  * **Médio:** 4 lixeiras;
  * **Difícil:** 5 lixeiras.
* Os botões das lixeiras foram preparados para enviar um identificador da lixeira selecionada para a função responsável pela mecânica do jogo.
* A interface foi estruturada para permitir que o texto do resíduo e a pontuação sejam atualizados sem a necessidade de recriar a janela.

### Comunicação com a mecânica do jogo

A interface não é responsável por determinar se uma resposta está correta. Ao clicar em uma lixeira, ela envia um identificador para a função de resposta da mecânica.

Exemplo:

```python
command=lambda: clicar_lixeira(1)
```

Nesse caso, `1` representa a lixeira de papel.

A função `clicar_lixeira()` será responsável por encaminhar essa escolha para a mecânica e receber as informações atualizadas para modificar a interface.

### Informações que a interface precisa receber da mecânica

Para completar a integração da tela do jogo, a interface precisa receber:

* **Próximo resíduo:** palavra que deverá ser exibida na tela;
* **Pontuação atualizada:** para atualizar o contador de pontos;
* **Indicação de fim de jogo:** para saber quando deve passar para a tela de resultados;
* **Resultado da resposta**, caso seja utilizado para apresentar algum feedback ao jogador;
* **Quantidade total de resíduos ou progresso atual**, caso seja exibido na interface.

A mecânica do jogo será responsável por determinar essas informações. A interface apenas apresentará os valores recebidos.

### Integrações ainda necessárias

Para finalizar a interface, ainda é necessária a integração com:

**`jogo.py`**

* Função responsável por receber a lixeira selecionada;
* Verificação da resposta;
* Atualização da pontuação;
* Seleção do próximo resíduo;
* Controle do progresso;
* Indicação de quando o jogo terminou.

**`materiais.py`**

* Lista de resíduos disponíveis;
* Categoria correspondente a cada resíduo;
* Informações que serão utilizadas pela mecânica para selecionar os resíduos.

**`dados/historico.json`**

* Recebimento dos resultados das partidas;
* Utilização dos dados para preencher a tela de histórico.

**`audio.py`**

* Reprodução do nome do resíduo;
* Reprodução de instruções ou feedbacks sonoros, caso essa funcionalidade seja utilizada.

**`main.py`**

* Controle do estado geral da aplicação;
* Integração entre as telas e as demais partes do projeto;
* Controle da mudança entre tela inicial, dificuldade, jogo, resultados e histórico.

