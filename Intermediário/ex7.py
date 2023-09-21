'''
Crie uma função que multiplique uma matriz por um escalar
'''


def multiplicar_matriz_por_escalar(matriz: list, escalar: list) -> list:
    if not matriz:
        return []

    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    matriz_resultante = [
        [0 for _ in range(num_colunas)] for _ in range(num_linhas)]

    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz_resultante[i][j] = matriz[i][j] * escalar

    return matriz_resultante


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

escalar = 2

resultado = multiplicar_matriz_por_escalar(matriz, escalar)
for linha in resultado:
    print(linha)
