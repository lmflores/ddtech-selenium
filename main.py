import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
# Avoid site blocking by cloudfire
import undetected_chromedriver  as uc
driver = uc.Chrome()
  ###  REGISTRO ##
driver.get("https://ddtech.mx/")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div/div[3]/ul/li[3]/a/font/font').click()

time.sleep(1)

usuario = driver.find_element(By.ID, "username")
time.sleep(1)
correo = driver.find_element(By.ID, "email")
time.sleep(1)
contraseña = driver.find_element(By.ID, "password")
time.sleep(1)
confir_contra = driver.find_element(By.ID, "confirm_pas")
time.sleep(1)

usuario.send_keys("Fumito10")
time.sleep(1)
correo.send_keys("manulop900@gmail.com")
time.sleep(1)
contraseña.send_keys("Fumito-10")
time.sleep(1)
confir_contra.send_keys("Fumito-10")
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/form/button').click()
