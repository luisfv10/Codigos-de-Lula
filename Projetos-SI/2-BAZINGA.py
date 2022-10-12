# entradas
reacao = ''
piada = ''
gostou = 0
n_gostou = 0

# while
piada = input()
while(piada != 'Fim do Show!'):
  reacao = input()
  if(reacao == 'BAZINGA!'):
    gostou+=1
  else:
    n_gostou+=1
  piada = input()
  
# saida   
if(gostou > (n_gostou * 1.5)):
  print('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')
elif(n_gostou > (gostou * 1.5)):
  print('Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!')
else:
  print('Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!')
