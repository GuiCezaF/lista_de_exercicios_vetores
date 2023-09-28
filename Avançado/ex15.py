'''
Crie um programa que implemente o método de Jacobi para encontrar os autovalores
de uma matriz simétrica.
'''
import math

def matriz_transposta(matriz: list) -> list:
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def matriz_identidade(n: int):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def produto_matriz(matriz1, matriz2):
    num_linhas_matriz1 = len(matriz1)
    num_colunas_matriz1 = len(matriz1[0])
    num_colunas_matriz2 = len(matriz2[0])

    resultado = [[0 for _ in range(num_colunas_matriz2)] for _ in range(num_linhas_matriz1)]

    for i in range(num_linhas_matriz1):
        for j in range(num_colunas_matriz2):
            for k in range(num_colunas_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

def matriz_simetrica_diagonal(matriz: list) -> bool:
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i != j and abs(matriz[i][j]) > 1e-6:
                return False
    return True

def jacobi(matriz, max_iter=100, tol=1e-6):
    n = len(matriz)
    V = matriz_identidade(n)
    contador = 0

    while contador < max_iter and not matriz_simetrica_diagonal(matriz):
        max_valor = 0
        p, q = 0, 0

        for i in range(n):
            for j in range(i + 1, n):
                if abs(matriz[i][j]) > max_valor:
                    max_valor = abs(matriz[i][j])
                    p, q = i, j

        if max_valor < tol:
            break

        a = matriz[p][p]
        b = matriz[q][q]
        c = matriz[p][q]
        phi = 0.5 * math.atan2(2 * c, (a - b))
        cos_phi = math.cos(phi)
        sin_phi = math.sin(phi)

        rotacao = matriz_identidade(n)
        rotacao[p][p] = cos_phi
        rotacao[q][q] = cos_phi
        rotacao[p][q] = -sin_phi
        rotacao[q][p] = sin_phi

        matriz = produto_matriz(produto_matriz(matriz_transposta(rotacao), matriz), rotacao)
        V = produto_matriz(V, rotacao)
        contador += 1

    autovalores = [matriz[i][i] for i in range(n)]
    return autovalores, V

matriz_simetrica = [
    [4, -2, 2],
    [-2, 2, -4],
    [2, -4, 11]
]

autovalores, autovetores = jacobi(matriz_simetrica)

print("Autovalores:")
print(autovalores)

print("\nAutovetores:")
for vetor in autovetores:
    print(vetor)
