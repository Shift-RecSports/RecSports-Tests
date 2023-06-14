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

#HU605
#Comprobar eliminación de anuncios existentes mediante la interfaz de Administrador.

class borrarAnuncios(unittest.TestCase):
    
    ADMIN_LOG = os.getenv('ADMIN_LOG')
    ADMIN_PASS = os.getenv('ADMIN_PASS')
    ADMIN_NAME = os.getenv('ADMIN_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_borrarAnuncios(self):
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
        driver.get(PAGE_ADDRESS + "/noticias")
        time.sleep(2)

        deleteButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-noticias/div/div/nz-row/nz-col[6]/nz-card/button/span[5]")
        deleteButton.click()
        time.sleep(2)

        confirmar = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/div/div/app-modal-borrar-noticia/div/div[5]/button/span[2]")
        confirmar.click()
        time.sleep(2)
        print("🟢 Se ha borrado la noticia")


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 



