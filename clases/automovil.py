from vehiculo import Vehiculo

import sqlite3

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

print("SQLITE*************")
conexion=sqlite3.connect("base_datos/mi_db.db")
cursor=conexion.cursor()

cursor.execute('''CREATE  TABLE IF NOT EXISTS  automoviles (id INTEGER PRIMARY KEY AUTOINCREMENT, color TEXT, marca TEXT, aceleracion INTEGER, velocidad INTEGER)''')
conexion.commit()

cursor.execute('''INSERT INTO automoviles(color,marca,aceleracion, velocidad) VALUES (?,?,?,?)''',(auto1.color, auto1.marca, auto1.aceleracion,auto1.velocidad))
conexion.commit()

#autos=cursor.execute('''SELECT * from automoviles''')

id=16

#cursor.execute('''DELETE FROM automoviles WHERE id =?''', (id,) )
#conexion.commit()



color="VERDE"
marca="TOYOTA2"
aceleracion=100
velocidad=120
mi_id=7

cursor.execute('''UPDATE automoviles SET color=?, marca=?, aceleracion=?, velocidad=? WHERE id=?''',(color, marca, aceleracion,velocidad,mi_id))
conexion.commit()

autos=cursor.execute('''SELECT * from automoviles''')
for auto in autos:
  print(auto)
    

  










