
'''
Crie um campo minado em Python de tamanho personalizado.
'''


from random import randint


def criar_campo_minado(linhas, colunas, num_minas):
    campo = [['⬛' for _ in range(colunas)] for _ in range(linhas)]

    minas_colocadas = 0
    while minas_colocadas < num_minas:
        linha = randint(0, linhas - 1)
        coluna = randint(0, colunas - 1)
        if campo[linha][coluna] != '💣':
            campo[linha][coluna] = '💣'
            minas_colocadas += 1

    return campo


def imprimir_campo(campo):
    for linha in campo:
        print(' '.join(linha))


linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))
num_minas = int(input("Número de minas: "))

campo_minado = criar_campo_minado(linhas, colunas, num_minas)
imprimir_campo(campo_minado)
