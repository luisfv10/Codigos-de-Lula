# contagem de dias e casas
dias = int(input('numero de dias'))
casas = int(input('qntd de casas'))
# calculo ticks por casa
horas_construindo = (dias * 1.5)
ticks = (72000 * horas_construindo)
ticks_casas = (ticks / casas)
print(int(ticks_casas))
