from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = input('Input: (OPP, OP1, OP2)')
opp, op1, op2 = sentence.split(',')

while(1):
    if(opp == '+' or opp == '-' or opp == '*' or opp == '/'):
        if(float(op1) and float(op2)):
            clientSocket.sendto(sentence.encode("utf-8"),(serverName, serverPort))
            break
    else:
        sentence = input('Input: (OPP, OP1, OP2)')
        opp, op1, op2 = sentence.split(',')

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode("utf-8"))
clientSocket.close()
