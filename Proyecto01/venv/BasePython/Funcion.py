
def nombre_completo(nombre, apellido, inverso = false):
    if inverso:
        return  f'{apellido} {nombre}'
    else:
        return  f'{nombre} {apellido}'

nombre_completo(jakie, alarcon, inverso = true)
