import time
from calculadora import calcular
from calculadora_s import calcular_s
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while 1:
     connectionSocket, addr = serverSocket.accept()
     print(f"Connected to {addr}")
     while 1:
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
            print(f"Erro no processamento: {e}")
            break

     print("Closed connection")
     connectionSocket.close()