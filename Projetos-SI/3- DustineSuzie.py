tam_matriz = int(input())

# fazendo matriz
MATRIZ = []
for linha in range(tam_matriz):
    MATRIZ.append([int(i) for i in input().split(' ')])

# linha horizontal
a, b = 0, 0
for linha in MATRIZ:
    c, d = 0, 0
    soma_par = 0
    rodada = 1
    while rodada < len(linha):
        if soma_par < linha[rodada - 1] + linha[rodada]:
            soma_par = linha[rodada - 1] + linha[rodada]
            c = int(linha[rodada - 1])
            d = int(linha[rodada])
        rodada += 1

    if c + d > a + b:
        a = c
        b = d
horizontal = [a, b]

# linha vertical
a, b = 0, 0
for indice in range(tam_matriz):
    coluna = [linha[indice] for linha in MATRIZ]
    c, d = 0, 0
    soma_par = 0
    rodada = 1
    while rodada < len(coluna):
        if soma_par < coluna[rodada - 1] + coluna[rodada]:
            soma_par = coluna[rodada - 1] + coluna[rodada]
            c = int(coluna[rodada - 1])
            d = int(coluna[rodada])
        rodada += 1

    if c + d > a + b:
        a = c
        b = d
vertical = [a, b]

# linha diagonal
a, b = 0, 0
diagonal_linha = [MATRIZ[indice][indice] for indice in range(tam_matriz)]
c, d = 0, 0
soma_par = 0
rodada = 1
while rodada < len(diagonal_linha):
    if soma_par < diagonal_linha[rodada - 1] + diagonal_linha[rodada]:
        soma_par = diagonal_linha[rodada - 1] + diagonal_linha[rodada]
        c = int(diagonal_linha[rodada - 1])
        d = int(diagonal_linha[rodada])
    rodada += 1
diagonal = [c, d]

# print
s = ''
print(
    f'Falei que era fácil Dustinzinho...\nPegando todas os números que formam as combinações dos pares de cada sentido temos...\nPassword: {s.join([str(i) for i in horizontal])}{s.join([str(i) for i in vertical])}{s.join([str(i) for i in diagonal])}')
