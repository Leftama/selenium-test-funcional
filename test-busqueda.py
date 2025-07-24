from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")
# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("pan con queso")
buscador.send_keys(Keys.RETURN)
# Esperar resultados
time.sleep(2)
# Validar que exista algún resultado
resultados = driver.find_elements(By.CSS_SELECTOR, "[data-testid='result']")
assert len(resultados) > 0, "No se encontraron resultados."
print("Prueba funcional completada con éxito")
driver.quit()