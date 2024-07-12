from controller.controller_webdriver_manager import WebDriverManager
from controller.controller_login import go_login
from controller.controller_check_ticket import check_ticket
from controller.controller_send_notification import send_notification
from view.view_message import view_message
from dotenv import load_dotenv
import os

TOKEN = os.getenv("TOKEN")
ID_CHAT = os.getenv("ID_CHAT")
id_tickets = []
contatos = []
tempos = []


def main():
    driver_manager = WebDriverManager()
    driver = driver_manager.start_driver()
    
    try:
        
        go_login(driver)
        
        # Intera entre os dados dos chamados disponiveis para criar uma lista
        for i in range(len(check_ticket(driver))):
            
            old_id_ticket = check_ticket(driver)[i][0].replace("BREVES - TIC", "") # Ajusta o id para remover a localidade
            id_tickets.append(old_id_ticket.strip())
            contatos.append(check_ticket(driver)[i][2].strip())
            tempos.append(check_ticket(driver)[i][5].strip())

        # print(check_ticket(driver))

        send_notification(TOKEN, ID_CHAT,  view_message(id_tickets, contatos, tempos))
        
    finally:
        driver_manager.quit_driver()  # Certifique-se de fechar o WebDriver no final

if __name__ == "__main__":
    main()

