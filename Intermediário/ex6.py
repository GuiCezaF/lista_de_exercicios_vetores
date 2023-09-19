'''
Implemente uma função que calcule o produto escalar entre dois vetores.
'''


def produto_escalar(vetor1: list, vetor2: list) -> float:
    if len(vetor1) != len(vetor2):
        return 'Os vetores devem ser do mesmo tamanho'
    resultado = 0
    for i in range(len(vetor1)):
        resultado += vetor1[i] * vetor2[i]

    return resultado


vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]

produto = produto_escalar(vetor1, vetor2)
print(produto)
