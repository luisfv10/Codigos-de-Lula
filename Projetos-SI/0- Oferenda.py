# Necessidade de Tantan
necessidade = int(input('Quantos diamantes o Tantan ta precisando?'))

if(necessidade <= 10):
    print('Arthur')
elif(10 < necessidade <= 30):
    print('Luiz')
elif(30 < necessidade <= 100):
    print('Pedro')
elif(necessidade > 100):
    print('Nenhum')
