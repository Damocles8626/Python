def area_cuadrado(lado):
    area_cu = lado * lado
    return area_cu

def area_triangulo(base, altura):
    area_t = (base * altura) / 2
    return area_t

def area_circulo(radio):
    area_ci = (radio * radio) * 3.1416
    return area_ci

print('CALCULAR AREA DE FIGURAS GEOMÉTRICAS')
print('1. Area del cuadrado')
print('2. Area del triangulo')
print('3. Area del circulo')
opcion = int(input('Escriba su opcion: '))

if opcion == 1:
    _lado = float(input('Lado del cuadrado: '))
    print('Area del cuadrado: ', area_cuadrado(_lado))

elif opcion == 2:
    _base = float(input('Base: '))
    _altura = float(input('Altura: '))
    print('Area del trinagulo: ',area_triangulo(_base, _altura))

elif opcion == 3:
    _radio = float(input('Radio: '))
    print('Area del círculo: ', area_circulo(_radio))

else:
    print('Opcion inválida...')
