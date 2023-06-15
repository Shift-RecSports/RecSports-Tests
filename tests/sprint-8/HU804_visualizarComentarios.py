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

#HU804
#Comprobar que los usuarios de tipo Administrador
#  puedan agregar anuncios a la plataforma, y que estas 
# puedan ser visibles para los alumnos.

class visualizarPromedio(unittest.TestCase):
    
    ADMIN_LOG = os.getenv('ADMIN_LOG')
    ADMIN_PASS = os.getenv('ADMIN_PASS')
    ADMIN_NAME = os.getenv('ADMIN_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_visualizarPromedio(self):
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
        #============================LOGIN COMPLETE============================

        driver.get(PAGE_ADDRESS + "/encuesta-admin")
        time.sleep(2)

        comentarios = driver.find_element(By.XPATH, "/html/body/app-root/div/app-encuestas-admin/div/div/nz-tabset/nz-tabs-nav/div/div/div[2]/div")
        comentarios.click()
        time.sleep(1)

        comentarioIndiviudal = driver.find_element(By.XPATH, "/html/body/app-root/div/app-encuestas-admin/div/div/nz-tabset/div/div/div[2]/div/div[1]")
        assert comentarioIndiviudal
        print("🟢 Se han visualizado los comentarios")

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 



