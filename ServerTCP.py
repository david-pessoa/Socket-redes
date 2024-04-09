######################### IMPORTANTE! ###############################
#                   EXECUTE O ServerTCP.py primeiro!
######################### IMPORTANTE! ###############################
# David Varão Lima Bentes Pessoa  10402647
# Pedro Nomura Picchioni  10401616

from ASCII_art import *
import socket #importa modulo socket
    #TODO: Tentar limpar a tela
 
SERVER_IP = '192.168.0.2' # endereço IP do servidor
CLIENTE_IP = '192.168.0.2'
PORTA_TCP = 4040     # porta disponibilizada pelo servidor
PORTA_UDP = 6667
TAMANHO_BUFFER = 1024     # definição do tamanho do buffer
 
def show_placar(placar):
    print(f"\t\tServidor {placar[1]}     X      Cliente {placar[0]}\n\n")

# Criação de socket TCP
# SOCK_STREAM, indica que será TCP.
servidorTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP e porta que o servidor deve aguardar a conexão
servidorTCP.bind((SERVER_IP, PORTA_TCP))

#Define o limite de conexões. 
servidorTCP.listen(1)

placar = [0, 0] # Posicão 0 cliente / Posição 1 servidor
print(f"Esperando um oponente..............")

# Aceita conexão 
conn, addr = servidorTCP.accept()
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
        print("Encerrando jogo")
        break

    #dados retidados da mensagem recebida
    cliente_choice = conn.recv(TAMANHO_BUFFER).decode("UTF-8") #Recebe resposta do cliente
    if cliente_choice == "QUIT" or cliente_choice == "":
        print("\nSeu oponente desistiu da partida")
        print("Jogo encerrado.")
        break
    else:
        
        conn.send(server_choice.encode("UTF-8"))  # envia dados recebidos em letra maiuscula
        server_choice = int(server_choice)
        cliente_choice = int(cliente_choice)

        print(indica)
        # Pedra Pedra
        if cliente_choice == 1 and server_choice == 1:
            print(pedra_pedra)
            print("Empate")

        # Papel Pedra
        elif cliente_choice == 1 and server_choice == 2:
            print(papel_pedra)
            print("Você ganhou!")
            placar[1] += 1

        # Tesoura Pedra
        elif cliente_choice == 1 and server_choice == 3:
            print(tesoura_pedra)
            print("Você perdeu!")
            placar[0] += 1

        # Pedra Papel
        elif cliente_choice == 2 and server_choice == 1:
            print(pedra_papel)
            print("Você perdeu!")
            placar[0] += 1

        # Papel Papel
        elif cliente_choice == 2 and server_choice == 2:
            print(papel_papel)
            print("Empate")

        # Tesoura Papel
        elif cliente_choice == 2 and server_choice == 3:
            print(tesoura_papel)
            print("Você ganhou!")
            placar[1] += 1

        # Pedra Tesoura
        elif cliente_choice == 3 and server_choice == 1:
            print(pedra_tesoura)
            print("Você ganhou!")
            placar[1] += 1

        # Papel Tesoura
        elif cliente_choice == 3 and server_choice == 2:
            print(papel_tesoura)
            print("Você perdeu!")
            placar[0] += 1

        # Tesoura Tesoura
        elif cliente_choice == 3 and server_choice == 3:
            print(tesoura_tesoura)
            print("Empate")

        else:
            print("Houve algum erro")
            print("Encerrando jogo.........")
            break

# Encerra conexão TCP com o cliente
conn.close()

servidor_UDP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# IP e porta que o servidor deve aguardar a conexão
servidor_UDP.bind((SERVER_IP, PORTA_UDP)) 

# Inicia chat após o jogo
print("\t\tCHAT\n\n")
while True:
    mensagem_cliente, addr = servidor_UDP.recvfrom(1024)
    mensagem_cliente = mensagem_cliente.decode("UTF-8")
    if mensagem_cliente != "" and mensagem_cliente != "QUIT":
       print("Cliente: ", mensagem_cliente)
    else:
        print("Cliente saiu do chat. Encerrando..............")
        break

    mensagem_servidor = input("Envie uma mensagem: ").encode('UTF-8')
    if mensagem_servidor == "QUIT":
        print("Encerrando chat...........")
        break
    servidor_UDP.sendto(mensagem_servidor, (CLIENTE_IP, PORTA_UDP))
