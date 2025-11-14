<<<<<<< HEAD
#TODO 1 y 3
class tiempo:
=======
#TODO #1 y #3
class Tiempo:
>>>>>>> 9598e239894168af3ecca2350313d2a4a102dfc1
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self._normalize()
<<<<<<< HEAD
   
    def __str__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
   
=======

    def __str__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
    
>>>>>>> 9598e239894168af3ecca2350313d2a4a102dfc1
    def _normalize(self):
        self.minutos += self.segundos // 60
        self.segundos %= 60
        self.horas += self.minutos // 60
        self.minutos %= 60
        self.horas %= 24
<<<<<<< HEAD
   
    def incrementar(self, horas, minutos, segundos):
=======

    # ahora ajusta el tiempo si excede
    def incrementar_tiempo(self, horas, minutos, segundos):
>>>>>>> 9598e239894168af3ecca2350313d2a4a102dfc1
        self.segundos += segundos
        self.minutos += minutos
        self.horas += horas
        self._normalize()
        return self
<<<<<<< HEAD
    
#TODO 2.
#convirtiendo el tiempo original a los segundos.
#convertir el total de segundos a un objeto tiempo
def sumar_tiempo(tiempo, hora, minuto, segundo):
    total_segundos = tiempo_a_int(tiempo) + hora * 3600 + minuto * 60 + segundo
    return int_a_tiempo(total_segundos)
=======


#TODO #2 
#convirtiendo tiempo original a los segundos
#convertir el total de segundos a un objeto Tiempo
>>>>>>> 9598e239894168af3ecca2350313d2a4a102dfc1
    
def tiempo_a_int(tiempo):
    return tiempo.horas * 3600 + tiempo.minutos * 60 + tiempo.segundos
    
def int_a_tiempo(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
<<<<<<< HEAD
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
=======
    return Tiempo(horas, minutos, segundos)
    
def sumar_tiempo(tiempo, horas, minutos, segundos):
    total_segundos = tiempo_a_int(tiempo) + horas * 3600 + minutos * 60 + segundos
    return int_a_tiempo(total_segundos)


mi_hora = Tiempo(14, 30, 15)
print("Hora inicial:", mi_hora)


#TODO #3
nueva_hora = sumar_tiempo(mi_hora, 2, 50, 30)
print("Nueva Hora:", nueva_hora)

mi_hora.incrementar_tiempo(1, 45, 30)
print("Hora incrementada:", mi_hora)

tiempo_desbordado = sumar_tiempo(mi_hora, 0, 120, 3600)
print("Hora después del overflow:", tiempo_desbordado)
>>>>>>> 9598e239894168af3ecca2350313d2a4a102dfc1
