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

#HU204
# Comprobar que la tabla de registros de alumnos 
# en el gimnasio sea visible y muestre los datos 
# de entrada y salida para cada uno de los alumnos 
# que se registren en tiempo real

class tablaRegistroGimnasio(unittest.TestCase):

    TRAINER_LOG = os.getenv('TRAINER_LOG')
    TRAINER_PASS = os.getenv('TRAINER_PASS')
    TRAINER_NAME = os.getenv('TRAINER_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_registroGimnasio(self):
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
        time.sleep(3)
        #=================================================================
        
        #do entrada
        driver.get("https://rec-sports-front.vercel.app/gimnasio/entrada")
        time.sleep(2)

        inputField = driver.find_element(By.XPATH, "/html/body/app-root/div/app-registro-entrada/div/div/div[1]/mat-form-field/div[1]/div/div[2]/input")
        inputField.send_keys("A00824394")
        inputField.send_keys(Keys.ENTER)
        time.sleep(0.5)

        #navigate to the table page to find register
        driver.get("https://rec-sports-front.vercel.app/gimnasio")
        time.sleep(2)

        tableTopElement = driver.find_element(By.XPATH, "/html/body/app-root/div/app-gimnasio/div/div/div[2]/table/tbody/tr[1]/td[1]").text
        assert tableTopElement == "A00824394"
        


        #do salida
        driver.get("https://rec-sports-front.vercel.app/gimnasio/salida")
        time.sleep(2)

        inputField = driver.find_element(By.XPATH, "/html/body/app-root/div/app-registro-salida/div/div/div/mat-form-field/div[1]/div/div[2]/input")
        inputField.send_keys("A00824394")
        inputField.send_keys(Keys.ENTER)
        time.sleep(0.5)

        #navigate to the table page to find register
        driver.get("https://rec-sports-front.vercel.app/gimnasio")
        time.sleep(2)

        tableTopElement = driver.find_element(By.XPATH, "/html/body/app-root/div/app-gimnasio/div/div/div[2]/table/tbody/tr[1]/td[1]").text
        assert tableTopElement == "A00824394"

        salidaField = driver.find_element(By.XPATH, "/html/body/app-root/div/app-gimnasio/div/div/div[2]/table/tbody/tr[1]/td[4]").text
        assert salidaField is not None
        

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 