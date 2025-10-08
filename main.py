from base_datos.conexion import Conexion
from clases.vehiculo import Vehiculo

veh1=Vehiculo(2024, "A3")

print(veh1.get_modelo())
print(veh1.get_anno())

veh1.set_anno(2025)
print(veh1.get_anno())

mi_conexion=Conexion("base_datos/mi_db.db")
mi_conexion.crear_tabla_usuarios()

mi_conexion.agregar_usuario("Pepe2","pepe2","peep2@gmail.com","admin2")


