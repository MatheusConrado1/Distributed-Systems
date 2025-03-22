import time
from calculadora import calcular
from calculadora_s import calcular_s
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(100)

print("Servidor iniciado na porta", serverPort)

while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        try:
            sentence = connectionSocket.recv(1024)
            if not sentence:
                continue

            text = sentence.decode('utf-8')
            parts = text.split(',')
            opp = parts[0]

            if opp in ['+', '-', '/', '*']:
                result = calcular(text)
            elif opp in ['^', 'sqr']:
                result = calcular_s(text)
            else:
                result = "Erro: operação inválida"

            time.sleep(0.1)

            connectionSocket.send(str(result).encode('utf-8'))

        except Exception as e:
            pass

        finally:
            connectionSocket.close()

    except Exception as e:
        pass
