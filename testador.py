import os
import trabalho6 as t6

def main():

    pathEntradas = "casos-de-teste\entradas"
    pathSaidas = "casos-de-teste\saidas"
    pathSaidasEsperadas = "casos-de-teste\saidas-esperadas"

    listaEntradas = sorted(os.listdir(pathEntradas))
    listaSaidas = sorted(os.listdir(pathSaidas))
    listaSaidasEsperadas = sorted(os.listdir(pathSaidasEsperadas))
    
    listPath = []

    for i in range(len(listaEntradas)):
        listPath.append([0, pathEntradas + '\\' + listaEntradas[i], pathSaidas + '\\' + listaSaidas[i]])

    for i in range(len(listaEntradas)):
        t6.main(listPath[i])

    for i in range(len(listaSaidas)):
        assert listaSaidas[i] == listaSaidasEsperadas[i]

if __name__ == "__main__":
    main()