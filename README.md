Projeto Lixeiras
Sobre o projeto

O Projeto Lixeiras é um jogo educativo desenvolvido em Python com o objetivo de ensinar, de forma simples e interativa, a separação correta de resíduos nas diferentes categorias de lixeiras.

Durante o jogo, o usuário recebe diferentes resíduos e deve escolher em qual lixeira cada um deve ser descartado. O jogo possui diferentes níveis de dificuldade, sistema de pontuação, contagem de acertos e erros, reprodução de áudio e histórico das partidas realizadas.

O projeto foi desenvolvido como atividade acadêmica, envolvendo pesquisa, desenvolvimento de interface, programação, organização de dados, desenvolvimento da mecânica do jogo e integração das diferentes partes realizadas pela equipe.

Objetivo

O principal objetivo do projeto é utilizar um jogo como ferramenta de educação ambiental, auxiliando o usuário a reconhecer diferentes tipos de resíduos e relacioná-los às suas respectivas lixeiras.

Além do aspecto educativo, o projeto teve como objetivos:

Desenvolver uma aplicação gráfica utilizando Python;
Trabalhar com desenvolvimento colaborativo;
Utilizar controle de versões com Git e GitHub;
Trabalhar com arquivos JSON para armazenamento de dados;
Implementar reprodução de áudio;
Desenvolver uma interface gráfica interativa;
Integrar diferentes módulos desenvolvidos pela equipe.
Como o jogo funciona

Ao iniciar o programa, o usuário encontra a tela inicial e pode acessar as diferentes funcionalidades do jogo.

O fluxo principal é:

Tela inicial → Seleção de dificuldade → Jogo → Resultado final

Durante a partida, um resíduo é apresentado na tela e o jogador deve selecionar a lixeira correspondente.

A quantidade de lixeiras e resíduos disponíveis varia de acordo com a dificuldade escolhida:

Dificuldade	Lixeiras	Resíduos
Fácil	3	10
Médio	4	15
Difícil	5	20

A cada resposta, o jogo verifica se a lixeira selecionada corresponde ao resíduo apresentado e atualiza a pontuação, os acertos e os erros.

Ao finalizar todas as jogadas, é apresentada uma tela de conclusão com a pontuação obtida e uma mensagem de parabéns. Nessa tela, o usuário pode voltar ao início ou iniciar uma nova partida.

Telas

O projeto possui 7 telas principais:

1. Tela inicial

É a primeira tela apresentada ao usuário. A partir dela é possível acessar as principais funções do programa.

2. Seleção de dificuldade

Permite escolher entre os níveis Fácil, Médio e Difícil.

A dificuldade determina a quantidade de lixeiras disponíveis e a quantidade de resíduos que serão apresentados durante a partida.

3. Tela do jogo

É a tela principal da partida.

Nela são apresentados:

O resíduo atual;
As lixeiras disponíveis;
A pontuação;
Um botão para reprodução do áudio do resíduo.

O jogador deve selecionar a lixeira correspondente ao resíduo apresentado.

4. Tela final

É apresentada após o término da partida.

Nela são mostrados o resultado obtido e uma mensagem de parabéns. O usuário pode escolher entre voltar ao início ou jogar novamente.

5. Tela de histórico

Apresenta as partidas realizadas anteriormente.

Cada registro contém informações como:

Data;
Dificuldade;
Pontuação;
Quantidade de erros;
Percentual de aproveitamento.

Os dados são armazenados em um arquivo JSON.

6. Tela "Como jogar"

Apresenta as instruções necessárias para entender o funcionamento do jogo.

7. Tela das lixeiras

Apresenta as categorias de lixeiras utilizadas no jogo, auxiliando o usuário a conhecer a função de cada uma.

Tecnologias utilizadas
Tecnologia	Utilização
Python	Linguagem utilizada no desenvolvimento
Tkinter	Construção da interface gráfica
JSON	Armazenamento dos dados dos resíduos e histórico
pyttsx3	Reprodução do nome dos resíduos por áudio
Git	Controle de versões
GitHub	Armazenamento do projeto e colaboração da equipe
VS Code	Editor utilizado durante o desenvolvimento
Canva	Criação de elementos visuais e materiais de apresentação
Organização do projeto

O projeto foi dividido em diferentes partes para permitir que os integrantes trabalhassem simultaneamente em áreas específicas.

Interface

Responsável pela construção da interface gráfica, organização das telas, botões, imagens e elementos visuais do jogo.

Pedro T

Pesquisa inicial sobre a biblioteca utilizada na interface;
Programação da interface;
Desenvolvimento da estrutura inicial das telas.

Isabelle

Desenvolvimento do design da interface;
Programação de algumas das telas;
Organização dos elementos visuais.
Resíduos e histórico

Responsável pela pesquisa e organização das informações utilizadas pelo jogo, além do sistema de armazenamento das partidas.

