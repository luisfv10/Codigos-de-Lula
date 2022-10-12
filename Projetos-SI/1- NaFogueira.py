# entradas
n1 = input()
p1 = int(input())
n2 = input()
p2 = int(input())
n3 = input()
p3 = int(input())

# uma pontuaçao maior que a outra
if(p1 > p2 and p2 > p3):
    print(f'{n3} {p3} \n{n2} {p2} \n{n1} {p1}')
elif(p1 > p3 and p3 > p2):
    print(f'{n2} {p2} \n{n3} {p3} \n{n1} {p1}')
elif(p2 > p1 and p1 > p3):
    print(f'{n3} {p3} \n{n1} {p1} \n{n2} {p2}')
elif(p2 > p3 and p3 > p1):
    print(f'{n1} {p1} \n{n3} {p3} \n{n2} {p2}')
elif(p3 > p2 and p2 > p1):
    print(f'{n1} {p1} \n{n2} {p2} \n{n3} {p3}')
elif(p3 > p1 and p1 > p2):
    print(f'{n2} {p2} \n{n1} {p1} \n{n3} {p3}')
    
# todas pontuaçoes iguais
elif(p1 == p2 and p1 == p3):
    if(n1 > n2 and n2 > n3):
        print(f'{n3} {p3} \n{n2} {p2} \n{n1} {p1}')
    elif(n1 > n3 and n3 > n2):
        print(f'{n2} {p2} \n{n3} {p3} \n{n1} {p1}')
    elif(n2 > n1 and n1 > n3):
        print(f'{n3} {p3} \n{n1} {p1} \n{n2} {p2}')
    elif(n2 > n3 and n3 > n1):
        print(f'{n1} {p1} \n{n3} {p3} \n{n2} {p2}')
    elif(n3 > n2 and n2 > n1):
        print(f'{n1} {p1} \n{n2} {p2} \n{n3} {p3}')
    elif(n3 > n1 and n1 > n2):
        print(f'{n2} {p2} \n{n1} {p1} \n{n3} {p3}')
        
# p1 = p2 >< p3
elif(p1 == p2 and p2 > p3):
    if(n1 > n2):
        print(f'{n3} {p3} \n{n2} {p2} \n{n1} {p1}')
    elif(n2 > n1):
        print(f'{n3} {p3} \n{n1} {p1} \n{n2} {p2}')
elif(p1 == p2 and p2 < p3):
    if(n1 > n2):
        print(f'{n2} {p2} \n{n1} {p1} \n{n3} {p3}')
    elif(n2 > n1):
        print(f'{n1} {p1} \n{n2} {p2} \n{n3} {p3}')
        
# p1 = p3 >< p2
elif(p1 == p3 and p3 > p2):
    if(n1 > n3):
        print(f'{n2} {p2} \n{n3} {p3} \n{n1} {p1}')
    elif(n3 > n1):
        print(f'{n2} {p2} \n{n1} {p1} \n{n3} {p3}')
elif(p1 == p3 and p3 < p2):
    if(n1 > n3):
        print(f'{n3} {p3} \n{n1} {p1} \n{n2} {p2}')
    elif(n3 > n1):
        print(f'{n1} {p1} \n{n3} {p3} \n{n2} {p2}')
        
# p2 = p3 >< p1
elif(p2 == p3 and p3 > p1):
    if(n2 > n3):
        print(f'{n1} {p1} \n{n3} {p3} \n{n2} {p2}')
    elif(n3 > n2):
        print(f'{n1} {p1} \n{n2} {p2} \n{n3} {p3}')
elif(p2 == p3 and p3 < p1):
    if(n2 > n3):
        print(f'{n3} {p3} \n{n2} {p2} \n{n1} {p1}')
    elif(n3 > n2):
        print(f'{n2} {p2} \n{n3} {p3} \n{n1} {p1}')
    