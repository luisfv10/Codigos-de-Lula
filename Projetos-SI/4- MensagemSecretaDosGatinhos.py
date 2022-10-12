# criar dois codigos pra primeiro letras minusculas
# depois letras maiusculas e depois um pro 100 pra dar espaço
# se input maior que 100  print('Infelizmente os números nao dizem nada')
# 0 a 49 chr(97 a 122)
# 50 a 99 chr(65 a 90)
# 100 (' ')
# criar um def pra usar os codigos de cima

# input = 64 100 17 4 8 13 14 100 3 14 18 100 56 0 19 14 18 100 14 5 4 17 4 2 4 100 15 4 19 8 18 2 14 18
lista_print = []


def letras():
    if n > 100:
        print('Infelizmente os números nao dizem nada')
        exit()
    else:
        if n <= 25:
            a = chr(n + 97)
            lista_print.append(a)
        elif n > 25 and n <= 49:
            a = chr(n + 71)
            lista_print.append(a)
        elif n > 49 and n <= 75:
            a = chr(n + 15)
            lista_print.append(a)
        elif n > 75 and n <= 99:
            a = chr(n - 11)
            lista_print.append(a)
        elif n == 100:
            a = str(' ')
            lista_print.append(a)


numeros = input().split(' ')
for i in numeros:
    n = int(i)
    letras()
for i in lista_print:
    print(i, end='')
