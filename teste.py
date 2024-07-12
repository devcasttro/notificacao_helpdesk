def view_message(id_tickets, contato, tempo):
    # Inicializa a variável texto
    texto = ""
    
    for ticket in id_tickets:
        # Adiciona cada ticket ao texto
        texto += f"""- Ticket {ticket} de {contato}, aberto há {tempo} <br>
        """
    
    # Cria o cabeçalho, ajustando dinamicamente a quantidade de tickets
    cabecalho = f"""
        Prezados,

        Foram encontrados <b>{len(id_tickets)} tickets em aberto</b>, sendo: \n
        """
    
    # Concatena o cabeçalho com o texto dos tickets
    message = cabecalho + texto

    return message

# id = [1, 2, 3, 4]

# print(view_message(id))