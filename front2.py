import tkinter as tk
from itertools import cycle
import subprocess
import threading
import time

def ejecutar_aplicacion():
    # Obtener los valores de la red y la máscara desde los campos de entrada
    red = entry_red.get()
    mask = entry_mask.get()

    # Deshabilitar el botón de ejecución mientras se ejecuta la aplicación
    boton_ejecutar.config(state=tk.DISABLED)

    # Limpiar el campo de texto de la lista final y el tiempo transcurrido
    lista_text.config(state=tk.NORMAL)
    lista_text.delete("1.0", tk.END)
    lista_text.config(state=tk.DISABLED)
    tiempo_label.config(text="")

    # Limpiar los campos de entrada
    entry_red.delete(0, tk.END)
    entry_mask.delete(0, tk.END)

    # Restablecer la etiqueta de asterisco a su estado original
    asterisco_label.config(text="")

    # Establecer el tiempo de inicio al momento de la ejecución
    global inicio
    inicio = time.time()

    # Iniciar el hilo para ejecutar la aplicación principal
    threading.Thread(target=ejecutar_aplicacion_principal, args=(red, mask)).start()

def ejecutar_aplicacion_principal(red, mask):
    # Ejecutar la aplicación principal con los valores ingresados
    proceso = subprocess.Popen(["python", "inicio.py", red, mask], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Animación del asterisco giratorio mientras la aplicación está en ejecución
    for frame in cycle(r"-/|\\"):
        if proceso.poll() is not None:  # La aplicación ha terminado
            break
        asterisco_label.config(text=frame)
        time.sleep(0.1)
    
    # Mostrar el contenido de la lista final y el tiempo transcurrido
    output, _ = proceso.communicate()
    lista_text.config(state=tk.NORMAL)
    lista_text.delete("1.0", tk.END)
    lista_text.insert(tk.END, output)
    lista_text.config(state=tk.DISABLED)

    tiempo_transcurrido = time.time() - inicio
    horas = int(tiempo_transcurrido // 3600)
    minutos = int((tiempo_transcurrido % 3600) // 60)
    segundos = int(tiempo_transcurrido % 60)
    tiempo_label.config(text=f"Tiempo transcurrido: {horas:02}:{minutos:02}:{segundos:02}")

    # Habilitar nuevamente el botón de ejecución
    boton_ejecutar.config(state=tk.NORMAL)

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación de Redes")

# Crear etiquetas y campos de entrada para la red y la máscara
label_red = tk.Label(root, text="Ingrese la red:")
label_red.grid(row=0, column=0, padx=10, pady=5)
entry_red = tk.Entry(root)
entry_red.grid(row=0, column=1, padx=10, pady=5)

label_mask = tk.Label(root, text="Ingrese la máscara:")
label_mask.grid(row=1, column=0, padx=10, pady=5)
entry_mask = tk.Entry(root)
entry_mask.grid(row=1, column=1, padx=10, pady=5)

# Crear el botón para ejecutar la aplicación principal
boton_ejecutar = tk.Button(root, text="Ejecutar Aplicación", command=ejecutar_aplicacion)
boton_ejecutar.grid(row=2, columnspan=2, padx=10, pady=10)

# Crear el campo de texto para mostrar la lista final
lista_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
lista_text.grid(row=3, columnspan=2, padx=10, pady=10)

# Crear una etiqueta para mostrar el asterisco giratorio
asterisco_label = tk.Label(root, text="", font=("Courier", 12))
asterisco_label.grid(row=4, columnspan=2)

# Crear una etiqueta para mostrar el tiempo transcurrido
tiempo_label = tk.Label(root, text="", font=("Courier", 12))
tiempo_label.grid(row=5, columnspan=2)

# Variable para guardar el tiempo de inicio
inicio = 0

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()