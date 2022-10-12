def analises(sentenca, c, p_esquerda, p_direita):
    if c == len(sentenca):
        if p_esquerda == p_direita:
            return 'Essa sentença está com os parênteses balanceados, HOORAY!'
        elif p_esquerda > p_direita:
            return 'A quantidade de parênteses \'(\' está maior que a de \')\', vamos descartá-la'
        elif p_direita > p_esquerda:
            return 'A quantidade de parênteses \')\' está maior que a de \'(\', vamos descartá-la'
    else:
        if c != len(sentenca) and sentenca[c] == '(':
            return analises(sentenca, c + 1, p_esquerda + 1, p_direita)  
        elif c != len(sentenca) and sentenca[c] == ')':
            return analises(sentenca, c + 1, p_esquerda, p_direita + 1)
        else:
            return analises(sentenca, c + 1, p_esquerda, p_direita) 
      
n = int(input())
rodada = 0
while n > rodada:
    s = input()
    p_direita = 0
    p_esquerda = 0
    x = analises(s, 0, 0, 0)
    print(x)
    rodada += 1
