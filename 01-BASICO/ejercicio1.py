"""
Crear una clase Estudiante con los atributos Nombre, Edad y Grado.
Crear el metodo estudiar() que muestre el estudiante (nombre) esta estudiando
Crear un objeto Estudiante y usar el metodo estudiar()
Se debe interactuar con el usuario y este debe brindar los atributos
Al escribir estudiar utilizar el metodo estudiar() no case sensitive
"""


class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")


nombre_estudiante = input("Ingrese el nombre: ")
edad_estudiante = input("Ingrese la edad: ")
grado_estudiante = input("Ingrese el grado: ")

estudiante1 = Estudiante(nombre_estudiante, edad_estudiante, grado_estudiante)
print(f"""
      Datos del Estudiante: \n
      Nombre: {estudiante1.nombre} \n
      Edad: {estudiante1.edad} \n
      Grado: {estudiante1.grado} \n
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante1.estudiar()
