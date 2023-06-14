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
# Visualizar todas las reservas existentes para un deporte desde la vista del admistiador

class editarDeporte(unittest.TestCase):

    ADMIN_LOG = os.getenv('ADMIN_LOG')
    ADMIN_PASS = os.getenv('ADMIN_PASS')
    ADMIN_NAME = os.getenv('ADMIN_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_editarDeporte(self):
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

        tarjetaDeporteDePrueba = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deportes/div/div/div[2]/div[8]/div/button/div/div[1]/div[2]")
        tarjetaDeporteDePrueba.click()
        time.sleep(0.5)

        botonEditarDeporte = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deporte-seleccionado/div/div/div/div[1]/div[2]/div[2]/button/span[2]/div")
        botonEditarDeporte.click()
        time.sleep(0.5)


        #EDITAR FORMS
        time.sleep(0.1)
        nombreDeporte = driver.find_element(By.XPATH, "/html/body/app-root/div/app-editar-deporte/div/div/div/form/div/div/div[1]/mat-form-field/div[1]/div/div[2]/input")
        nombreDeporte.send_keys(" Editado")
        print("🟢 Se ha llenado el campo de nombre")

        time.sleep(0.1)
        materialesDeporte = driver.find_element(By.XPATH, "/html/body/app-root/div/app-editar-deporte/div/div/div/form/div/div/div[3]/mat-form-field/div[1]/div/div[2]/input")
        materialesDeporte.send_keys(" Editado")
        print("🟢 Se ha llenado el campo de materiales")

        time.sleep(0.1)
        descripcionDeporte = driver.find_element(By.XPATH, "/html/body/app-root/div/app-editar-deporte/div/div/div/form/div/div/div[4]/mat-form-field/div[1]/div/div[2]/input")
        descripcionDeporte.send_keys(" Editado")
        print("🟢 Se ha llenado la descripcion")

        time.sleep(0.1)
        imageField = driver.find_element(By.XPATH, "/html/body/app-root/div/app-editar-deporte/div/div/div/form/div/div/div[5]/mat-form-field/div[1]/div/div[2]/mat-toolbar/div/input[2]")
        imageField.send_keys("/Users/aleksandrmorozov/Desktop/RecSports-Tests/tests/recsports_logo.png")
        print("🟢 Se ha agregado la foto")

        #Enviar Form
        botonGuardar = driver.find_element(By.XPATH, "/html/body/app-root/div/app-editar-deporte/div/div/div/form/div/div/div[7]/div/button[3]/span[2]/div")
        botonGuardar.click()
        time.sleep(2)

        print("🟢 El deporte ha sido editado")


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 

