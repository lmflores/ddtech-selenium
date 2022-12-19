import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
# Avoid site blocking by cloudfire
import undetected_chromedriver  as uc

driver = uc.Chrome()
driver.get("https://ddtech.mx/")
driver.maximize_window()
time.sleep(12)


###  REGISTRO ##
def signup():
    driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div/div[3]/ul/li[3]/a').click()
    time.sleep(5)
    usuario = driver.find_element(By.ID, "username")
    usuario.send_keys("Fumito10")
    correo = driver.find_element(By.ID, "email")
    correo.send_keys("manulop900@gmail.com")
    contraseña = driver.find_element(By.ID, "password")
    contraseña.send_keys("Fumito-10")
    confir_contra = driver.find_element(By.ID, "confirm_password")
    confir_contra.send_keys("Fumito-10")

    time.sleep(2)
    driver.find_element(By.NAME, 'sign_up').click()
    time.sleep(5)


## INGRESAR CUENTA ##
def login():
    correo = driver.find_element(By.ID, "email_login")
    correo.send_keys("manulop900@gmail.com")
    contraseña = driver.find_element(By.ID, "password_login")
    contraseña.send_keys("Fumito-10")

    time.sleep(5)
    driver.find_element(By.NAME, 'login').click()
    time.sleep(10)


## DATOS ENVIO ##
def setup_shipment_data():
    driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div/div[3]/ul/li[1]/a').click()
    time.sleep(5)
    calle = driver.find_element(By.ID, "form_name")
    calle.send_keys("Cruz Manuel")
    calle = driver.find_element(By.ID, "form_last_name")
    calle.send_keys("López Mera")

    calle = driver.find_element(By.ID, "form_street")
    calle.send_keys("Venustiano Carranza")
    numero = driver.find_element(By.ID, "form_number")
    numero.send_keys("8")
    cp = driver.find_element(By.ID, "form_zipcode")
    cp.send_keys("42760")
    colonia = driver.find_element(By.ID, "form_colony")
    colonia.send_keys("Tezontepec de Aldama")
    ciudad = driver.find_element(By.ID, "form_town")
    ciudad.send_keys("Tezontepec de Aldama")
    tel = driver.find_element(By.ID, "form_phone")
    tel.send_keys("1123456789")
    driver.find_element(By.ID, "form_state").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="form_state"]/option[14]').click()

    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/form/div[11]/div/button').click()
    # go back to main page
    driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div/div[1]/a").click()
## Add cart items ##

articles = {
            'Accesorios': 'Mouse Gamer Logitech G502 X Lightspeed / Óptico / Blanco / Inalámbrico / 25.600DPI / Interruptores Lightforce / 910-006188',
            'Componentes': 'Tarjeta Madre Asus X670 ROG Strix X670E-I Gaming / AMD / AM5 / Ryzen 7000 / Mini-ITX / WiFi 6E / PCIe 5.0 / DDR5 / botón EZ Mode PBO / 2X M.2 / 2X USB4 Tipo C / ROG STRIX X670E-I GAMING WIFI',
            'Almacenamiento': 'Memoria USB Tipo C 256GB / ADATA ELITE UE800 / Gris - Negro / AELI-UE800-256G-CSG',
            'Software': 'Licencia Microsoft Office Hogar y Estudiantes 2021 Licencia Descargable - Multi Lenguaje 1 PC/Mac - 79G-0534',
            'Celulares': 'Smartband Huawei Band 6 B10 Negro Grafito / Android / Bluetooth / Resistente al agua / FRA-B19B',
        }

def add_cart():
    for category, name in articles.items():
        driver.find_element(By.XPATH, "//a[contains(text(),\'" + category + "\')]").click()
        time.sleep(2)
        container = driver.find_element(By.CSS_SELECTOR, 'li.dropdown.menu-item.open')
        container.find_element(By.CSS_SELECTOR, "ul > li > div > div:nth-child(1) > ul > li:nth-child(1) > a").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),\'" + name + "\')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),\' Agregar al carrito\')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div/div[1]/a").click()
        time.sleep(2)
       

def show_cart():
    driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div/div[2]/ul[2]/li[2]/a").click()
    time.sleep(2)


signup()
login()
setup_shipment_data()
add_cart()
show_cart()


time.sleep(20)