nome = input()
n_filmes = int(input())

lista_filmes = []
filme = ''
rodada = 0
while rodada < n_filmes:
    filme = input().split(' - ')
    lista_filmes.append(filme)
    rodada += 1 
# lista_filmes 1 caso = [['Psicose', '4.6'], ['Invocação do Mal 2', '3.6'], ['Constantine', '4.4'], ['Invasão Zumbi', '3.7'], ['Um Lugar Silencioso', '4.3']]
for n_lista in range(len(lista_filmes) - 1, 0 , -1):
    #comeca do final, para no zero e da step em -1
    for i in range(n_lista):
        if lista_filmes[i][1] > lista_filmes[i + 1][1]:
            inverter = lista_filmes[i]
            lista_filmes[i] = lista_filmes[i + 1]
            lista_filmes[i + 1] = inverter

lista_filmes.reverse()

print(f'Os filmes sugeridos por {nome} são:')
for i in range(len(lista_filmes)):
    print(f'{lista_filmes[i][0]} - {lista_filmes[i][1]}')