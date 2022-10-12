# Coordenadas do Ponto Flutuante
x = int(input(''))
z = int(input(''))
# Distancia para Hogsmeade:
h = (x - 34) ** 2 + (z - 220) ** 2
distancia_h = h ** 0.5
print(f'Distancia para Hogsmeade: {distancia_h:.2f}')
# Distancia para kakariko:
k = (x - 0) ** 2 + (z - 0) ** 2
distancia_k = k ** 0.5
print(f'Distancia para Kakariko: {distancia_k:.2f}')
# Distancia para Solitude:
s = (x - 140) ** 2 + (z - 456) ** 2
distancia_s = s ** 0.5
print(f'Distancia para Solitude: {distancia_s:.2f}')