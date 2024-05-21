########################################### INSTALACION O VERIFICACION DE NMAP ###################################
    #########################################################################################################
import subprocess
import sys


def instalar_ipaddress():
    try:
        subprocess.run([sys.executable, "import-ipaddress.py"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error al instalar ipaddress:", e)

# Verificar si ipaddress está instalado
try:
    import ipaddress
    
except ImportError:
    instalar_ipaddress()

# Importar nmap si está instalado
try:
    import ipaddress
except ImportError:
    sys.exit(1)

########################################### Obtener direcciones ip ###################################
    #########################################################################################################

def obtener_direcciones_de_red(rango_de_red):
    direcciones = []
    red = ipaddress.ip_network(rango_de_red)
    for ip in red:
        direcciones.append(str(ip))
    direcciones.pop(0)
    direcciones.pop()
    return direcciones
