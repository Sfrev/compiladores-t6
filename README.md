# Trabalho 06 - Construção de Compiladores

## Documentação Externa

### Integrantes do Grupo:

- Igor Teixeira Machado (RA: 769708)
- Júlia Aparecida Sousa de Oliveira (RA: 769707)
- Rafael Vinicius Polato Passador (RA: 790036)

### Introdução

Esse trabalho trata-se do projeto final da disciplina de Compiladores, como parte da avaliação de desempenho da mesma. Os autores tem como objetivo a implementação de um compilador que irá executar um gerador markdown de referências de livros e artigos de acordo com o padrão estabelecido Associação Brasileira de Normas Técnicas (ABNT) para textos técnicos e científicos, a partir da linguagem criada. 

Para o desenvolvimento do trabalho, utilizou-se da linguagem Python e da ferramenta ANTLR4, já implementado em projetos anteriores.

O compilador será capaz de receber um arquivo de entrada no formato especificado, indicar se há alguma informação preenchida erroneamente ou faltante e em caso de adequação às regras estabelecidas gerar o markdown com citação já padronizada pela ABNT

### Modo de Execução e Compilação

#### Instalação do ANTLR4 no Windows
Utilize o seguinte comando no terminal:
```
pip install antlr4-python3-runtime
```
#### Execução do ANTLR4 no Windows
Utilize o seguinte comando no terminal:
```
java -jar antlr-4.9.2-complete.jar -visitor -Dlanguage=Python3 ABNT.g4
```
#### Execução do Código do Trabalho
Utilize o seguinte comando no terminal:
```
python trabalho6.py <arquivo_entrada>.txt <arquivo_saida>.md
```
Certifique-se que o formato do arquivo de saída é .md
#### Uso do Corretor
Para utilizar o corretor, siga as seguintes etapas:
1. Execute o seguinte comando no terminal para iniciar o corretor:
```
python testador.py
```
1. Certifique-se de possuir a pasta "casos-de-teste" no mesmo diretório do arquivo "testador.py" e as pastas "entradas", "saidas" e "saidas-esperadas" dentro da pasta de "casos-de-teste".

#### Link do vídeo de apresentação do grupo 
(inserir)
