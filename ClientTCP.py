######################### IMPORTANTE! ###############################
#                   EXECUTE O ServerTCP.py primeiro!
######################### IMPORTANTE! ###############################
# David Varão Lima Bentes Pessoa  10402647
# Pedro Nomura

import socket
    #TODO: Testar todos os casos
    #TODO: Implementar arte ASCII
    #TODO: Tentar limpar a tela

TCP_IP = '192.168.0.5' # endereço IP do cliente
TCP_PORTA = 8080      # porta disponibilizada pelo servidor
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
    while cliente_choice != "1" and cliente_choice != "2" and cliente_choice != "3" and cliente_choice != "QUIT":
        print("Insira um número de 1 a 3 ou QUIT para sair")
        cliente_choice = input("Escolha: ") # Cliente insere mensagem
    if cliente_choice == "QUIT": #Se o cliente digitou QUIT sai do chat
        print("Encerrando conexão.....")
        break
    
    cliente.send(cliente_choice.encode('UTF-8')) # Mensagem é enviada ao servidor
    cliente_choice = int(cliente_choice)

    # recebe dados do servidor 
    data, addr = cliente.recvfrom(1024) #Cliente recebe resposta do servidor
    server_choice = data.decode("UTF-8") #Decodifica mensagem
    if server_choice == "QUIT" or server_choice == "": # Se a resposta do servidor foi QUIT sai do chat
        print("\nSeu oponente desistiu da partida")
        print("Jogo encerrado.")
        break
    server_choice = int(server_choice)

    # Pedra Pedra
    if cliente_choice == 1 and server_choice == 1:
        print("\n\nVocê: Pedra")
        print("Oponente: Pedra")
        print("Empate")

    # Pedra Papel
    elif cliente_choice == 1 and server_choice == 2:
        print("\n\nVocê: Pedra")
        print("Oponente: Papel")
        print("Você perdeu!")
        placar[1] += 1
    
    # Pedra Tesoura
    elif cliente_choice == 1 and server_choice == 3:
        print("\n\nVocê: Pedra")
        print("Oponente: Tesoura")
        print("Você ganhou!")
        placar[0] += 1
    
    # Papel Pedra
    elif cliente_choice == 2 and server_choice == 1:
        print("\n\nVocê: Papel")
        print("Oponente: Pedra")
        print("Você ganhou!")
        placar[0] += 1
    
    # Papel Papel
    elif cliente_choice == 2 and server_choice == 2:
        print("\n\nVocê: Papel")
        print("Oponente: Papel")
        print("Empate")
    
    # Papel Tesoura
    elif cliente_choice == 2 and server_choice == 3:
        print("\n\nVocê: Papel")
        print("Oponente: Tesoura")
        print("Você perdeu!")
        placar[1] += 1
    
    # Tesoura Pedra
    elif cliente_choice == 3 and server_choice == 1:
        print("\n\nVocê: Tesoura")
        print("Oponente: Pedra")
        print("Você perdeu!")
        placar[1] += 1
    
    # Tesoura Papel
    elif cliente_choice == 3 and server_choice == 2:
        print("\n\nVocê: Tesoura")
        print("Oponente: Papel")
        print("Você ganhou!")
        placar[0] += 1
    
    # Tesoura Tesoura
    elif cliente_choice == 3 and server_choice == 3:
        print("\n\nVocê: Tesoura")
        print("Oponente: Tesoura")
        print("Empate")

    else:
        print("Houve algum erro")
        print("Encerrando conexão.....")
        break

# fecha conexão com servidor
cliente.close()
