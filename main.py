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

time.sleep(5)
driver.find_element(By.NAME, 'sign_up').click()
time.sleep(5)

## INGRESAR CUENTA ##

correo = driver.find_element(By.ID, "email_login")
correo.send_keys("manulop900@gmail.com")
contraseña = driver.find_element(By.ID, "password_login")
contraseña.send_keys("Fumito-10")

time.sleep(5)
driver.find_element(By.NAME, 'login').click()
time.sleep(20)