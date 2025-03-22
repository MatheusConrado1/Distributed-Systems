from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    text = message.decode("utf-8")
    opp, op_1, op_2 = text.split(',')

    op1 = float(op_1)
    op2 = float(op_2)

    if(opp == '+'):
        result = op1 + op2
    elif(opp == '-'):
        result = op1 - op2
    elif(opp == '*'):
        result = op1 * op2   
    elif(opp == '/'):
        result = op1 / op2

    modifiedMessage = str(result)
    serverSocket.sendto(modifiedMessage.encode("utf-8"), clientAddress)
