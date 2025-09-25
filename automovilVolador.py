from automovil import Automovil

class AutomovilVolador(Automovil):
  ruedas=6
  def __init__(self, color, marca, aceleracion, velocidad,esta_volando=True):
    super().__init__(color, marca, aceleracion, velocidad)
    self.esta_volando=esta_volando
  def vuela(self):
    self.esta_volando=True
  def aterriza(self):
    self.esta_volando=False
  def datos(self):
    if self.esta_volando==False:
      return f"El automovil bolador tiene {self.ruedas} ruedas y no está volando"
    else:
      return f"El automovil bolador tiene {self.ruedas} ruedas y está volando"

autoV1=AutomovilVolador("rojo","Ferrari", 100,120,True)
print(autoV1.datos())