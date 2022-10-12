# lagarto envenena spock
# spock quebra tesoura
# tesoura decapita lagarto
# se os dois participantes escolhem o mesmo elemento, ninguém ganha
# spock = pedra
# lagarto = papel
pontos = 0
n = int(input())
for i in range(0, n):
  sheldon = input()
  raj = input()
  

# jogo de cria
  if(sheldon == 'lagarto' and raj == 'spock'):
    pontos+= 1
  elif(sheldon == 'lagarto' and raj == 'tesoura'):
    pontos-= 1
  elif(sheldon == 'lagarto' and raj == 'lagarto'):
    pontos+= 0
  elif(sheldon == 'spock' and raj == 'lagarto'):
    pontos-= 1
  elif(sheldon == 'spock' and raj == 'tesoura'):
    pontos+= 1
  elif(sheldon == 'spock' and raj == 'spock'):
    pontos+= 0
  elif(sheldon == 'tesoura' and raj == 'spock'):
    pontos-= 1
  elif(sheldon == 'tesoura' and raj == 'lagarto'):
    pontos+= 1
  elif(sheldon == 'tesoura' and raj == 'tesoura'):
    pontos+= 0
    
  # resultados
if(pontos>0):
  print('BAZINGA! EU SOU O SENHOR DA SALA!')
elif(pontos<0):
  print('ENGOLE ESSA, SHELDON!')
elif(pontos == 0):
  print('Oh não, precisamos de outra rodada.')

