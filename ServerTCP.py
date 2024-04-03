######################### IMPORTANTE! ###############################
#                   EXECUTE O ServerTCP.py primeiro!
######################### IMPORTANTE! ###############################

import socket #importa modulo socket
    #TODO: Testar todos os casos
    #TODO: Implementar arte ASCII
    #TODO: Tentar limpar a tela
 
TCP_IP = '192.168.0.5' # endereço IP do servidor 
TCP_PORTA = 3225     # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024     # definição do tamanho do buffer
 
def show_placar(placar):
    print(f"\t\tCliente {placar[0]}     X      Servidor {placar[1]}\n\n")

# Criação de socket TCP
# SOCK_STREAM, indica que será TCP.
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP e porta que o servidor deve aguardar a conexão
servidor.bind((TCP_IP, TCP_PORTA))

#Define o limite de conexões. 
servidor.listen(1)

placar = [0, 0] # Posicão 0 cliente / Posição 1 servidor
print(f"Esperando um oponente..............") 
# Aceita conexão 
conn, addr = servidor.accept()
print ('Endereço conectado:', addr) #Exibe IP da máquina conectada
while 1:
    show_placar(placar)
    print("Escolha entre:")
    print("1 Pedra")
    print("2 Papel")
    print("3 Tesoura")

    server_choice = input("Escolha: ") # Servidor insere mensagem
    while server_choice != "1" and server_choice != "2" and server_choice != "3" and server_choice != "QUIT":
        print("Insira um número de 1 a 3 ou QUIT para sair")
        server_choice = input("Escolha: ") # Servidor insere mensagem
    if server_choice == "QUIT": #Se o servidor digitou QUIT sai do chat
        print("Encerrando conexão.....")
        break

    #dados retidados da mensagem recebida
    cliente_choice = conn.recv(TAMANHO_BUFFER).decode("UTF-8") #Recebe resposta do cliente
    if cliente_choice == "QUIT":
        print("Seu oponente desistiu da partida")
        print("Jogo encerrado.")
    else:
        
        conn.send(server_choice.encode("UTF-8"))  # envia dados recebidos em letra maiuscula
        server_choice = int(server_choice)
        cliente_choice = int(cliente_choice)

        # Pedra Pedra
        if cliente_choice == 1 and server_choice == 1:
            print("\n\n Você: Pedra")
            print("Oponente: Pedra")
            print("Empate")

        # Papel Pedra
        elif cliente_choice == 1 and server_choice == 2:
            print("\n\n Você: Papel")
            print("Oponente: Pedra")
            print("Você ganhou!")
            placar[1] += 1

        # Tesoura Pedra
        elif cliente_choice == 1 and server_choice == 3:
            print("\n\n Você: Tesoura")
            print("Oponente: Pedra")
            print("Você perdeu!")
            placar[0] += 1

        # Pedra Papel
        elif cliente_choice == 2 and server_choice == 1:
            print("\n\n Você: Pedra")
            print("Oponente: Papel")
            print("Você perdeu!")
            placar[0] += 1

        # Papel Papel
        elif cliente_choice == 2 and server_choice == 2:
            print("\n\n Você: Papel")
            print("Oponente: Papel")
            print("Empate")

        # Tesoura Papel
        elif cliente_choice == 2 and server_choice == 3:
            print("\n\n Você: Tesoura")
            print("Oponente: Papel")
            print("Você ganhou!")
            placar[1] += 1

        # Pedra Tesoura
        elif cliente_choice == 3 and server_choice == 1:
            print("\n\n Você: Pedra")
            print("Oponente: Tesoura")
            print("Você ganhou!")
            placar[1] += 1

        # Papel Tesoura
        elif cliente_choice == 3 and server_choice == 2:
            print("\n\n Você: Papel")
            print("Oponente: Tesoura")
            print("Você perdeu!")
            placar[0] += 1

        # Tesoura Tesoura
        elif cliente_choice == 3 and server_choice == 3:
            print("\n\n Você: Tesoura")
            print("Oponente: Tesoura")
            print("Empate")

        else:
            print("Houve algum erro")
            print("Encerrando conexão.....")
            break
conn.close()

