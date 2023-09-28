'''
Crie um programa que calcule o determinante de uma matriz 3x3.
'''


def calcular_determinante(matriz: list) -> float:
    if len(matriz) != 3 or len(matriz[0]) != 3:
        return "A matriz deve ser 3x3"

    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    determinante = a * (e * i - f * h) - b * \
        (d * i - f * g) + c * (d * h - e * g)

    return determinante


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = calcular_determinante(matriz)
print("O determinante da matriz é:", resultado)
