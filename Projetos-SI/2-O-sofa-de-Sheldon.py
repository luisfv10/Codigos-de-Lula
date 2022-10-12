# dados iniciais
temp = 30 # perfeito é menor que 25
fome = 0 # se fome 1 o cara ta sem fome e se 0 ta na larica
internet = 0 # perfeito é acima de 100

# açoes
acao = input()
while(acao != 'parar'):
  if(acao == 'ir para o grad'):
    temp-=5
    internet+=300
  elif(acao == 'sair para a rua'):
    temp+=5
  elif(acao == 'comer uma quentinha'):
    fome+=1
  elif(acao == 'conectar no wifi'):
    internet+=100
  else:
    print('Entrada inválida')
  acao = input()

# print
if(temp>=30):
  print('A temperatura aqui não está agradável')
elif(temp<=25):
  print('Agora sim, está aconchegante')
if(fome==0):
  print('Meu corpo precisa de comida')
if(internet<100):
  print('Essa conexão está horrível')
if(fome==1 and temp<=25 and internet>=300):
  print('Finalmente um lugar preciso para mim!')
