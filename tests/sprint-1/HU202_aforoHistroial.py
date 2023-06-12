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

#HU202
# Comprobar que el sistema muestre una gráfica del 
# historial de aforo diario registrado para cada uno de 
# los días de la semana actual que concuerden con los 
# registros de la base de datos

class aforoHistorialTest(unittest.TestCase):
    
    USER_PASS = os.getenv('USER_PASS')
    USER_LOG = os.getenv('USER_LOG')
    USER_NAME = os.getenv('USER_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_barraSuperiorUser(self):
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
        loginField.send_keys(self.USER_LOG)

        passField.click()
        passField.send_keys(self.USER_PASS)

        loginButton.click()
        
        time.sleep(2)
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div/div[1]/div[1]/div/div/app-bar-chart/div/div[2]") 

        print("🟢 Barras del AforoHistorial OK")


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 