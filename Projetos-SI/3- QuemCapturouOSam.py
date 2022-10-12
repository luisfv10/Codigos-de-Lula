# comandos
comando = ''
remover_ultimo = 'O último da lista está limpo'
remover_primeiro = 'Não encontrei nada no primeiro suspeito'
remover_centro = 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita'
remover_posicao = 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:'
add_suspeito = 'Acho que temos mais uma opção a ser analisada…'

comando_nao_listado = 'Isso não estava no combinado, a lista vai permanecer do mesmo jeito'

suspeitos_string = input()
suspeitos = suspeitos_string.split(',')
comando_listado = False
# While
cond_while = True
while cond_while:
    comando = input()
    if comando == remover_ultimo:
        suspeitos.pop(-1)

    elif comando == remover_primeiro:
        suspeitos.pop(0)

    elif comando == remover_centro:
        if len(suspeitos) % 2 == 0:
            par = int(len(suspeitos) / 2)
            suspeitos.pop(par)
        elif len(suspeitos) % 2 == 1:
            impar = int((len(suspeitos) - 1) / 2)
            suspeitos.pop(impar)

    elif comando == remover_posicao:
        posicao = int(input())
        suspeitos.pop(posicao)

    elif comando == add_suspeito:
        novo_suspeito = input()
        suspeitos.append(novo_suspeito)
    else:
        print(comando_nao_listado)

    qntd_suspeitos = len(suspeitos)
    if qntd_suspeitos == 1:
        cond_while = False
        print( f'Acho que encontramos o suspeito. O seu nome é {suspeitos[0]}, vamos salvar o Sam!')
