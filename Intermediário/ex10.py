# Escreva uma função que retorne a matriz resultante da multiplicação de duas matrizes.

def multiplicar_matrizes(matriz1: list, matriz2: list) -> list:
    if len(matriz1[0]) != len(matriz2):
        return "Número de colunas da matriz1 não é igual ao número de linhas da matriz2"
    
    num_linhas_matriz1 = len(matriz1)
    num_colunas_matriz1 = len(matriz1[0])
    num_colunas_matriz2 = len(matriz2[0])

    resultado = [[0 for _ in range(num_colunas_matriz2)] for _ in range(num_linhas_matriz1)]

    for i in range(num_linhas_matriz1):
        for j in range(num_colunas_matriz2):
            for k in range(num_colunas_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

matriz1 = [
    [1, 2],
    [3, 4]
]

matriz2 = [
    [5, 6],
    [7, 8]
]

resultado = multiplicar_matrizes(matriz1, matriz2)

for linha in resultado:
    print(linha)
