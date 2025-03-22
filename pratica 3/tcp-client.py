from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    sentence = input('Input: (OPP, OP1, OP2) or (OPP, OP1)\n')
    if(sentence == 'quit'): break
    clientSocket.send(sentence.encode('utf-8'))
    modifiedSentence = clientSocket.recv(1024)
    text = modifiedSentence.decode('utf-8')
    print("From Server:", text)   

clientSocket.close()