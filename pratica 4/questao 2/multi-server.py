from calculadora import Calculadora
from calculadora_s import Calculadora_Science
from socket import *
from threading import Thread
import time

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(100)

Calc = Calculadora()
Calculadora_Sci = Calculadora_Science()

def handle_client(connectionSocket, addr):
    while True:
        try:
            sentence = connectionSocket.recv(1024)
            if not sentence:
                break
            text = sentence.decode('utf-8')
            parts = text.split(',')
            
            if len(parts) < 2:
                connectionSocket.send("Erro: entrada mal formulada".encode('utf-8'))
                continue
            
            opp = parts[0].strip()
            
            if opp in ['+', '-', '/', '*']:
                if len(parts) == 3:
                    result = Calc.calcular(text)
                else:
                    result = "Erro: formato incorreto para operação básica"
            
            elif opp in ['^', 'sqr']:
                result = Calculadora_Sci.calcular_s(text)
            
            else:
                result = "Erro: operação inválida"

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
