import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
#chromediver download from selenium-manager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import os
from dotenv import load_dotenv
import time

load_dotenv()
PAGE_ADDRESS = os.getenv('PAGE_ADDRESS')

#HU404
# Agregar un deporte a la lista de deportes y 
# se visualice en la página “Deportes” de otro usuario.

class agregarDeporte(unittest.TestCase):

    ADMIN_LOG = os.getenv('ADMIN_LOG')
    ADMIN_PASS = os.getenv('ADMIN_PASS')
    ADMIN_NAME = os.getenv('ADMIN_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_agregarDeporte(self):
        driver = self.driver

        #Page Loads Correctly
        driver.get(PAGE_ADDRESS + "/login")
        self.assertIn("Athletics", driver.title)

        #Page Elements 
        loginField = driver.find_element(By.XPATH, "//*[@id='mat-input-0']")
        passField = driver.find_element(By.XPATH, "//*[@id='mat-input-1']")

        loginButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-login/mat-sidenav-container/mat-sidenav-content/div/div/form/div[3]/button")

        #Fields Input 
        loginField.click()
        loginField.send_keys(self.ADMIN_LOG)

        passField.click()
        passField.send_keys(self.ADMIN_PASS)

        loginButton.click()
        time.sleep(2)
        
        #================= END LOGIN ===================

        driver.get(PAGE_ADDRESS + "/deportes")
        time.sleep(2)

        agregarDeporteBoton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deportes/div/div/div[1]/div[1]/button/span[2]/div")
        agregarDeporteBoton.click()
        time.sleep(2)

        #Llenar forms
        time.sleep(0.1)
        nombreDeporte = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nuevo-deporte/div/div/div/form/div/div/div[1]/mat-form-field/div[1]/div/div[2]/input")
        nombreDeporte.send_keys("Deporte de Prueba")
        print("🟢 Se ha llenado el campo de nombre")

        time.sleep(0.1)
        duracionDeporte = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nuevo-deporte/div/div/div/form/div/div/div[2]/mat-form-field/div[1]/div/div[2]/input")
        duracionDeporte.send_keys("60")
        print("🟢 Se ha llenado el campo de duracion")

        time.sleep(0.1)
        materialesDeporte = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nuevo-deporte/div/div/div/form/div/div/div[3]/mat-form-field/div[1]/div/div[2]/input")
        materialesDeporte.send_keys("Prueba")
        print("🟢 Se ha llenado el campo de materiales")

        time.sleep(0.1)
        descripcionDeporte = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nuevo-deporte/div/div/div/form/div/div/div[4]/mat-form-field/div[1]/div/div[2]/input")
        descripcionDeporte.send_keys("Descripcion de prueba")
        print("🟢 Se ha llenado la descripcion")

        time.sleep(0.1)
        imageField = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nuevo-deporte/div/div/div/form/div/div/div[5]/mat-form-field/div[1]/div/div[2]/mat-toolbar/div/input[2]")
        imageField.send_keys("/Users/aleksandrmorozov/Desktop/RecSports-Tests/tests/recsports_logo.png")
        print("🟢 Se ha agregado la foto")

        #Enviar Form
        botonGuardar = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nuevo-deporte/div/div/div/form/div/div/div[7]/div/button[2]/span[2]/div")
        botonGuardar.click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 

