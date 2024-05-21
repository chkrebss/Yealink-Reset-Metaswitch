import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciar_navegador(ip):
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)
    url = "http://" + ip + "/servlet?p=settings-upgrade&q=load"
    print("Abriendo URL:", url)
    driver.get(url)
    return driver

def iniciar_sesion(driver):
    username_field = driver.find_element("name", "username")
    password_field = driver.find_element("name", "pwd")
    username_field.send_keys("admin")
    password_field.send_keys("admin")
    login_button = driver.find_element("id", "idConfirm")
    login_button.click()
    print("Inicio de sesión exitoso.")

def abrir_configuracion(driver, url):
    print("Abriendo settings")
    driver.get(url + "/servlet?p=settings-upgrade&q=load")
    print("Página de configuración abierta.")

def resetear_fabrica(driver):
    # Esperar hasta que el botón de reseteo de fábrica esté presente en la página
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnResetFactory")))
    
    reset_button = driver.find_element("id", "btnResetFactory")
    print("reset boton es: "+str(reset_button))
    reset_button.click()
    print("Reseteo de fábrica iniciado.")
    time.sleep(1)
    alert = driver.switch_to.alert
    print("Mensaje de confirmación:", alert.text)
    alert.accept()

def configurar_proxy(driver, url):
    driver.get(url + "/servlet?p=account-register&q=load&acc=0")
    time.sleep(3)
    iniciar_sesion(driver)
    print("url proxy abierta")
    time.sleep(3)
    print("Seleccionando proxy")
    select_proxy = Select(driver.find_element("name", "AccountOutboundSwitch"))
    select_proxy.select_by_value("1")
    print("Proxy seleccionado.")
    proxy_field = driver.find_element("name", "AccountOutboundProxy")
    proxy_field.clear()
    proxy_field.send_keys("10.32.254.90")
    print("Proxy agregado.")
    time.sleep(1)
    select_confirm = driver.find_element(By.NAME, "btnSubmit")
    select_confirm.click()
    print("Configuración de proxy confirmada.")

def deshabilitar_certificado(driver, url):
    driver.get(url + "/servlet?p=trusted-cert&q=load")
    time.sleep(2)
    print("Deshabilitando certificado.")
    select_certificado = Select(driver.find_element("name", "HTTPSTrustCertificates"))
    select_certificado.select_by_value("0")
    time.sleep(1)
    select_confirm = driver.find_element(By.NAME, "btnSubmit")
    select_confirm.click()
    time.sleep(2)
    alert = driver.switch_to.alert
    print("Mensaje de confirmación:", alert.text)
    alert.accept()
    print("Certificado deshabilitado.")
    time.sleep(1)

def ini_web(ip):
    #ip = input("Ingrese la dirección IP: ")
    driver = iniciar_navegador(ip)
    try:
        iniciar_sesion(driver)
        abrir_configuracion(driver, "http://" + ip)
        time.sleep(3)
        resetear_fabrica(driver)
        WebDriverWait(driver, 180).until(EC.presence_of_element_located(By.NAME, "username"))
        configurar_proxy(driver, "http://" + ip)
        time.sleep(3)
        deshabilitar_certificado(driver, "http://" + ip)
        print("Proceso completo.")
    except Exception as e:
        print("Ocurrió un error:", e)
    finally:
        driver.quit()

def main():
    ip = input("Ingrese la dirección IP: ")
    driver = iniciar_navegador(ip)
    try:
        iniciar_sesion(driver)
        abrir_configuracion(driver, "http://" + ip)
        time.sleep(3)
        resetear_fabrica(driver)
        time.sleep(100)
        configurar_proxy(driver, "http://" + ip)
        time.sleep(3)
        deshabilitar_certificado(driver, "http://" + ip)
        print("Proceso completo.")
    except Exception as e:
        print("Ocurrió un error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
