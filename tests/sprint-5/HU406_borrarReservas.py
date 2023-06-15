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

#HU405
#Separar un bloque de tiempo en un espacio deportivo 
#y que este se vea bloqueado en el calendario de otro usuario.
class borrarReservas(unittest.TestCase):

    ADMIN_LOG = os.getenv('ADMIN_LOG')
    ADMIN_PASS = os.getenv('ADMIN_PASS')
    ADMIN_NAME = os.getenv('ADMIN_NAME')

    USER_LOG = os.getenv('USER_LOG')
    USER_PASS = os.getenv('USER_PASS')
    USER_NAME = os.getenv('USER_NAME')


    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_borrarReservas(self):
        driver = self.driver
        #================ BEIGN ADMIN LOGIN ====================
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

        #================= END ADMIN LOGIN ====================

        #Realizar una reserva
        time.sleep(2)
        driver.get("https://rec-sports-front.vercel.app/deportes/1d16b6f2-bee6-4fae-a74e-cbffcdf12a19")
        
        time.sleep(2)
        #navegar a ultimo dia de semana
        diaDeSemana = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deporte-seleccionado/div/div/div/div[3]/div[2]/div[9]/div/div/button/span[2]")
        diaDeSemana.click()

        time.sleep(2)
        reservedField = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deporte-seleccionado/div/div/div/div[3]/div[3]/table/tbody/tr[5]/td[2]/div[3]/div[1]/button/span[2]/div")
        reservedField.click()
        
        time.sleep(2)
        reservator = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/div/div/app-modal-reservacion/div/div[2]/div[5]/span[2]").text
        assert reservator == self.USER_LOG
        print("🟢 The user matches and the reservation is visible")
        #========================================================
        
        #Cancel Reservation for future tests
        cancelReservation = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/div/div/app-modal-reservacion/div/div[3]/button/span[2]")
        cancelReservation.click()
        print("🟢 Test Reset")


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 

