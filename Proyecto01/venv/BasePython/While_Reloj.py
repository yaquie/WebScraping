
hora =0
minuto =0
segundo =0

while hora <= 1:
    while minuto <=5:
        while segundo <=4:
            print(hora, " hh: "+ str(minuto), " mm: "+ str(segundo) + " ss")
            segundo +=1

        minuto +=1
        segundo =0

    hora += 1
    minuto = 0
    segundo = 0