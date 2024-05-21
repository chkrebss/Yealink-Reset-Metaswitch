########################################### INSTALACION O VERIFICACION DE NMAP ###################################
    #########################################################################################################
import ctypes
import sys
import scapy.all as scapy
from concurrent.futures import ThreadPoolExecutor

def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        # Si el usuario ya tiene privilegios de administrador, ejecutar el código principal
        #print("Ya tienes privilegios de administrador.")
        return True
    else:
        # Si el usuario no tiene privilegios de administrador, solicitarlos
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            return True
        except Exception as e:
            #print("Error al solicitar permisos de administrador:", e)
            return False
    
def obtener_mac(rango):
    
    ip_yealink = []
    contador = 0


################# OBTENER IP DE TELEFONOS YEALINK CON SCAPY ##################
    for ip in rango:
        #print ("inicio for obtener mac en prueba_mac.py "+ip)
        arp_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip)
        #print ("arp_request "+arp_request)
        respuesta = scapy.srp(arp_request, timeout=2, verbose=False)[0]
        for _, respuesta in respuesta:
            if respuesta.haslayer(scapy.ARP):
                mac = respuesta[scapy.ARP].hwsrc
                #print (mac)
                #if mac and mac.startswith(('d4:a6:51', '84:e3:42', '80:5E:C0', '80:5E:0C', '00:15:65')): # MAC DISPOSITIVOS TUYA SMART
                if mac and mac.startswith(('80:5E:C0', '80:5E:0C', '00:15:65', '24:9A:D8', )): # mac yealink para comparar
                    contador += 1
                    #print("Dispositivos encontrados:", contador)
                    ip_yealink.append(ip)  

    #print("Dispositivos Yealink encontrados:", ip_yealink)  
    return ip_yealink