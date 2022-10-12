# entrada
n_estrelas = int(input())
# so comecar a rodar se possuir mais de 3 estrelas
if(n_estrelas > 3):
    x_antes = 0
    y_antes = 0
    soma_distancias = 0
    rodada_n_fibonacci = 0

# while enqnt tiver mais estrela doq rodadas continuar rodando
    rodada = 0
    while(rodada < n_estrelas):
        x = int(input())
        y = int(input())
# calcular a distancia da estrela
        if(rodada != 0):
            distancia = int(((x_antes - x) ** 2 + (y_antes - y) ** 2) ** 0.5)
            print(
                f'Distância [star{rodada} <-> star{rodada + 1}]: {distancia}')
            soma_distancias += distancia
# ver se o num é um fibonacci
            ultimo = 1
            penultimo = 1
            if(distancia > 2):
                termo = 3
                while(termo < distancia):
                    termo = ultimo + penultimo
                    penultimo = ultimo
                    ultimo = termo
                if(termo != distancia):
                    rodada_n_fibonacci += 1

        x_antes = x
        y_antes = y
        rodada += 1
# ver se a soma é primo
    SomaPrimo = False
    cond = 0
    for i in range(2, soma_distancias):
        if(soma_distancias % i == 0):
            cond += 1
    if(cond == 0):
        SomaPrimo = True
# ver se todos sao fibonacci
    tds_fibonacci = False
    if(rodada_n_fibonacci == 0):
        tds_fibonacci = True

# VARIAVEIS
# tds_fibonacci
# SomaPrimo
# rodada_n_fibonacci

    if(tds_fibonacci and not SomaPrimo):
        print('Yes! Eu consegui!')
    elif(tds_fibonacci and SomaPrimo):
        print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')
    elif(not tds_fibonacci and rodada_n_fibonacci == 1):
        print('Oh, não! Eu quase consegui!')
    elif(not SomaPrimo and rodada_n_fibonacci >= 2):
        print('Eu vou acabar como o Stuart :/')
    elif(SomaPrimo and rodada_n_fibonacci >= 2):
        print('Pelo menos o programa está funcionando...')
elif(0 < n_estrelas < 3):
    print('Acho que bebi demais, eu juro que tinha mais estrelas!')
elif(n_estrelas <= 0):
    print('Isso está quebrado, acho que Howard pode me ajudar.')
