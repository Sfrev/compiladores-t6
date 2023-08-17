# Trabalho 06 - Construção de Compiladores

## Documentação Externa

### Integrantes do Grupo:

- Igor Teixeira Machado (RA: 769708)
- Júlia Aparecida Sousa de Oliveira (RA: 769707)
- Rafael Vinicius Polato Passador (RA: 790036)

### Introdução

Este relatório apresenta o trabalho desenvolvido pela equipe composta pelos integrantes acima mencionados, como atividade avaliativa da disciplina de Construção de Compiladores. O objetivo do trabalho foi a implementação de um gerador markdown de referências no padrão ABNT a partir de uma linguagem criada pelos integrantes. O trabalho foi desenvolvido utilizando a linguagem Python e a ferramenta ANTLR4.

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
python trabalho6.py <arquivo_entrada> <arquivo_saida>
```
#### Uso do Corretor
Para utilizar o corretor, siga as seguintes etapas:
1. Execute o seguinte comando no terminal para iniciar o corretor:
```
python testador.py
```
1. Certifique-se de possuir a pasta "casos-de-teste" no mesmo diretório do arquivo "testador.py" e as pastas "entradas", "saidas" e "saidas-esperadas" dentro da pasta de "casos-de-teste".
