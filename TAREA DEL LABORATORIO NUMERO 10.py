        #VETERINARIA
class Animal:
    def __init__(self, nombre, edad, peso, color, raza):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.raza=raza
        self.color=color

    def Datos_medicos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad} años')
        print(f'Peso: {self.peso} kg')
        print(f'Color: {self.raza}')
        print(f'Raza: {self.color}') 
       

    def Dosis_de_medicamento(self):
        raise NotImplementedError()

    def Ficha_medica(self):
        self.Datos_medicos()
        print(f'Dosis recomendada: {self.Dosis_de_medicamento()} mg\n')

class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza, color):
        super().__init__(nombre, edad, peso, raza, color)

    def Dosis_de_medicamento(self):
        return round(self.peso * 5, 2)  

class Gato(Animal):
    def __init__(self, nombre, edad, peso, raza, color):
        super().__init__(nombre, edad, peso, raza, color)

    def Dosis_de_medicamento(self):
        return round(self.peso * 3, 2)  

class Ave(Animal):
    def __init__(self, nombre, edad, peso, raza, color):
        super().__init__(nombre, edad, peso, raza, color)

    def Dosis_de_medicamento(self):
        return round(self.peso * 0.5, 2)

class Reptil(Animal):
    def __init__(self, nombre, edad, peso, raza, color):
        super().__init__(nombre, edad, peso, raza, color)

    def Dosis_de_medicamento(self):
        return round(self.peso * 2, 2)

perro = Perro('Solo bino', 10, 40, 'Pastor Aleman','Cafe con Negro')
gato = Gato('Estrella', 5, 100, 'Angora','Blanco')
ave = Ave('Piolin', 3, 5, 'Canario','Amarillo')
reptil=Reptil('COCO',5,300,'cocodrilo','Verde')
perro.Ficha_medica()
gato.Ficha_medica()
ave.Ficha_medica()
reptil.Ficha_medica()



        #SISTEMA PERSONAL EN UNA INSTITUCION
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def Informacion(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'DNI: {self.dni}')

class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, carrera, carnet):
        super().__init__(nombre, edad, dni)
        self.carrera = carrera
        self.carnet = carnet

    def Informacion(self):
        super().Informacion()
        print(f'Carrera: {self.carrera}')
        print(f'Carnet: {self.carnet}')

class Profesor(Persona):
    def __init__(self, nombre, edad, dni, titulo, curso):
        super().__init__(nombre, edad, dni)
        self.titulo=titulo
        self.curso=curso

    def Informacion(self):
        super().Informacion()
        print(f'Titulo: {self.titulo}')
        print(f'Curso: {self.curso}')

class Administrativo(Persona):
    def __init__(self, nombre, edad, dni, titulo, area):
        super().__init__(nombre, edad, dni)
        self.titulo=titulo
        self.area=area

    def Informacion(self):
        super().Informacion()
        print(f'Titulo: {self.titulo}')
        print(f'Area: {self.area}')

estudiantes=Estudiante('Pedro Perez', 20, '1234567', 'Ingeniería en sistemas', '3216547')
profesores=Profesor('Samuel Son', 45, '9125432', 'Ingreniero en Sistemas','Pensamiento Computacionel')
Administrativos=Administrativo('Rodrigo Lopez', 60, '1129874', 'Secretariado Bilingue','Secretaria')
estudiantes.Informacion()
profesores.Informacion()
Administrativos.Informacion()