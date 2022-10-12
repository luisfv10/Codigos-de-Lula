# entrada
c1 = input()
n1 = float(input()) 
d1 = float(input())
c2 = input()
n2 = float(input())
d2 = float(input())
c3 = input()
n3 = float(input())
d3 = float(input())

# notas
if(n1 < 4 and n2 < 4 and n3 < 4):
    print('Nota mínima não atingida')
else:
  if(n1 > n2 and n1 > n3):
    print(c1)
  elif(n2 > n1 and n2 > n3):
    print(c2)
  elif(n3 > n1 and n3 > n2):
    print(c3)
  
  # empate
  if(n1==n2 and n1>n3):
      if(d1>d2):
          print(c2)
      elif(d2>d1):
          print(c1)
  
  elif(n1==n3 and n1>n2):
      if(d1>d3):
          print(c3)
      elif(d3>d1):
          print(c1)
  
  elif(n2==n3 and n2>n1):
      if(d2>d3):
          print(c3)
      elif(d3>d2):
          print(c2)
          
  elif(n1==n2==n3):
      if(d1<d2) and (d1<d3):
          print(c1)
      elif(d2<d1) and (d2<d3):
          print(c2)
      elif(d3<d1) and (d3<d2):
          print(c3)
