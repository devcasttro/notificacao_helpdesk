def view_message(id_tickets, contato, tempo):
    # Inicializa a variável texto
    texto = ""
    
    for i in range(len(id_tickets)):
        # Adiciona cada ticket ao texto
        texto += f"""
        - Ticket {id_tickets[i]} de {contato[i]}, aberto há {tempo[i]}
        """
    
    # Cria o cabeçalho, ajustando dinamicamente a quantidade de tickets
    cabecalho = f"""
    Prezados,

    Foram encontrados <b>{len(id_tickets)} tickets em aberto</b>, sendo: \n
        """
    
    # Concatena o cabeçalho com o texto dos tickets
    message = cabecalho + texto

    return message