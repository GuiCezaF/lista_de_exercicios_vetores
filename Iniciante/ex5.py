'''
Crie um programa que calcule a média dos elementos de uma matriz
'''


def media_elementos(lista: list) -> float:
    soma = sum(lista)
    indices = len(lista)
    media = soma / indices
    return media

lista = [1, 2, 3, 4, 5]
print(media_elementos(lista))