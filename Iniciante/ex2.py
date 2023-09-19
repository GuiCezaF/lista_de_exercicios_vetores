'''
Crie uma função que receba dois vetores e retorne a soma deles
'''


def soma_vetores(vetor1: list, vetor2: list) -> list:
    if len(vetor1) != len(vetor2):
        return 'Os vetores devem ser do mesmo tamanho'
    resultado = [0] * len(vetor1)
    for i in range(len(vetor1)):
        resultado[i] = vetor1[i] + vetor2[i]

    return resultado


vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
soma = soma_vetores(vetor1, vetor2)
print(soma)  # Deve imprimir [5, 7, 9]
