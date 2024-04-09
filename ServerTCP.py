######################### IMPORTANTE! ###############################
#                   EXECUTE O ServerTCP.py primeiro!
######################### IMPORTANTE! ###############################
from ASCII_art import *
import socket #importa modulo socket
 
TCP_IP = '192.168.0.3' # endereço IP do servidor 
TCP_PORTA = 3225     # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024     # definição do tamanho do buffer
 
def show_placar(placar):
    print(f"\t\Servidor {placar[1]}     X      Cliente {placar[0]}\n\n")

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
    flag = False
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
        conn.send(server_choice.encode("UTF-8"))
        flag = True

    conn.send(server_choice.encode("UTF-8")) #Envia mensagem para o cliente
    #dados retidados da mensagem recebida
    cliente_choice = conn.recv(TAMANHO_BUFFER).decode("UTF-8") #Recebe resposta do cliente
    if cliente_choice == "QUIT" or cliente_choice == "":
        print("\nSeu oponente desistiu da partida")
        print("Jogo encerrado.")
        break
    if flag:
        break

    else:
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
            print("Encerrando conexão.....")
            break

print("Iniciando chat pós jogo")
while 1:
    # dados retidados da mensagem recebida
    data = conn.recv(TAMANHO_BUFFER)
    if data:
        if data.decode("UTF-8") == "QUIT":
            break
        print("Mensagem recebida do cliente:", data.decode("UTF-8"))
        resp = str(input("Mensagem para o cliente: "))
        conn.send(resp.encode("UTF-8"))  # envia dados recebidos em letra maiuscula
        if resp == "QUIT":
            break
print("Chat encerrado")
conn.close()
