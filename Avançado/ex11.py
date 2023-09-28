'''
implemente uma função
que calcule o produto vetorial entre dois vetores tridimensionais.
'''
def produto_vetorial(vetor1: list, vetor2: list) -> list:
    if len(vetor1) != 3 or len(vetor2) != 3:
        return "Ambos os vetores devem ser tridimensionais (ter 3 elementos)."

    a1, a2, a3 = vetor1
    b1, b2, b3 = vetor2

    resultado = [
        a2 * b3 - a3 * b2,
        a3 * b1 - a1 * b3,
        a1 * b2 - a2 * b1
    ]

    return resultado

vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]

produto = produto_vetorial(vetor1, vetor2)
print("Produto Vetorial:", produto)
