import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
#chromediver download from selenium-manager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

import os
from dotenv import load_dotenv
import time

load_dotenv()
PATH = os.getenv('PATH')
PAGE_ADDRESS = os.getenv('PAGE_ADDRESS')


#HU101
# Ingresar con los datos de tres tipos de 
# usuario y verificar que puedan acceder a sus componentes


class LoginPageTest(unittest.TestCase):

    USER_LOG = os.getenv('USER_LOG')
    USER_PASS = os.getenv('USER_PASS')
    USER_NAME = os.getenv('USER_NAME')

    ADMIN_LOG = os.getenv('ADMIN_LOG')
    ADMIN_PASS = os.getenv('ADMIN_PASS')
    ADMIN_NAME = os.getenv('ADMIN_NAME')

    TRAINER_LOG = os.getenv('TRAINER_LOG')
    TRAINER_PASS = os.getenv('TRAINER_PASS')
    TRAINER_NAME = os.getenv('TRAINER_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def test_adminLogin(self):
        driver = self.driver

        #Page Loads Correctly
        driver.get(PAGE_ADDRESS + "/login")
        self.assertIn("Athletic", driver.title)

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


        #Page Deporte
        deporteButton = driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/div[2]/a/span/span/div/span")
        deporteButton.click()
        time.sleep(2)

        #Page Baloncesto
        baloncestoButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deportes/div/div/div[2]/div[1]/div/button/div/div[1]/div[2]")
        baloncestoButton.click()
        time.sleep(2)

        #Seleccionar dia
        reservacionButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deporte-seleccionado/div/div/div/div[3]/div[2]/div[9]/div/div/button/span[2]")
        reservacionButton.click()
        time.sleep(2)

        #Mostrar detalles reservacion
        reservacionButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-deporte-seleccionado/div/div/div/div[3]/div[3]/table/tbody/tr[6]/td[2]/div[3]/div[1]/button/span[2]/div")
        reservacionButton.click()
        time.sleep(2)

        #Validar que se muestran detalles de la reservacion
        self.assertEqual(driver.find_element(By.XPATH, "/html/body/div/div[3]/div/mat-dialog-container/div/div/app-modal-reservacion/div/div[2]/div[1]/span[2]").text, "2023-06-17")
        self.assertEqual(driver.find_element(By.XPATH, "/html/body/div/div[3]/div/mat-dialog-container/div/div/app-modal-reservacion/div/div[2]/div[2]/span[2]").text, "11:00:00")
        self.assertEqual(driver.find_element(By.XPATH, "/html/body/div/div[3]/div/mat-dialog-container/div/div/app-modal-reservacion/div/div[2]/div[3]/span[2]").text, "Cancha 2")
        self.assertEqual(driver.find_element(By.XPATH, "/html/body/div/div[3]/div/mat-dialog-container/div/div/app-modal-reservacion/div/div[2]/div[4]/span[2]").text, "Wellness Center")
        print("🟢 DETALLES RESERVACION OK")

        #Hacer Reservacion
        confirmarReservacion = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/mat-dialog-container/div/div/app-modal-reservacion/div/div[3]/button/span[2]")
        confirmarReservacion.click()
        time.sleep(2)
        print("🟢 RESERVACION CONFIRMADA OK")

        #Ir a pagina mis reservaciones
        confirmarReservacion = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/mat-dialog-container/div/div/app-modal-reservacion/div/div[3]/button/span[2]")
        confirmarReservacion.click()
        time.sleep(2)

        #Boton eliminar reservacion
        cancelarButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-reservaciones/div/div/div/div/div[6]/button/span[2]/div")
        cancelarButton.click()
        time.sleep(2)

        #CEliminar reservacion en modal
        confirmarCancelacion = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/mat-dialog-container/div/div/app-modal/div/div[2]/div[5]/button/span[2]")
        confirmarCancelacion.click()
        time.sleep(2)
        
       

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 