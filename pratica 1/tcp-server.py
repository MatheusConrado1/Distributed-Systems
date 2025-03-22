import time
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while 1:
     connectionSocket, addr = serverSocket.accept()
     sentence = connectionSocket.recv(1024)
     text = sentence.decode('utf-8')
     opp, op_1, op_2 = text.split(',')
     op1 = float(op_1)
     op2 = float(op_2)

     if opp in ['+', '-', '*', '/'] and (opp != '/' or float(op2) != 0):
          try:
               float(op_1)
               float(op_2)
               if(opp == '+'):
                    result = op1 + op2
               elif(opp == '-'):
                    result = op1 - op2
               elif(opp == '*'):
                    result = op1 * op2 
               elif(opp == '/'):
                    result = op1 / op2
          except ValueError:
               error = "Sentença mal formulada"
               connectionSocket.send(error.enconde('utf-8'))
     else:
          error = "Sentença mal formulada"
          connectionSocket.send(error.enconde('utf-8'))
  
     if(result):
          connectionSocket.send(str(result).encode('utf-8'))
          connectionSocket.close()