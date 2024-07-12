from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from time import sleep
import os


# ====== Configuração inicial ======
load_dotenv()
URL = os.getenv("URL")


def check_ticket(driver):

    driver.get(f'{URL}/ocomon/geral/tickets_main.php')

    # CORRIGIR A ADAPTAÇÃO DE ESPERA
    sleep(3)

    tabela = driver.find_element(By.XPATH, '//*[@id="table_my_queued"]/tbody')

    # Coleta todas as linhas da tabela
    linhas = tabela.find_elements(By.TAG_NAME, "tr")

    # Lista para armazenar os dados
    tickets = []

    for linha in linhas:
        # Coleta todas as células da linha
        celulas = linha.find_elements(By.TAG_NAME, "td")
        
        # Adiciona os dados desejados à lista
        tickets.append([celulas[1].text, celulas[2].text, celulas[3].text, 
                    celulas[4].text, celulas[5].text, celulas[6].text, celulas[7].text])
   
    
    return tickets
