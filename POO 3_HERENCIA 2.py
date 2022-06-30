class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia
    def descripcion(self):
        print('Nombre: ', self.nombre, ' Edad: ', self.edad, ' Residencia: ',self.residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) # Super llama al método de la clase Padre

        self.salario = salario
        self.antiguedad = antiguedad
    def descripcion(self):
        super().descripcion() # Va a ese método de la clase Padre y lo ejecuta
        print('Salario: ', self.salario, ' Antiguedad: ', self.antiguedad)

Antonio = Persona('Antonio', 55, 'México')
Antonio.descripcion()

Manuel = Empleado(2000, 19, 'Manuel', '42', 'México')
Manuel.descripcion()

# Principio de sustitución: una clase hija siempre será como la clase Padre, pero no al revés
# un objeto 'Empleado' es siempre perteneciente a la clase Persona también

print(isinstance(Antonio, Empleado)) # Devuelve True si el objeto pertenece a la clase mencionada
print(isinstance(Antonio, Persona)) # Antonio es Persona (True), pero no Empleado (False)

print(isinstance(Manuel, Empleado)) # Manuel sí es Empleado (True)
print(isinstance(Manuel, Persona)) # también es forzosamente Persona (True)