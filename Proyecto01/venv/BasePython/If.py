
nombre1=input('Ingrese su nombre: ')
edad1=int(input('Ingrese su edad: '))

nombre2=input('Ingrese su nombre: ')
edad2=int(input('Ingrese su edad: '))

#comparar edades

if edad1 > edad2:
    print(nombre1 + ' Es mayor que: ' + nombre2)
    print('Edad de ' + nombre1 + ' es: ' + str(edad1))
elif edad1 < edad2:
    print(nombre2 + 'Es menor que: ' + nombre1)
    print('Edad de ' + nombre2 + ' es: ' + str(edad2))
else:
    print(nombre2 + ' Tiene la misma edad que: ' + nombre1)
