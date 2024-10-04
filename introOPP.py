# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad, genero, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion

    # Método 1: Presentarse
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    # Método 2: Cambiar ocupación
    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        print(f"{self.nombre} ahora trabaja como {self.ocupacion}.")

    # Método 3: Cumplir años
    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ha cumplido {self.edad} años.")

    # Método 4: Saludar a otra persona
    def saludar(self, otra_persona):
        print(f"{self.nombre} saluda a {otra_persona.nombre}. ¡Hola, {otra_persona.nombre}!")

    # Método 5: Mostrar información
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Ocupación: {self.ocupacion}")
    # Metodo 5: pasar saludo
    def saludara(self,miri):
        print (f"hola, {self.nombre},te manda a saludar {miri.nombre}")
# Crear una instancia de la clase Persona
persona1 = Persona("Carlos", 30, "Masculino", "Ingeniero")
persona2 = Persona("victor", 10, "hombre", "docente")
persona3 = Persona("brenda", 21, "Femenino", "secretaria")

# Usar los métodos
persona1.presentarse()  # Hola, mi nombre es Carlos y tengo 30 años.
persona1.cambiar_ocupacion("Profesor")  # Carlos ahora trabaja como Profesor.
persona1.cumplir_anios()  # Carlos ha cumplido 31 años.
persona1.mostrar_informacion()  # Nombre: Carlos, Edad: 31, Género: Masculino, Ocupación: Profesor
persona1.saludar(persona2)  # Carlos saluda a Ana. ¡Hola, Ana!
persona1.saludara(persona2)

