class Persona:  # Clase base o padre, es la clase principal que todos los demás heredan
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola estoy hablando")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es {self.habilidad}")


# #### HERENCIA MULTIPLE ########
# La clase hija tiene a las dos clases padres en su constructor
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        # Se llama al constructor de la clase padre para poder utilizar sus atributos y mét
        Persona.__init__(self, nombre, edad, nacionalidad)
        # Se llama al método de la clase Artista para inicializar una variable específica
        Artista.__init__(self, habilidad)
        self.salario = salario  # Atributo propio de la clase EmpleadoArtista
        self.empresa = empresa  # Atributo propio de la clase EmpleadoArtista

    def presentarse(self):  # Método personalizado de la clase hija
        print(f"Me llamo {self.nombre}, tengo {self.edad} años, soy {self.nacionalidad} . Mi habilidad es {
              self.habilidad}, trabajo de {self.empresa}. Mi habilidad es {self.habilidad} y mi salario es de {self.salario}")
        # return f"{super().mostrar_habilidad()}" #  Llamada al método de la superclase para imprimir la habilidad del artista


jorge = EmpleadoArtista("Jorge", 45, "Argentino",
                        "Bailar", "Desarrollador", 1000)

jorge.presentarse()

# Comprobamos si EmpleadoArtista hereda de Artista
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)  # Devuelve True porque EmpleadoArtista hereda de Artista

# Comprobamos si jorge es una instancia de EmpleadoArtista
instancia = isinstance(jorge, EmpleadoArtista)
print(instancia)  # Devuelve True porque jorge es una instancia de EmpleadoArtista
