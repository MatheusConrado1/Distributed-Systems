from socket import *

class Client:
    def __init__(self):
        serverName = 'localhost'
        serverPort = 12000
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((serverName, serverPort))

    def sendReq(self, req):
        self.clientSocket.send(req.encode('utf-8'))
        res = self.getRes()
        return res

    def getRes(self):
        res = self.clientSocket.recv(1024)
        self.clientSocket.close()
        print(res)
        print(res.decode('utf-8'))
        return (res.decode('utf-8'))