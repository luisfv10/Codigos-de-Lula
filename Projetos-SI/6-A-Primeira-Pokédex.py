pokedex = dict()

while True:
    try:
        c = input().split(' ')
        comando = c[0]
        pokemon = c[1]
        if comando == 'ADD':
            if pokemon not in pokedex:
                desc = input()
                pokedex[pokemon] = desc
                print('Pokémon adicionado com sucesso')
            else:
                print('Pokémon já adicionado na Pokédex')
        elif comando == 'DESC':
            if pokemon not in pokedex:
                print('Ainda não há registro desse Pokémon')
            else:
                print(pokedex[pokemon])
    except:
        break
