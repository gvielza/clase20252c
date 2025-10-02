import sqlite3
from clases.vehiculo import Vehiculo

veh1=Vehiculo(2024, "A3")

print(veh1.get_modelo())
print(veh1.get_anno())

veh1.set_anno(2025)
print(veh1.get_anno())




