import sys
from cx_Freeze import setup, Executable

# Script principal
script = "front2.py"

# Archivos adicionales que necesitas incluir
include_files = [
    'dividir_lista.py',
    'Final.py',
    'import_ipaddress.py',
    'inicio.py',
    'obtener_rango_ip.py',
    'prueba_mac.py',
    't20p.py',
    'test_lista.py',
    'manifest.xml'  # Añade el manifiesto
]

# Opciones adicionales (si las necesitas)
build_options = {
    "includes": [],
    "excludes": [],
    "packages": [],
    "include_files": include_files,
}

# Dependiendo del sistema operativo, cambia el directorio de salida
if sys.platform == "win32":
    base = "Win32GUI"  # Si no quieres una ventana de consola en Windows, cambia esto a "None"
    target_name = "Reset_Yealink.exe"  # Nombre del ejecutable en Windows
    icon = None  # Ruta al icono de la aplicación (si lo tienes)
else:
    base = None
    target_name = "Reset_Yealink"
    icon = None

# Configuración de la compilación
setup(
    name="Nombre de tu aplicación",
    version="1.0",
    description="Descripción de tu aplicación",
    options={"build_exe": build_options},
    executables=[Executable(script, base=base, target_name=target_name, icon=icon)]
)
