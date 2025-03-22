from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = input('Input: (OPP, OP1, OP2)')
opp, op1, op2 = sentence.split(',')

while(1):
    sentence = input('Input: (OPP, OP1, OP2)')
    opp, op1, op2 = sentence.split(',') 
    if opp in ['+', '-', '*', '/'] and (opp != '/' or float(op2) != 0):
        try:
            float(op1)
            float(op2)
            clientSocket.send(sentence.encode('utf-8'))
            break
        except ValueError:
            print("Sentença mal formulada, tente novamente")
    else:
        print("Sentença mal formulada, tente novamente")

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode("utf-8"))
clientSocket.close()
