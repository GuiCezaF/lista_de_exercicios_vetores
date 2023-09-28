# Desenvolva uma função que calcule a matriz inversa de uma matriz quadrada.

def matriz_inversa(matriz: list) -> list:
    if len(matriz) != len(matriz[0]):
        return "A matriz não é quadrada, não possui matriz inversa."

    n = len(matriz)
    
    def determinante(matriz):
        if len(matriz) == 2:
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        
        det = 0
        for j in range(n):
            cofator = matriz[0][j] * determinante(cofator_matriz(matriz, 0, j))
            det += ((-1) ** j) * cofator
        return det

    def matriz_adjunta(matriz):
        adjunta = []
        for i in range(n):
            linha_adjunta = []
            for j in range(n):
                cofator = determinante(cofator_matriz(matriz, i, j))
                linha_adjunta.append(((-1) ** (i + j)) * cofator)
            adjunta.append(linha_adjunta)
        return matriz_transposta(adjunta)

    det = determinante(matriz)
    if det == 0:
        return "A matriz não possui matriz inversa, pois seu determinante é zero."
    
    adjunta = matriz_adjunta(matriz)
    inversa = [[adjunta[i][j] / det for j in range(n)] for i in range(n)]

    return inversa

def matriz_transposta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def cofator_matriz(matriz, linha, coluna):
    return [row[:coluna] + row[coluna + 1:] for row in (matriz[:linha] + matriz[linha + 1:])]

matriz = [
    [2, 1],
    [5, 3]
]

matriz_inversa_resultado = matriz_inversa(matriz)
if isinstance(matriz_inversa_resultado, list):
    for linha in matriz_inversa_resultado:
        print(linha)
else:
    print(matriz_inversa_resultado)
