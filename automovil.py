from vehiculo import Vehiculo

class Automovil(Vehiculo):
  ruedas=4
  def __init__(self,color,marca,aceleracion, velocidad):
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=velocidad
  def acelera(self):
    self.velocidad=self.aceleracion+self.velocidad
  def frena(self):
    self.velocidad=self.velocidad-self.aceleracion

  def conducir(self):
    return "Está siendo conducido"
  def volar(self):
    return "EL automovil no puede volar"


auto1=Automovil("Azul", "Toyota",10,10)
print(f'El auto es de color {auto1.color}')
print(f'El auto tiene una aceleración de  {auto1.aceleracion}')
print("***************")
auto1.aceleracion=20
print(f'El auto tiene una aceleración de  {auto1.aceleracion}')

print(f'El auto tiene una velocidad de  {auto1.velocidad}')

auto1.acelera()
print(f'El auto tiene una velocidad de  {auto1.velocidad}')
print("**********")

auto2=Automovil("amarillo", "Audi",50,100)
print(f"La velocidad es de {auto2.velocidad}")
auto2.frena()

print(f"La velocidad es de {auto2.velocidad}")

print("Abstracción +++++++++++++++")
print(auto1.conducir())


    

  










