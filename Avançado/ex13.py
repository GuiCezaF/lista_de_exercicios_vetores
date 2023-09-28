'''
Implemente um programa que resolva um sistema de equações lineares usando a matriz aumentada
e o método deeliminação de Gauss.
'''

def eliminacao_de_gauss(matriz_aumentada: list) -> list:
    num_linhas = len(matriz_aumentada)
    num_colunas = len(matriz_aumentada[0])

    for coluna_pivot in range(num_colunas - 1):
        max_valor = abs(matriz_aumentada[coluna_pivot][coluna_pivot])
        max_linha = coluna_pivot
        for i in range(coluna_pivot + 1, num_linhas):
            if abs(matriz_aumentada[i][coluna_pivot]) > max_valor:
                max_valor = abs(matriz_aumentada[i][coluna_pivot])
                max_linha = i


        if max_linha != coluna_pivot:
            matriz_aumentada[coluna_pivot], matriz_aumentada[max_linha] = matriz_aumentada[max_linha], matriz_aumentada[coluna_pivot]

        for i in range(coluna_pivot + 1, num_linhas):
            fator = -matriz_aumentada[i][coluna_pivot] / matriz_aumentada[coluna_pivot][coluna_pivot]
            for j in range(coluna_pivot, num_colunas):
                matriz_aumentada[i][j] += fator * matriz_aumentada[coluna_pivot][j]

    return matriz_aumentada

def substituicao_regressiva(matriz_aumentada: list) -> list:
    num_linhas = len(matriz_aumentada)
    solucao = [0] * num_linhas

    for i in range(num_linhas - 1, -1, -1):
        solucao[i] = matriz_aumentada[i][-1] / matriz_aumentada[i][i]
        for j in range(i - 1, -1, -1):
            matriz_aumentada[j][-1] -= matriz_aumentada[j][i] * solucao[i]

    return solucao

def resolver_sistema(matriz_aumentada: list) -> list:
    matriz_triangular = eliminacao_de_gauss(matriz_aumentada)
    solucao = substituicao_regressiva(matriz_triangular)
    return solucao

matriz_aumentada = [
    [2, 1, 1,  8],
    [1, 3, 2, 11],
    [1, 0, 0,  3]
]

solucao = resolver_sistema(matriz_aumentada)
print("Solução do sistema:", solucao)
