head
from datetime import datetime
ahora= datetime.now()
current_time= ahora.hour
current_minute= ahora.minute

delta_alarma=int(input("Dentro de cuantas horas horas quieres que suene la alarma?"))
alarm_day= delta_alarma // 24
alarm_hrs= (ahora.hour + delta_alarma) % 24
print("La hora que me suena la alarma sera {0:02d}:{1:02d} dentro de {2:d} dias".format(alarm_hrs,current_minute,alarm_day))
