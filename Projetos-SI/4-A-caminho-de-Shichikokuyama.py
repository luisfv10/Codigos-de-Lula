# shichikokuyama.
# 'shi' 'chi' 'ko' 'ku' 'ya' 'ma'
# nenhuma silaba : “Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.”
# uma silaba : “Lembrei! A sílaba {silaba} está no nome do hospital. Obrigada, Totoro!”
# duas ou mais : “Lembrei! As sílabas: {silaba1}, {silaba2}, {silabaN} estão no nome do hospital. Obrigada, Totoro!”
# palavra certa : “A palavra {palavra} está toda no nome do hospital. Acertou em cheio, Totoro!”
# OBS2: Se tiver uma palavra que contenha sílabas que já foram identificadas, ignore essa sílaba e a considere como uma sílaba que não faz parte da palavra.
# print final: “Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!”

# criar funcao de um separador de silabas
# criar funcao de checar se as silabas tao em ordem
# checar silabas achadas
# printar saidas dependendo do numero de silabas achadas
# printar saida final quando codigo tiver todas as silabas

hospital = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']

# CRIAR FUNCOES
def sep_silabas(texto):
    vogais = set('aeiou') # cada silaba tem uma vogal
    comecar = 0
    resposta = []
    for indice in range(len(texto)):
        if texto[indice] in vogais:
            resposta.append(texto[comecar:indice + 1])
            comecar = indice + 1
    return resposta

def comparador(a, b):
    return a == b

def na_ordem(n_silabas):
    na_ordem = False
    ult_indice = 0
    indice_atual = 0
    rodada = 0
    while rodada < len(n_silabas):
        if rodada == 0:
            ult_indice = hospital.index(n_silabas[rodada])
        else:
            indice_atual = hospital.index(n_silabas[rodada])
            na_ordem = comparador(ult_indice, indice_atual - 1)
            ult_indice = indice_atual
        rodada += 1
    return na_ordem

# FUNCOES COMPLETAS
# CHECAR SILABAS ACHADAS
hospital = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']
silaba_achada = [] 
cond_while = True
while cond_while:
    silaba_input = input() 
    silabas = sep_silabas(silaba_input) # separou
    tem_hospital = []
    for silaba in silabas: # cada silaba
        if silaba in hospital: # se silaba em hospital
            indice_nome = hospital.index(silaba) # acha onde
            if indice_nome not in silaba_achada: 
                silaba_achada.append(indice_nome) # add silaba ja achada
                tem_hospital.append(silaba) # add no tem_hospital a silaba mandada
# prints iniciais  
    if len(tem_hospital) == 1:
        print(f'Lembrei! A sílaba {tem_hospital[0]} está no nome do hospital. Obrigada, Totoro!')
    elif len(tem_hospital) > 1:
        em_ordem = na_ordem(tem_hospital)
        t = ''
        if em_ordem and t.join(tem_hospital) == silaba_input:
            print(f'A palavra {t.join(tem_hospital)} está toda no nome do hospital. Acertou em cheio, Totoro!')
        else:
            separador = ', '
            print(f'Lembrei! As sílabas: {separador.join(tem_hospital)} estão no nome do hospital. Obrigada, Totoro!')

    else:
        print('Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')
# print final
    silaba_achada.sort()
    if silaba_achada == [0, 1, 2, 3, 4, 5]:
        cond_while = False
        print('Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')
