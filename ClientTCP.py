######################### IMPORTANTE! ###############################
#                   EXECUTE O ServerTCP.py primeiro!
######################### IMPORTANTE! ###############################
# David Varão Lima Bentes Pessoa  10402647
# Pedro Nomura

import socket #importa modulo socket

TCP_IP = '192.168.0.5' # endereço IP do cliente
TCP_PORTA = 3225      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024

def show_placar(placar):
    print(f"\t\tCliente {placar[0]}     X      Servidor {placar[1]}\n\n")

# Criação de socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor em IP e porta especifica 
cliente.connect((TCP_IP, TCP_PORTA))

placar = [0, 0] # Posicão 0 cliente / Posição 1 servidor
while True:
    show_placar(placar)
    print("Escolha entre:")
    print("1 Pedra")
    print("2 Papel")
    print("3 Tesoura")

    cliente_choice = input("Escolha: ") # Cliente insere mensagem
    if cliente_choice == "QUIT": #Se o cliente digitou QUIT sai do chat
        break
    cliente_choice = int(cliente_choice)
    
    cliente.send(cliente_choice.encode('UTF-8')) # Mensagem é enviada ao servidor


    
    # recebe dados do servidor 
    data, addr = cliente.recvfrom(1024) #Cliente recebe resposta do servidor
    server_choice = data.decode("UTF-8") #Decodifica mensagem
    if data == "QUIT": # Se a resposta do servidor foi QUIT sai do chat
        break
    server_choice = int(server_choice)

    # Pedra Pedra
    if cliente_choice == 1 and server_choice == 1:
        print("\n\n Você: Pedra")
        print("Oponente: Pedra")
        print("Empate")

    # Pedra Papel
    elif cliente_choice == 1 and server_choice == 2:
        print("\n\n Você: Pedra")
        print("Oponente: Papel")
        print("Você perdeu!")
        placar[1] += 1
    
    # Pedra Tesoura
    elif cliente_choice == 1 and server_choice == 3:
        print("\n\n Você: Pedra")
        print("Oponente: Tesoura")
        print("Você ganhou!")
        placar[0] += 1


    #TODO: Continuar ifs para o cliente e servidor
    #TODO: Testar código
    

    # Papel Pedra
    # Papel Papel
    # Papel Tesoura

    # Tesoura Pedra
    # Tesoura Papel
    # Tesoura Tesoura



# fecha conexão com servidor
cliente.close()
