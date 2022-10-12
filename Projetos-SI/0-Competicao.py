# Numeros naturais
A = int(input())
L = int(input())
P = int(input())
H = int(input())

# calculo media
M1 = int((A+L + abs(A-L)) / 2)
M2 = int((M1+P + abs(M1-P)) / 2)
M = int(M2 * H)
print(M)
