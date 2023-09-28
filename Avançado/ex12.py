'''
Crie uma função que encontre os autovalores e autovetores de uma matriz.
'''


def multiplicar_matriz_vetor(matriz: list, vetor: list) -> list:
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    resultado = [0] * num_linhas

    for i in range(num_linhas):
        for j in range(num_colunas):
            resultado[i] += matriz[i][j] * vetor[j]

    return resultado

def encontrar_autovalores_e_autovetores(matriz, iteracoes=1000, tolerancia=1e-6):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    autovetor = [1] * num_colunas

    for _ in range(iteracoes):
        produto = multiplicar_matriz_vetor(matriz, autovetor)

        max_valor = max(produto, key=abs)

        autovetor = [x / max_valor for x in produto]

    # Calcule o autovalor correspondente
    autovalor = max_valor

    return autovalor, autovetor

# Exemplo de uso:
matriz = [
    [2, -1],
    [1, 3]
]

autovalor, autovetor = encontrar_autovalores_e_autovetores(matriz)

print("Autovalor:", autovalor)
print("Autovetor:", autovetor)
