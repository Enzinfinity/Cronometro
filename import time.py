import time
import keyboard

print("Cronometro iniciado, se quiser parar aperte Enter ")
  
segundos= 0



while True:

 time.sleep(1)
 segundos+= 1
 minutos= segundos // 60
 horas= minutos // 60
 print(f"{horas:02}:{minutos % 60:02}:{segundos % 60:02}", end="\r")

 if keyboard.is_pressed ("Enter"):
   print("\nCronômetro parado!")
   break