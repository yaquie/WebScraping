multiplicando=0
multiplicador=0

while multiplicando <4:
    while multiplicador <3:
        producto = multiplicando* multiplicador
        print(multiplicando, " * " + str(multiplicador), " = " + str(producto))
        multiplicador +=1

    multiplicando +=1
    multiplicador = 0
