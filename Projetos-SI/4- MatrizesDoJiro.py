# pesquisar de calculadora de matrizes
# while rodada < qnt_op: e tambem while rodada < N
# final do while rodada += 1 para finalizar o while
# 2 while pra formar as duas matrizes
# while rodada < N: numeros = input.split(' ') e depois matriz1.append(numeros):
# CRIANDO AS MATRIZES

m1 = []
m2 = []
N = int(input())
rodada = 0
while rodada < N:
    numeros_matrizes1 = input().split(' ')
    for i in range(len(numeros_matrizes1)):
        numeros_matrizes1[i] = int(numeros_matrizes1[i])
    m1.append(numeros_matrizes1)
    rodada += 1
rodada = 0
while rodada < N:
    numeros_matrizes2 = input().split(' ')
    for i in range(len(numeros_matrizes2)):
        numeros_matrizes2[i] = int(numeros_matrizes2[i])
    m2.append(numeros_matrizes2)
    rodada += 1
# m1 = [['31', '21', '46'], ['37', '9', '8'], ['37', '29', '2']]
# m2 = [['10', '12', '40'], ['8', '11', '8'], ['26', '22', '11']]


# CRIAR AS DUAS MATRIZES CONCLUIDO
# CRIAR OPERAÇOES
qtd_op = int(input())
operacoes = []
rodada = 0
while rodada < qtd_op:
    op = input().split(' ')
    operacoes.append(op)
    rodada += 1
# OPERACOES CONCLUIDO
# CRIAR FUNCOES CALCULOS PARA AS MATRIZES
# SOMA


def SomaMatrizes(M1, M2):
    resultado = []
    for a in range(len(M1)):
        resultado.append([])
        for b in range(len(m1[0])):
            resultado[a].append(int(M1[a][b]) + int(M2[a][b]))
    return resultado

# SUBTRAÇAO


def SubMatrizes(M1, M2):
    resultado = []
    for a in range(len(M1)):
        resultado.append([])
        for b in range(len(M1[0])):
            resultado[a].append(int(M1[a][b]) - int(M2[a][b]))
    return resultado

# MULTIPLICAÇAO


def MultiMatrizes(M1, M2):
    def linha(matriz, n):
        return [i for i in matriz[n]]

    def coluna(matriz, n):
        return [i[n] for i in matriz]

    m1linha = len(M1)
    m2coluna = len(M2[0])

    resolucao = []
    for a in range(m1linha):
        resolucao.append([])
        for b in range(m2coluna):
            multi = [x * y for x, y in zip(linha(M1, a), coluna(M2, b))]
            resolucao[a].append(sum(multi))
    return resolucao


def EscalarMatrizes(matriz, k):
    resultado = []
    for l in matriz:
        resultado.append([elemento * k for elemento in l])
    return resultado


# FUNCOES CALCULOS CONCLUIDOS
# CALCULO
# m1 primeiro
resultado = []
for operacao in operacoes:
    if operacao[0] == 'm1' and '*' not in operacao:
        Ma = None
        if operacao[2] == 'm1':
            Ma = m1
        else:
            Ma = m2
        Mb = None
        if operacao[4] == 'm1':
            Mb = m1
        else:
            Mb = m2
        if operacao[3] == '+':
            resultado = SomaMatrizes(Ma, Mb)
            m1 = resultado
        elif operacao[3] == '-':
            resultado = SubMatrizes(Ma, Mb)
            m1 = resultado
        elif operacao[3] == '.':
            resultado = MultiMatrizes(Ma, Mb)
            m1 = resultado
    elif operacao[0] == 'm1' and '*' in operacao:
        A = None
        B = None
        if operacao[2] == 'm1' or operacao[2] == 'm2':
            if operacao[2] == 'm1':
                A = m1
            else:
                A = m2
            B = int(operacao[4])
        else:
            B = int(operacao[2])
            if operacao[4] == 'm1':
                A = m1
            else:
                A = m2
        resultado = EscalarMatrizes(A, B)
        m1 = resultado
# m2 primeiro
    elif operacao[0] == 'm2' and '*' not in operacao:
        Ma = None
        if operacao[2] == 'm1':
            Ma = m1
        else:
            Ma = m2
        Mb = None
        if operacao[4] == 'm1':
            Mb = m1
        else:
            Mb = m2
        if operacao[3] == '+':
            resultado = SomaMatrizes(Ma, Mb)
            m2 = resultado
        elif operacao[3] == '-':
            resultado = SubMatrizes(Ma, Mb)
            m2 = resultado
        elif operacao[3] == '.':
            resultado = MultiMatrizes(Ma, Mb)
            m2 = resultado
    elif operacao[0] == 'm2' and '*' in operacao:
        A = None
        B = None
        if operacao[2] == 'm1' or operacao[2] == 'm2':
            if operacao[2] == 'm1':
                A = m1
            else:
                A = m2
            B = int(operacao[4])
        else:
            B = int(operacao[2])
            if operacao[4] == 'm1':
                A = m1
            else:
                A = m2
        resultado = EscalarMatrizes(A, B)
        m2 = resultado

for linha in resultado:
    s = ' '
    cLinha = [str(a) for a in linha]
    print(s.join(cLinha))
