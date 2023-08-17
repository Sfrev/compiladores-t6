import os
import filecmp
import trabalho6 as t6

def main():

    pathEntradas = "casos-de-teste\entradas"
    pathSaidas = "casos-de-teste\saidas"
    pathSaidasEsperadas = "casos-de-teste\saidas-esperadas"

    listaEntradas = sorted(os.listdir(pathEntradas))
    listaSaidasEsperadas = sorted(os.listdir(pathSaidasEsperadas))
    listaSaidas = sorted(os.listdir(pathSaidas))

    for i in range(len(listaSaidas)):
        os.remove(pathSaidas + '\\' + listaSaidas[i])
    
    listPath = []

    for i in range(len(listaEntradas)):
        listPath.append([0, pathEntradas + '\\' + listaEntradas[i], pathSaidas + '\\' + 'saida' + str(i) + '.txt'])

    for i in range(len(listaEntradas)):
        t6.main(listPath[i])

    listaSaidas = sorted(os.listdir(pathSaidas))

    casosDeTeste = len(listaSaidasEsperadas)
    testesCorretos = 0

    for i in range(casosDeTeste):

        print('Testando caso de teste ' + str(i))
        try:
            assert True == filecmp.cmp(pathSaidas + '\\' + listaSaidas[i], pathSaidasEsperadas + '\\' + listaSaidasEsperadas[i])
            print('Teste ' + str(i) + ' passou')
            testesCorretos += 1
            
        except:
            os.rename(pathSaidas + '\\' + listaSaidas[i], pathSaidas + '\\' + 'saida' + str(i) + 'ERRO.txt')
            print('Teste ' + str(i) + ' falhou')
    
    print('\n' + str(testesCorretos) + '/' + str(casosDeTeste) + ' testes passaram\n')


if __name__ == "__main__":
    main()