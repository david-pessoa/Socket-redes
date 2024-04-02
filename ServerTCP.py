######################### IMPORTANTE! ###############################
#                   EXECUTE O ServerTCP.py primeiro!
######################### IMPORTANTE! ###############################

import socket #importa modulo socket
 
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
    #dados retidados da mensagem recebida
    data = conn.recv(TAMANHO_BUFFER).decode("UTF-8") #Recebe resposta do cliente
    if data: 
        print ("Cliente:", data)
        if data != "QUIT":
            answer = input("Servidor: ")
            conn.send(answer.encode("UTF-8"))  # envia dados recebidos em letra maiuscula
            if answer == "QUIT":
                break
        else:
            break
conn.close()

