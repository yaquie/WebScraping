
objetivo=int(input('Escoge un numero: '))
epsilon=0.1
paso=epsilon**2
respuesta=0.0

while abs(respuesta**2-objetivo) >= epsilon and respuesta <= objetivo:
    #print(abs(respuesta**2-objetivo), respuesta)
    respuesta +=paso

if abs(respuesta**2-objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')


