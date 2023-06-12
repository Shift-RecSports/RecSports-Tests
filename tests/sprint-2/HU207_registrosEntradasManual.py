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

#HU207
# Comprobar que el sistema registre una entrada 
# nueva al escribir la matrícula del alumno de manera 
# manual y la añada correctamente a la tabla
# de registros en tiempo real.

class registrosEntradasManualTest(unittest.TestCase):

    TRAINER_LOG = os.getenv('TRAINER_LOG')
    TRAINER_PASS = os.getenv('TRAINER_PASS')
    TRAINER_NAME = os.getenv('TRAINER_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_registroEntrada(self):
        driver = self.driver

        #Page Loads Correctly
        driver.get(PAGE_ADDRESS + "/login")
        self.assertIn("Athletics", driver.title)

        #=========================  LOGIN =================================
        #Page Elements 
        loginField = driver.find_element(By.XPATH, "//*[@id='mat-input-0']")
        passField = driver.find_element(By.XPATH, "//*[@id='mat-input-1']")

        loginButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-login/mat-sidenav-container/mat-sidenav-content/div/div/form/div[3]/button")

        #Fields Input 
        loginField.click()
        loginField.send_keys(self.TRAINER_LOG)

        passField.click()
        passField.send_keys(self.TRAINER_PASS)

        loginButton.click()
        #=================================================================

        time.sleep(2)
        sideBarEntrada = driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/div[3]/a/span/span/div/mat-icon")
        sideBarEntrada.click()

        time.sleep(2)
        entradaInputField = driver.find_element(By.XPATH, "/html/body/app-root/div/app-registro-entrada/div/div/div[1]/mat-form-field/div[1]/div/div[2]/input")
        entradaInputField.send_keys("A00824394")
        entradaInputField.send_keys(Keys.ENTER)

        #Falta ir a la tabla a verificar si el usuario se haya registrado

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main() 
        