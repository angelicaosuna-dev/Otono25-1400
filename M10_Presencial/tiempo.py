#TODO 1 y 3
class tiempo:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self._normalize()
   
    def __str__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
   
    def _normalize(self):
        self.minutos += self.segundos // 60
        self.segundos %= 60
        self.horas += self.minutos // 60
        self.minutos %= 60
        self.horas %= 24
   
    def incrementar(self, horas, minutos, segundos):
        self.segundos += segundos
        self.minutos += minutos
        self.horas += horas
        self._normalize()
        return self
    
#TODO 2.
#convirtiendo el tiempo original a los segundos.
#convertir el total de segundos a un objeto tiempo
def sumar_tiempo(tiempo, hora, minuto, segundo):
    total_segundos = tiempo_a_int(tiempo) + hora * 3600 + minuto * 60 + segundo
    return int_a_tiempo(total_segundos)
    
def tiempo_a_int(tiempo):
    return tiempo.horas * 3600 + tiempo.minutos * 60 + tiempo.segundos
    
def int_a_tiempo(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    return tiempo(horas, minutos, segundos)
    
mi_hora = tiempo(14, 30, 15)
print("hora inicial:", mi_hora)
#TODO 3. 
nueva_hora = sumar_tiempo(mi_hora, 2, 45, 50)
print("nueva hora:", nueva_hora)
hora_incrementada = mi_hora.incrementar(2, 45, 50)
print("hora incrementada:", hora_incrementada)
mi_hora.incrementar(1, 20, 30)
print("hora despues del overflow", mi_hora)