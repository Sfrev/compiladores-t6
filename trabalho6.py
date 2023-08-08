# UFSCar - Departamento de Computação
# Construção de compiladores
# Gerador de Código C para a linguagem LA

# Autor: Igor Teixeira Machado RA: 769708
# Autor: Júlia Aparecida de Sousa RA: 769707
# Autor: Rafael Vinicius Polato Passador RA: 790036

# Para instalar o ANTLR4 no Windows, basta executar o comando abaixo no terminal
# pip install antlr4-python3-runtime

# Para executar o ANTLR4 no Windows, basta executar o comando abaixo no terminal
# java -jar antlr-4.9.2-complete.jar -visitor -Dlanguage=Python3 LA.g4

# Para executar o programa, basta executar o comando abaixo no terminal
# python trabalho5.py <arquivo_entrada> <arquivo_saida>

# Para executar o corretor, basta executar o comando abaixo no terminal
# java -jar <caminho_do_corretor> "<python <caminho_programa>>" gcc <pasta_saidas> <pasta_casos_de_teste> "<RAs dos integrantes>" "t5"
# Exemplo:
# java -jar .\compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar "python C:\Repositorio\Compiladores\compiladores-t5\trabalho5.py" gcc C:\Repositorio\Compiladores\compiladores-t5\saidas C:\Repositorio\Compiladores\casos-de-teste "RA" "t5"

# Importação de bibliotecas
import sys
import traceback
from antlr4 import *
from ABNTLexer import ABNTLexer
from ABNTParser import ABNTParser
from ABNTSemantico import ABNTSemantico
from antlr4.error.ErrorListener import ErrorListener


# Função para escrever a saída em um arquivo
def saidaArquivo(nomeArquivo, saida):
    arquivo = open(nomeArquivo, 'w')
    for linha in saida:
        arquivo.write(f'{linha}\n')

    arquivo.close()


class ABNTParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Erro sintático na linha {line}, coluna {column}: {msg}"
        raise SyntaxError(error_message)

class ABNTLexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        char_position = offendingSymbol.start
        char_value = offendingSymbol.text
        
        # Verifica se o token é um campo vazio
        if char_value.strip() == '':
            error_message = f"Erro léxico na linha {line}, coluna {column}: Campo vazio detectado."
        else:
            error_message = f"Erro léxico na linha {line}, coluna {column}: {msg}. Caractere '{char_value}' na posição {char_position}."
        
        raise ValueError(error_message)


def main(argv):
    # Lendo o camino para o arquivo de entrada e de saída passados na linha de comando
    arquivoEntrada = argv[1]
    arquivoSaida = argv[2]

    # Lista para armazenar a saída
    saida = []

    try:

        # Lendo o arquivo de entrada
        arquivo = FileStream(arquivoEntrada, encoding="utf-8")

        # Criando o analisador léxico
        lexer = ABNTLexer(arquivo)

        # Criando o fluxo de tokens
        stream = CommonTokenStream(lexer)

        # Criando o analisador sintático
        parser = ABNTParser(stream)

        # Removendo os listeners padrões
        #lexer.removeErrorListeners()
        #parser.removeErrorListeners()

        # Adicionando os listeners personalizados
        #lexer.addErrorListener(ABNTLexerErrorListener())
        #parser.addErrorListener(ABNTParserErrorListener())

        # Executando o analisador semântico
        arvore = parser.programa()
        #listener = ABNTSemantico()
        #listener.visitPrograma(arvore)

        # Se existirem erros, eles são mostrados na saída
        #for error in LASemanticoUtils.errosSemanticos:
        #    saida.append(error)

        # Se não houverem erros, o código C é gerado
        #if len(LASemanticoUtils.errosSemanticos) == 0:
        #    codigoC = GeradorCodigoC()
        #    codigoC.visitPrograma(arvore)
        #    for codigo in codigoC.codigo:
        #        saida.append(codigo)

    except Exception as e:
        saida.append(traceback.format_exc())

    saidaArquivo(arquivoSaida, saida)

if __name__ == "__main__":
    main(sys.argv)
