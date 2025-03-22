from Calculadora import Calculadora
from Calculadora_s import Calculadora_Science
from socket import *
from threading import Thread
from Despachante import Despachante
import time

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(100)

Calc = Calculadora()
Calculadora_Sci = Calculadora_Science()
Despachante = Despachante()

def handle_client(connectionSocket, addr):
    while True:
        try:
            sentence = connectionSocket.recv(1024)
            if not sentence:
                break
            text = sentence.decode('utf-8')
            
            result = Despachante.invoke(text)

            time.sleep(0.1)
            connectionSocket.send(str(result).encode('utf-8'))
        except Exception as e:
            print(f"Erro: {e}")
            connectionSocket.send("Erro no processamento".encode('utf-8'))
            break

    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    client_thread = Thread(target=handle_client, args=(connectionSocket, addr))
    client_thread.start()
