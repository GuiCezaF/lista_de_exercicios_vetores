'''
Crie uma função que receba uma matriz e retorne a transposta dela
'''


def matriz_transposta(matriz: list) -> list:
    if not matriz:
        return []

    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    transposta = [[0 for _ in range(num_linhas)] for _ in range(num_colunas)]

    for i in range(num_linhas):
        for j in range(num_colunas):
            transposta[j][i] = matriz[i][j]

    return transposta


matriz_original = [
    [1, 2, 3],
    [4, 5, 6]
]
resultado = matriz_transposta(matriz_original)
for linha in resultado:
    print(linha)
