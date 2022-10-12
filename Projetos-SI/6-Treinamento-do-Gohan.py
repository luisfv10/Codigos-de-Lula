# recebi as duas listas
n = int(input())
p1 = input().split(' ')
p2 = input().split(' ')
for i in range(len(p1)):
  p1[i] = int(p1[i])
for i in range(len(p2)):
  p2[i] = int(p2[i])
#checar frequencia
freq1 = dict()
freq2 = dict()
for numero in p1:
  if numero not in freq1:
    freq1[numero] = 1
  else:
    freq1[numero] += 1
for numero in p2:
  if numero not in freq2:
    freq2[numero] = 1
  else:
    freq2[numero] += 1
if freq1 == freq2:
  print('Dale Gohan!')
else:
  print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')
