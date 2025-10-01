#Agregar dos métodos abstractos en clases correspondientes volar() y conducir()

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def conducir(self):
        pass
    @abstractmethod
    def volar(self):
        pass

    '''Ejercicio
En el código de la clase anterior crear una carpeta que alojará una función suma() que sume dos números
-Crear otro archivo en la carpeta que que use esa función y sume y muestre por pantalla la suma
-Crear un archivo en la raíz del proyecto que llame a esa función y sume dos números
'''