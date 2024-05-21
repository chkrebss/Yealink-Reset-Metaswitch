import subprocess

def instalar_ipaddress():
    try:
        subprocess.run(["pip", "install", "ipaddress"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error al instalar ipaddress:", e)

# Instalar ipaddress
instalar_ipaddress()
