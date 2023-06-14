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

class visualizarReservas(unittest.TestCase):

    ADMIN_LOG = os.getenv('ADMIN_LOG')
    ADMIN_PASS = os.getenv('ADMIN_PASS')
    ADMIN_NAME = os.getenv('ADMIN_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_visualizarReservas(self):
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

        #================= END LOGIN ===================

        time.sleep(2)
        driver.get("https://rec-sports-front.vercel.app/deportes/1d16b6f2-bee6-4fae-a74e-cbffcdf12a19")
        
        time.sleep(2)
        #navegar a ultimo dia de semana
        diaDeSemana = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deporte-seleccionado/div/div/div/div[3]/div[2]/div[9]/div/div/button/span[2]")
        diaDeSemana.click()

        time.sleep(2)
        #Prueba espacio reservado / visiualizar reservador
        espacioReservado = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deporte-seleccionado/div/div/div/div[3]/div[3]/table/tbody/tr[5]/td[2]/div[3]/div[2]/button/span[2]/div")
        espacioReservado.click()

        reservador = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/div/div/app-modal-reservacion/div/div[2]/div[5]/span[2]").text
        assert reservador == "ADMIN"

        print("🟢 Reservado Detectado")

        #Prueba visualziar reserva normal
        espacioNoReservado = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deporte-seleccionado/div/div/div/div[3]/div[3]/table/tbody/tr[6]/td[2]/div[3]/div[2]/button/span[5]")
        assert espacioNoReservado

        print("🟢 Reservacion Detectada")


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 

