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

#HU208
# Comprobar que el sistema registre una salida 
# nueva al escribir la matrícula del alumno de manera 
# manual

class registroSalidaManual(unittest.TestCase):
    
    TRAINER_LOG = os.getenv('TRAINER_LOG')
    TRAINER_PASS = os.getenv('TRAINER_PASS')
    TRAINER_NAME = os.getenv('TRAINER_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_pronosticoAforo(self):
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
        loginField.send_keys(self.USER_LOG)

        passField.click()
        passField.send_keys(self.USER_PASS)

        loginButton.click()
        #=================================================================

        time.sleep(2)
        sideBarSalida = driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/div[4]/a/span/span/div/mat-icon")
        sideBarSalida.click()

        time.sleep(2)
        salidaInputField = driver.find_element(By.XPATH, "/html/body/app-root/div/app-registro-entrada/div/div/div[1]/mat-form-field/div[1]/div/div[2]/input")
        salidaInputField.send_keys("A00824394")
        salidaInputField.send_keys(Keys.ENTER)

        #falta ir a la tabla a verificar que la hora de salida se haya agregado 

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 
