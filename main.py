from controller.controller_webdriver_manager import WebDriverManager
from controller.controller_login import go_login
from controller.controller_check_ticket import check_ticket
from controller.controller_send_notification import send_notification
from view.view_message import view_message
from dotenv import load_dotenv
from time import sleep
import os

TOKEN = os.getenv("TOKEN")
ID_CHAT = os.getenv("ID_CHAT")
id_tickets = []
contatos = []
tempos = []
update_time = 10 # Tempo de espera em segundos para uma nova verificação de chamados aberto

def main():

    driver_manager = WebDriverManager()
    driver = driver_manager.start_driver()


    go_login(driver)

    while True:
        try:

            is_ticket = check_ticket(driver)

            # Intera entre os dados dos chamados disponiveis para criar uma lista
            for i in range(len(is_ticket)):
                
                old_id_ticket = check_ticket(driver)[i][0].replace("BREVES - TIC", "") # Ajusta o id para remover a localidade
                id_tickets.append(old_id_ticket.strip())
                contatos.append(is_ticket[i][2].strip())
                tempos.append(is_ticket[i][5].strip())

            send_notification(TOKEN, ID_CHAT,  view_message(id_tickets, contatos, tempos))

            sleep(update_time) # aguarda o tempo definido para uma nova consulta

        except IndexError as e:

            if e != "list index out of range":
                print(f'Error: {e}')
                send_notification(TOKEN, ID_CHAT, f'ERROR: {e}')
            else:
                print('Você não tem chamado em aberto no momento.')
            
            sleep(60) # aguarda o tempo definido para uma nova consulta


if __name__ == "__main__":
    main()

