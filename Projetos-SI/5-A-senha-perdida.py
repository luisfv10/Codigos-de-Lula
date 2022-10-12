def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gerar_fibonacci(tamanho):
    sequencia = []
    for i in range(tamanho):
        sequencia.append(fibonacci(i))
    return sequencia

def fatorial(numero):
    if numero == 0:
        return 1
    else: 
        return numero * fatorial(numero - 1)

def gerar_fatorial(tamanho):
    sequencia = []
    for i in range(tamanho):
        sequencia.append(fatorial(i))
    return sequencia

def adicionar_listas(A, B):
    add = []
    for i in range(len(A)):
        add.append(A[i] + B[i])
    return add

def multiplicas_listas(A, B):
    multi = []
    for i in range(len(A)):
        multi.append(A[i] * B[i])
    return multi

def numero_maior_26(numero):
    if numero < 26:
        return numero
    else:
        return numero_maior_26(numero % 26) #envia o resto p pegar o equivalente

def numero_p_letra(x):
    retorno = []
    for num in x:
        retorno.append(alfabeto[numero_maior_26(num)])
    s = ''
    return s.join(retorno)

def mod11(n):
    return n % 11

senha = input()
n_palavras = int(input())
palavras = []
rodada = 0
while rodada < n_palavras:
    palavras.append(input())
    rodada += 1

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

palavras_possiveis = []

for palavra in palavras:
    comparacao = []
    for letra in palavra:
        indice_mod11 = mod11(alfabeto.index(letra))
        if indice_mod11 != 0:
            sequencia_fibonacci = gerar_fibonacci(indice_mod11)
            sequencia_fatorial = gerar_fatorial(indice_mod11)
            if indice_mod11 % 2 == 0:
                sequencia1 = adicionar_listas(sequencia_fibonacci, sequencia_fatorial)
            else:
                sequencia1 = multiplicas_listas(sequencia_fibonacci, sequencia_fatorial)
            comparacao.append(numero_p_letra(sequencia1))
        else:
            comparacao.append('1')
    s = ''
    palavras_possiveis.append(s.join(comparacao))
if senha in palavras_possiveis:
    print('Achamos! Achamos a senha.')
else:
    print('É... Temos que procurar mais.')
