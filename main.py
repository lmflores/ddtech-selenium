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
correo = driver.find_element(By.ID, "email_login")
correo.send_keys("manulop900@gmail.com")
contraseña = driver.find_element(By.ID, "password_login")
contraseña.send_keys("Fumito-10")

time.sleep(5)
driver.find_element(By.NAME, 'login').click()
time.sleep(10)


## DATOS ENVIO ##
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



time.sleep(20)