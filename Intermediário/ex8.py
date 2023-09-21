def matriz_identidade(n):
    if n <= 0:
        return 'Não é possível criar uma matriz identidade de ordem não positiva'

    identidade = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        identidade.append(linha)

    return identidade


ordem = 4
matriz = matriz_identidade(ordem)
for linha in matriz:
    print(linha)
