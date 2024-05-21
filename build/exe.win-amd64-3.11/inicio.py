import time
import datetime
from multiprocessing import Pool
#import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
#import bisect
import ctypes
import sys



from obtener_rango_ip import obtener_direcciones_de_red
from prueba_mac import obtener_mac
from dividir_lista import dividir_lista
#from Final import ini_web
from t20p import ini_web


def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        # Si el usuario ya tiene privilegios de administrador, ejecutar el código principal
        print("Ya tienes privilegios de administrador.")
        return True
    else:
        # Si el usuario no tiene privilegios de administrador, solicitarlos
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            return True
        except Exception as e:
            print("Error al solicitar permisos de administrador:", e)
            return False

red = sys.argv[1]
mask = sys.argv[2]

#red = input("Ingrese red: ")
#mask = input("Ingrese Mascara /")
rango_de_red = red+"/"+mask
inicio = time.time()                                                # Obtener el tiempo de inicio


if __name__ == '__main__':

    rango = obtener_direcciones_de_red(rango_de_red)

    if run_as_admin():
        print("Código con permisos de administrador.")
    else:
        print("No se pudieron obtener los permisos")


    largo = (len(rango))
    largo1 = (largo/4)
    largo1 = int(largo1)
    largo2 = (largo1)+(largo1)
    largo3 = (largo2)+(largo1)
    largo4 = (largo3)+(largo1)

    #print(rango)
    lista1 = (rango[0:largo1])
    lista2 = (rango[largo1:largo2])
    lista3 = (rango[largo2:largo3])
    lista4 = (rango[largo3:largo4])

    
    executor = ThreadPoolExecutor(max_workers=20)
    future_yealink1 = executor.submit(obtener_mac, lista1)
    future_yealink2 = executor.submit(obtener_mac, lista2)
    future_yealink3 = executor.submit(obtener_mac, lista3)
    future_yealink4 = executor.submit(obtener_mac, lista4)

   
    yealink1 = future_yealink1.result()  # obtener mac de la lista 1
    yealink2 = future_yealink2.result()  # obtener mac de la lista 2
    yealink3 = future_yealink3.result()  # obtener mac de la lista 3
    yealink4 = future_yealink4.result()  # obtener mac de la lista 4


    lista_yealink = []
    for lista_yealink1 in [yealink1, yealink2, yealink3, yealink4]:
        lista_yealink.extend(lista_yealink1)

    sublistas = dividir_lista(lista_yealink)
    sublistas_almacenadas = []
    for i, sublista in enumerate(sublistas):
        sublistas_almacenadas.append(sublista)
        p=(f"Sublista {i + 1}: {sublista}") 

    executor = ThreadPoolExecutor(max_workers=10)
    for i in sublistas[0]:
        print(i)
        executor.submit(ini_web, i)
    for i in sublistas[1]:
        print(i)
        executor.submit(ini_web, i)
    for i in sublistas[2]:
        executor.submit(ini_web, i)
    for i in sublistas[3]:
        executor.submit(ini_web, i)
    for i in sublistas[4]:
        executor.submit(ini_web, i)
    for i in sublistas[5]:
        executor.submit(ini_web, i)
    for i in sublistas[6]:
        executor.submit(ini_web, i)
    for i in sublistas[7]:
        executor.submit(ini_web, i)
    for i in sublistas[8]:
        executor.submit(ini_web, i)
    for i in sublistas[9]:
        executor.submit(ini_web, i)
    for i in sublistas[10]:
        executor.submit(ini_web, i)




tiempo_transcurrido = time.time() - inicio                          # Finaliza el cronometro
delta_tiempo = datetime.timedelta(seconds=tiempo_transcurrido)      # Convertir el tiempo transcurrido a un objeto timedelta
# Obtener la parte de horas, minutos y segundos
horas = delta_tiempo.seconds // 3600
minutos = (delta_tiempo.seconds % 3600) // 60
segundos = delta_tiempo.seconds % 60
print(f"Tiempo transcurrido: {horas:02}:{minutos:02}:{segundos:02}")