Fernanda

Pesquisa sobre os diferentes resíduos;
Pesquisa sobre as categorias das lixeiras;
Organização das informações;
Criação do arquivo JSON utilizado pelo jogo.

Seth

Desenvolvimento do sistema de histórico;
Criação do módulo historico.py;
Desenvolvimento da tela de histórico;
Organização e armazenamento dos resultados das partidas.
Áudio

Pedro A e Lorenzo

Os dois integrantes trabalharam conjuntamente na implementação do sistema de áudio.

O áudio utiliza a biblioteca pyttsx3 para transformar o nome do resíduo em fala, permitindo que o usuário escute qual é o resíduo apresentado.

Mecânica do jogo

Gustavo e Hector

Os dois integrantes trabalharam conjuntamente na implementação da lógica principal do jogo.

Essa parte é responsável por:

Controle da partida;
Seleção dos resíduos;
Controle da dificuldade;
Verificação das respostas;
Contagem de acertos;
Contagem de erros;
Controle da pontuação;
Controle da quantidade de jogadas;
Passagem para a tela final.
Principais módulos
main.py

É responsável pela inicialização e integração geral do programa.

Entre suas funções estão:

Criar a janela principal;
Inicializar a interface;
Controlar a mudança entre as telas;
Integrar os diferentes módulos do projeto.
interface.py

Contém a construção das telas e dos elementos gráficos do jogo.

É responsável por:

Criar botões;
Posicionar imagens;
Exibir textos;
Mostrar as diferentes telas;
Conectar os elementos da interface às funções do jogo.
jogo.py

Contém a lógica principal da partida.

É responsável pelo controle de:

Dificuldade;
Resíduo atual;
Pontuação;
Acertos;
Erros;
Quantidade de jogadas;
Seleção dos próximos resíduos;
Verificação das respostas.
materiais.py

Contém os dados dos resíduos utilizados pelo jogo e permite selecionar os materiais de acordo com a dificuldade escolhida.

historico.py

Controla o sistema de histórico das partidas.

O módulo permite carregar os resultados anteriormente registrados e adicionar novas partidas ao arquivo de histórico.

audio.py

Contém as funções relacionadas à reprodução dos nomes dos resíduos utilizando pyttsx3.

Arquivo JSON

Os dados utilizados pelo jogo são armazenados em arquivos no formato JSON, permitindo organizar as informações dos resíduos e os resultados das partidas.

Requisitos

Para executar o projeto é necessário ter:

Python 3
Tkinter
pyttsx3
eSpeak NG em sistemas Linux
Os arquivos do próprio projeto, incluindo imagens, fontes e arquivos JSON.

O projeto não utiliza outras bibliotecas externas além do pyttsx3.

Instalação
1. Instalar o Python

Verifique se o Python está instalado:

python3 --version
2. Instalar o pyttsx3

No terminal:

python3 -m pip install pyttsx3
3. Linux — instalar o eSpeak NG

No Fedora, instale o mecanismo de síntese de voz:

sudo dnf install espeak-ng

O pyttsx3 utiliza esse mecanismo para realizar a síntese de voz no Linux.

Executando o projeto

Entre na pasta do projeto pelo terminal:

cd "caminho/para/Projeto-lixeiras"

Depois execute:

python3 main.py
Observação sobre o VS Code

Durante o desenvolvimento, dependendo da configuração do interpretador Python selecionado no VS Code, o programa pode não executar diretamente pelo botão de execução da IDE, principalmente quando as versões do Python ou as dependências instaladas são diferentes.

Caso isso aconteça, recomenda-se executar o projeto diretamente pelo terminal utilizando o mesmo Python em que as dependências foram instaladas:

python3 main.py
Controle de versões e colaboração

O desenvolvimento foi realizado de forma colaborativa utilizando Git e GitHub.

Cada dupla pôde trabalhar em sua própria parte do projeto, mantendo as alterações organizadas por meio do controle de versões.

O Git foi utilizado para:

Registrar alterações;
Criar e utilizar branches;
Trabalhar em partes diferentes do projeto;
Integrar as contribuições dos integrantes;
Manter o histórico das modificações.

O GitHub foi utilizado como repositório central do projeto, permitindo que os integrantes compartilhassem e integrassem seus códigos.

Estrutura geral

A estrutura do projeto é organizada de forma modular, separando a interface, a lógica do jogo, os dados, o áudio, o histórico e os recursos visuais.

Uma representação simplificada é:

Projeto-lixeiras/
│
├── main.py
├── interface.py
├── jogo.py
├── materiais.py
├── historico.py
├── audio.py
│
├── dados/
│   └── historico.json
│
├── imagens/
│   └── ...
│
├── fontes/
│   └── ...
│
└── README.md

Os arquivos e pastas de recursos visuais podem conter diferentes imagens utilizadas pelas telas e elementos da interface.
