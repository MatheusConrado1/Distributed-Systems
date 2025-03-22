from socket import *
from ProxyCalc import ProxyCalc
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
ProxyCalc = ProxyCalc()

while True:
    sentence = input('Input: (OPP, OP1, OP2)\n')
    if(sentence == 'quit'): break
    res = ProxyCalc.treat_response(sentence)
    modifiedSentence = res
    text = modifiedSentence
    print("From Server:", text)

clientSocket.close()