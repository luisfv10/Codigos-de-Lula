adversario = input()
vida_viloes = {'Vingador': 30, 'Tiamat': 20, 'Vingador das Sombras': 14}
if adversario not in vida_viloes:
    vida_viloes[adversario] = 9
dano_herois = {'Bobby': 8, 'Diana': 12, 'Eric': 8, 'Hank': 6, 'Presto': 4,
               'Sheila': 6, 'Uni': 2, 'Mestre dos Magos': vida_viloes[adversario]}
rodadas_perder = int(input())
rodadas = 0
while rodadas_perder > rodadas:
    try:
        lutador = input()
        vida_viloes[adversario] -= dano_herois[lutador]
        if vida_viloes[adversario] <= 0:
            if lutador == 'Mestre dos Magos':
                print('Muito obrigado amigo, que nos vejamos novamente um dia')
            else:
                print(
                    f'{lutador} executou o ultimo golpe em {adversario}, estamos livres!')
        rodadas += 1
    except:
        break
