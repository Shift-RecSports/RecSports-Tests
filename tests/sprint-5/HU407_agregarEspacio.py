import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
#chromediver download from selenium-manager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

import os
from dotenv import load_dotenv

load_dotenv()
PAGE_ADDRESS = os.getenv('PAGE_ADDRESS')

#HU407
#Agregar un espacio deportivo a un deporte y 
#que este sea visible para todos en el sistema.

class pronosticoAforoTest(unittest.TestCase):
    
    ADMIN_LOG = os.getenv('ADMIN_LOG')
    ADMIN_PASS = os.getenv('ADMIN_PASS')
    ADMIN_NAME = os.getenv('ADMIN_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_agregarEspacio(self):
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
        #============================LOGIN COMPLETE============================

        time.sleep(2)
        driver.get("https://rec-sports-front.vercel.app/deportes/1d16b6f2-bee6-4fae-a74e-cbffcdf12a19")

        time.sleep(2)
        addSpace = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deporte-seleccionado/div/div/div/div[2]/div[2]/div[3]/button")
        addSpace.click()
        print("🟢 Agregar Espacio")

        time.sleep(2)
        nombreEspacio = driver.find_element(By.XPATH, "/html/body/app-root/div/app-espacios-formulario/div/div/div/form/div/div[1]/mat-form-field/div[1]/div/div[2]/input")
        nombreEspacio.send_keys("Espacio de Prueba")
        print("🟢 Se agrego el nombre de espacio")

        time.sleep(2)
        areaEspacio = driver.find_element(By.XPATH, "/html/body/app-root/div/app-espacios-formulario/div/div/div/form/div/div[2]/mat-form-field/div[1]/div/div[2]/input")
        areaEspacio.send_keys("Area de Prueba")
        print("🟢 Se agrego el area del espacio")

        time.sleep(2)
        aforoEspacio = driver.find_element(By.XPATH, "/html/body/app-root/div/app-espacios-formulario/div/div/div/form/div/div[3]/mat-form-field/div[1]/div/div[2]/input")
        aforoEspacio.send_keys("10")
        print("🟢 Se agrego el aforo del espacio")
        
        time.sleep(2)
        deporteEspacio = driver.find_element(By.XPATH, "/html/body/app-root/div/app-espacios-formulario/div/div/div/form/div/div[4]/mat-form-field/div[1]/div/div[2]/input")
        deporteEspacio.send_keys("Baloncesto")
        print("🟢 Se agrego el deporte correspondiente")

        time.sleep(2)
        horarioEsoacio = driver.find_element(By.XPATH, "/html/body/app-root/div/app-espacios-formulario/div/div/div/form/div/div[5]/mat-form-field/div[1]/div/div[1]/div[2]/label/mat-label")
        horarioEsoacio.click()

        time.sleep(2)
        horaEspecifica = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/mat-option[3]/mat-pseudo-checkbox")
        horaEspecifica.click()
        print("🟢 Se agrego el nombre de espacio")

        time.sleep(2)
        fileUpload = driver.find_element(By.XPATH, "/html/body/app-root/div/app-espacios-formulario/div/div/div/form/div/div[6]/mat-form-field/div[1]/div/div[2]/mat-toolbar/div/input[2]")
        fileUpload.send_keys("/Users/aleksandrmorozov/Desktop/RecSports-Tests/tests/recsports_logo.png")
        print("🟢 Se ha subido el espacio")

        nombreEspacio.send_keys(Keys.ESCAPE)

        time.sleep(5)
        submitSpace = driver.find_element(By.XPATH, "/html/body/app-root/div/app-espacios-formulario/div/div/div/form/div/div[8]/div/button[2]")
        submitSpace.click()

        time.sleep(2)

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 



