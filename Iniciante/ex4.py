''' 
Crie uma função que verifique se uma matriz é simétrica
'''


def is_symmetric(matriz: list) -> bool:
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    if num_linhas != num_colunas:
        return False

    for i in range(num_linhas):
        for j in range(i + 1, num_colunas):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True


matriz1 = [[1, 2, 3],
           [2, 4, 5],
           [3, 5, 6]]

matriz2 = [[1, 2, 3],
           [2, 4, 5],
           [3, 9, 6]]

print(is_symmetric(matriz1))  # Deve imprimir True
print(is_symmetric(matriz2))  # Deve imprimir False
