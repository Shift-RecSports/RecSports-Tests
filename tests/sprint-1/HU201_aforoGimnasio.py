import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
#chromediver download from selenium-manager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import os
from dotenv import load_dotenv

load_dotenv()
PAGE_ADDRESS = os.getenv('PAGE_ADDRESS')


#HU201
# Verificar que el panel con el aforo actual sea visible 
# y sea correcto en base a los registros de entrada en el gimnasio

class aforoGimnasioTest(unittest.TestCase):

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

        #Login Page Loaded Correctly and the User is Admin
        try:
            elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='donut-card']"))
            )
        finally:
            time.sleep(3)
            aforoActual = driver.find_element(By.XPATH, "//*[@id='donut-card']/div/app-donut-chart/div/div[2]/div[1]").text

            print(aforoActual)
            result_array = str(aforoActual).split('/')
            aforoActual = int(result_array[0])
            print(aforoActual)

            assert aforoActual >= 0
            print("🟢 DEBUG: AFORO ACTUAL MAYOR A 0")




    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 