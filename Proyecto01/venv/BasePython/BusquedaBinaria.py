
objetivo=int(input('Escoge un numero: '))
epsilon=0.01
izquierda=0.0
derecha=max(1.0, objetivo)
respuesta=(derecha + izquierda)/2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'izquierda = {izquierda}, derecha = {derecha}, respuesta = {respuesta}')

    if respuesta**2 < objetivo:
        izquierda = respuesta
    else:
        derecha = respuesta

    respuesta =(derecha + izquierda)/2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')