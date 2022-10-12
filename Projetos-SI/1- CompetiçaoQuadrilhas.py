# entrada
nome = input()
p1 = input()
p2 = input()
p3 = input()
p4 = input()
p5 = input()
nota = float()
Casamento = False


# Uso de passo errado
if p1 != 'Cumprimento' and p1 != 'Balancê' and p1 != 'Passeio' and p1 != 'Túnel' and p1 != 'Serrote' and p1 != 'Casamento' and p1 != 'Despedida':
    print(f'Poxa, {nome}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')
    
elif p2 != 'Cumprimento' and p2 != 'Balancê' and p2 != 'Passeio' and p2 != 'Túnel' and p2 != 'Serrote' and p2 != 'Casamento' and p2 != 'Despedida':
    print(f'Poxa, {nome}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')

elif p3 != 'Cumprimento' and p3 != 'Balancê' and p3 != 'Passeio' and p3 != 'Túnel' and p3 != 'Serrote' and p3 != 'Casamento' and p3 != 'Despedida':
    print(f'Poxa, {nome}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')

elif p4 != 'Cumprimento' and p4 != 'Balancê' and p4 != 'Passeio' and p4 != 'Túnel' and p4 != 'Serrote' and p4 != 'Casamento' and p4 != 'Despedida':
    print(f'Poxa, {nome}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')

elif p5 != 'Cumprimento' and p5 != 'Balancê' and p5 != 'Passeio' and p5 != 'Túnel' and p5 != 'Serrote' and p5 != 'Casamento' and p5 != 'Despedida':
    print(f'Poxa, {nome}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')

else:
    
# passos
    if(p1 == 'Cumprimento'):
      nota+= 100
    elif(p1 == 'Balancê'):
      nota+=50
    elif(p1 == 'Passeio'):
      nota+=70
    elif(p1 == 'Túnel'):
      nota = nota * 0.9
    elif(p1 == 'Serrote'):
      nota+=100
    elif(p1 == 'Casamento'):
      Casamento = True
    elif(p1 == 'Despedida'):
      nota+=0
      
    if(p2 == 'Cumprimento'):
      nota+= 10
    elif(p2 == 'Balancê'):
      nota+=50
    elif(p2 == 'Passeio'):
      nota+=70
    elif(p2 == 'Túnel'):
      nota = nota * 0.9
    elif(p2 == 'Serrote'):
      nota+=100
    elif(p2 == 'Casamento'):
      Casamento = True
    elif(p2 == 'Despedida'):
      nota+=0
      
    if(p3 == 'Cumprimento'):
      nota+= 10
    elif(p3 == 'Balancê'):
      nota+=50
    elif(p3 == 'Passeio'):
      nota+=70
    elif(p3 == 'Túnel'):
      nota = nota * 0.9
    elif(p3 == 'Serrote'):
      nota+=100
    elif(p3 == 'Casamento'):
      Casamento = True
    elif(p3 == 'Despedida'):
      nota+=0
      
    if(p4 == 'Cumprimento'):
      nota+= 10
    elif(p4 == 'Balancê'):
      nota+=50
    elif(p4 == 'Passeio'):
      nota+=70
    elif(p4 == 'Túnel'):
      nota = nota * 0.9
    elif(p4 == 'Serrote'):
      nota+=100
    elif(p4 == 'Casamento'):
      Casamento = True
    elif(p4 == 'Despedida'):
      nota+=0
      
    if(p5 == 'Cumprimento'):
      nota+= 10
    elif(p5 == 'Balancê'):
      nota+=50
    elif(p5 == 'Passeio'):
      nota+=70
    elif(p5 == 'Túnel'):
      nota = nota * 0.9
    elif(p5 == 'Serrote'):
      nota+=100
    elif(p5 == 'Casamento'):
      Casamento = True
    elif(p5 == 'Despedida'):
      nota+=35
      
    if(Casamento == True):
      nota = nota * 2
      
    print(f'Parabéns, {nome}! Bela apresentação. A pontuação foi de {nota}!')
    
