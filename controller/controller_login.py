from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from time import sleep
import os

# ====== Configuração inicial ======
load_dotenv()
URL = os.getenv("URL")


def go_login(driver):

    driver.get(f'{URL}/index.php')

    driver.find_element(By.ID, "user").send_keys(os.getenv("USER"))
    driver.find_element(By.ID, "pass").send_keys(os.getenv("PASSWORD"))
    driver.find_element(By.ID, "bt_login").click()

    # CORRIGIR A ADAPTAÇÃO DE ESPERA
    sleep(5)

    return True