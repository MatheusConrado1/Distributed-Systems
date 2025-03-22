import time
from calculadora import calcular
from calculadora_s import calcular_s
from socket import *
from threading import Thread

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(100)
# print("The server is ready to receive")

def handle_client(connectionSocket, addr):
    # print(f"Connected to {addr}")
    while True:
        try:
            sentence = connectionSocket.recv(1024)
            if not sentence:
                break
            text = sentence.decode('utf-8')
            parts = text.split(',')
            opp = parts[0]

            if opp in ['+', '-', '/', '*']:
                result = calcular(text)
            elif opp in ['^', 'sqr']:
                result = calcular_s(text)
            else:
                result = "Erro: operação inválida"

            connectionSocket.send(str(result).encode('utf-8'))
        except Exception as e:
            # print(f"Erro no processamento com {addr}: {e}")
            break

    # print(f"Closed connection with {addr}")
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    client_thread = Thread(target=handle_client, args=(connectionSocket, addr))
    client_thread.start()
