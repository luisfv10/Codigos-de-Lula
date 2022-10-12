# ENTRADAS
n_mochilas = int(input())
nomes = input().split(' ')

tam_mochila = []
rodada = 0
while n_mochilas > rodada:  # rodada maior que n continuar rodando
    tam_mochila.append(int(input()))
    rodada += 1

n_itens = int(input())

# Como montar as mochilas
mochila = []
rodada = 0
while rodada < n_mochilas:
    mochila.append(['Lanterna', 'Omega 3 da top therm'])
    rodada += 1

# Colocando os itens
rodada = 0
while n_itens > rodada:
    item = input()
    indice = int(input())
    # se tam da mochila maior que o indice da mochila
    if len(mochila[indice]) < tam_mochila[indice]:
        mochila[indice].append(item)  # add item
    else:
        print('Mochila cheia. Não vai dar para levar.')
    rodada += 1

# 1A PARTE FINALIZADA PARTE DE ADD MOCHILA E ITENS

# ACOES
# variaveis açoes possiveis
remover_item = 'Tirar da mochila'
guardar_item = 'Guardar na mochila'
chegamo = 'CHEGAMOS NO CIN!'

cond_while = True  # condicao pra parar while, qnd eles chegarem vira falso
rodada = 0
while cond_while:
    acao = input()

    if acao == remover_item:
        item = input()
        indice_mochila = int(input())
        if item in mochila[indice_mochila]:
            mochila[indice_mochila].remove(item)
            print(f'{item} usado com sucesso da mochila {indice_mochila}.')
        else:
            print(f'Você não tem {item} na mochila {indice_mochila}.')

    elif acao == guardar_item:
        item = input()
        indice_mochila = int(input())
        if len(mochila[indice_mochila]) < tam_mochila[indice_mochila]:
            mochila[indice_mochila].append(item)
            print(f'{item} adicionado na mochila {indice_mochila}.')
        else:
            print(f'Mochila {indice_mochila} cheia!')

    elif acao == chegamo:
        cond_while = False
    else:
        print('Ação inválida.')

# 2A PARTE FINALIZADA OQ FAZER CASO RECEBER AS ACOES

# SAIDAS
rodada = 0
while rodada < len(mochila):
    print(f'Mochila de {nomes[rodada]} chegou assim:')

    rodada2 = 0
    while rodada2 < len(mochila[rodada]):
        print(mochila[rodada][rodada2])
        rodada2 += 1
    rodada += 1
