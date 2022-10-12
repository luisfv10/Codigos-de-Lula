# Etapas
e1 = 'Começou a Trabalhar na Caltech'
e2 = 'Trabalho sobre a String Theory'
e3 = 'Ganhar o Chancellor de ciência'
e4 = 'Pensar na Teoria de Cooper-Hofstader'
e5 = 'Criou a Super Assimetria'
e6 = 'Ganhar o Nobel'

e1_ok = False
e2_ok = False
e3_ok = False
e4_ok = False
e5_ok = False
e6_ok = False

# x = xingamentos
x1 = 'Tinha que ser o engenheiro sem Phd do Wolowitz'
x2 = 'Leonard seu anão covarde'
x3 = 'Tu é muito burro Raj'

# desitiu
desistiu = 'É o fim da Estrada pra Sheldon Cooper'

ult_entrada = ''

# while
cond_while = True
while(cond_while):
    entrada = input()
    
    eAvanco = entrada == e1 or entrada == e2 or entrada == e3 or entrada == e4 or entrada == e5 or entrada == e6
    foiAvanco = ult_entrada == e1 or ult_entrada == e2 or ult_entrada == e3 or ult_entrada == e4 or ult_entrada == e5 or ult_entrada == e6
    
# dizendo a ultima etapa
    ult1 = e1_ok and not e2_ok
    ult2 = e2_ok and not e3_ok
    ult3 = e3_ok and not e4_ok
    ult4 = e4_ok and not e5_ok
    ult5 = e5_ok and not e6_ok
    ult6 = e6_ok 
    
# se ele ganhar
    if(eAvanco):
        if(entrada == e1):
            if(not e1_ok):
                e1_ok = True
        elif(entrada == e2):
            if(e1_ok and not e2_ok):
                e2_ok = True
        elif(entrada == e3):
            if(e1_ok and e2_ok and not e3_ok):
                e3_ok = True
        elif(entrada == e4):
            if(e1_ok and e2_ok and e3_ok and not e4_ok):
                e4_ok = True
        elif(entrada == e5):
            if(e1_ok and e2_ok and e3_ok and e4_ok and not e5_ok):
                e5_ok = True
        elif(entrada == e6):
            if(e1_ok and e2_ok and e3_ok and e4_ok and e5_ok and not e6_ok):
                e6_ok = True
                print('Você conseguiu Sheldon, o Nobel é seu!!!')
                cond_while = False
# se a entrada for bazinga eliminar a entrada               
    elif(entrada == 'Bazinga'):
        if(foiAvanco):
            if(ult_entrada == e1):
                e1_ok = False
            elif(ult_entrada == e2):
                e2_ok = False
            elif(ult_entrada == e3):
                e3_ok = False
            elif(ult_entrada == e4):
                e4_ok = False
            elif(ult_entrada == e5):
                e5_ok = False
            elif(ult_entrada == e6):
                e6_ok = False
# se xingar
    elif(entrada == x1 or entrada == x2 or entrada == x3):
        print('Não xingue seus amigos Sheldon!')
#se desistir
    elif(entrada == desistiu):
        if(ult1 or ult2):
            print('Tão perto, mas tão longe')
        elif(ult3 or ult4):
            print('Não desista Sheldon, você ainda têm muito para alcançar!')
        elif(ult5):
            print('Nãoooooo, esse momento ia ser seu Sheldon')
        else:
            print('Que potencial desperdiçado...')
        cond_while = False
    ult_entrada = entrada
            
            
