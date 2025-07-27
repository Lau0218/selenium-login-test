from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir la página
driver.get("https://www.saucedemo.com")

# Esperar que la página cargue
time.sleep(2)

# Escribir el usuario
username_input = driver.find_element(By.ID, "user-name")
username_input.send_keys("standard_user")

# Escribir la contraseña
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

# Hacer clic en el botón de login
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Esperar para ver qué pasa después del login
time.sleep(5)

# Cerrar el navegador
driver.quit()
