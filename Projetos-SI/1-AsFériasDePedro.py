# entrada
# 17 18 19 21 22 23 24 25 26
x = int(input())

if(x == 17 or x == 19 or x ==21 or x == 23 or x == 25):
  print('Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!')
elif(x == 18 or x == 22 or x == 24 or x == 26):
  print('Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!')
elif(x == 20):
  print('Você escolheu um dia que não irá acontecer nenhum show, tente novamente!')
else: print('Você escolheu um dia que não irá acontecer nenhum show, tente novamente!')
