from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    sentence = input('Input: (OPP, OP1, OP2)\n')
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

modifiedSentence = clientSocket.recv(1024)
text = modifiedSentence.decode('utf-8')
print("From Server:", text)
clientSocket.close()