'''
Crie uma função que receba dois vetores e retorne a soma deles
'''


def soma_vetores(vetor_1: list, vetor_2: list) -> float:
    vetor_1.extend(vetor_2)
    soma = sum(vetor_1)
    return soma


lista_1 = [5, 5]
lista_2 = [70, 70]
calcular = soma_vetores(lista_1, lista_2)
print(calcular)
