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

#HU601
#Comprobar la visualización de anuncios
#  relevantes de RecSports y LiFE en la
#  pantalla de inicio.

class llenarEncuesta(unittest.TestCase):

    USER_LOG = os.getenv('USER_LOG')
    USER_PASS = os.getenv('USER_PASS')
    USER_NAME = os.getenv('USER_NAME')


    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_llenarEncuesta(self):
        driver = self.driver

        #================ BEIGN USER LOGIN ====================

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

        #================= END USER LOGIN ===================

        driver.get(PAGE_ADDRESS + "/encuesta")
        time.sleep(2)


        #gimnasio
        gimnasioRateBar = driver.find_element(By.XPATH, "/html/body/app-root/div/app-encuesta/div/div/div[1]/div/div/mat-slider/input")
        driver.execute_script("arguments[0].setAttribute('aria-valuetext', '10');", gimnasioRateBar)
        
        wellnessRateBar = driver.find_element(By.XPATH, "/html/body/app-root/div/app-encuesta/div/div/div[2]/div/div/mat-slider/input")
        driver.execute_script("arguments[0].setAttribute('aria-valuetext', '10');", wellnessRateBar)

        athleticsWebRateBar = driver.find_element(By.XPATH, "/html/body/app-root/div/app-encuesta/div/div/div[3]/div/div/mat-slider/input")
        driver.execute_script("arguments[0].setAttribute('aria-valuetext', '10');", athleticsWebRateBar)

        #Bottom Part
        temaField = driver.find_element(By.XPATH, "/html/body/app-root/div/app-encuesta/div/div/div[4]/div/nz-select/nz-select-top-control/nz-select-search/input")
        temaField.click()
        specificTemaField = driver.find_element(By.XPATH, "/html/body/div/div/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[4]/div")
        specificTemaField.click()

        #comment field
        commentField = driver.find_element(By.XPATH, "/html/body/app-root/div/app-encuesta/div/div/div[4]/textarea")
        commentField.send_keys("This is a test comment")
        print("🟢 Encuesta se ha generado satisfactoriamente")

        botonEnviar = driver.find_element(By.XPATH, "/html/body/app-root/div/app-encuesta/div/div/div[4]/button")
        botonEnviar.click()

        time.sleep(2)

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 

