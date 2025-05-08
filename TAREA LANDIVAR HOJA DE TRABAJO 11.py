import math
    # TIEMPO
class Realizar_experimento:
    def __init__(self):
        self.altura = int(input('Ingrese la altura '))
        self.gravedad = int(input('Ingrese la gravedad '))
    def tiempo(self):
        try:
            if self.altura < 0 or self.gravedad < 0:
                raise ValueError('')
            else:
                self.tiempo = math.sqrt((2 * self.altura) / self.gravedad)
                return self.tiempo 
        except ValueError:
            print('la altura no debe ser negativa y la gravedad no debe ser cero')
resultado=Realizar_experimento()
print('El tiempo es: ',resultado.tiempo())

    # CALCULADORA
class Calculadora:
    def __init__(self):
        try:
            self.numero = float(input('Ingrese un número: '))
            opcion = int(input('Elija una opción:\n1. Factorial\n2. Raíz\n3. Potencia\n4. Logaritmo\nOpción: '))

            if opcion == 1:
                resultado = Factorial(self.numero).calcular()
                print('El factorial es:', resultado)
            elif opcion == 2:
                resultado = Raiz(self.numero).calcular()
                print('La raíz es:', resultado)
            elif opcion == 3:
                resultado = Potencia(self.numero).calcular()
                print('La potencia es:', resultado)
            elif opcion == 4:
                resultado = Logaritmo(self.numero).calcular()
                print('El logaritmo es:', resultado)
            else:
                raise ValueError('Opción no válida.')
        except ValueError as e:
            print('Error:', e)

class Factorial:
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero < 0 or not self.numero.is_integer():
            raise ValueError('El factorial solo se puede calcular para enteros no negativos.')
        resultado = 1
        for i in range(1, int(self.numero) + 1):
            resultado *= i
        return resultado

class Raiz:
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero < 0:
            raise ValueError('No se puede calcular la raíz de un número negativo.')
        return math.sqrt(self.numero)

class Potencia:
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        return math.pow(self.numero, 2)

class Logaritmo:
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero <= 0:
            raise ValueError('El logaritmo solo está definido para números positivos.')
        return math.log10(self.numero)
Calculadora()

