
objetivo=int(input('Escoge un entero : '))
respuesta=0

while respuesta**2 <objetivo:
    print(respuesta)
    respuesta +=1

if respuesta**2 == objetivo:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
else:
    print(f' {objetivo} No tiene una raiz cuadrada exacta')