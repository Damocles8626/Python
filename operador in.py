print('Oferta de Materias Optativas para Informática')

oferta = ('Sistemas Embebidos', 'Circuitos Eléctricos', 'Inteligencia Artificial')
print(oferta)

materia = input('Elija una materia optativa: ')
materia = materia.title()

if materia in oferta:
    print('Se eligió correctamente: ' + materia)
else:
    print('Entrada inválida')