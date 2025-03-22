from socket import *

class Client:
    def __init__(self):
        serverName = 'localhost'
        serverPort = 12000
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((serverName, serverPort))

    def sendReq(self):
        req = '+,10,11'
        self.clientSocket.send(req.encode('utf-8'))
        res = self.clientSocket.recv(1024)
        #print(f"Resposta do servidor: {res.decode('utf-8')}")
        self.clientSocket.close()
