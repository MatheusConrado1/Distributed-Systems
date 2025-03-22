from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    sentence = input(">>")
    if (sentence == "exit"):
        break

    clientSocket.send(sentence.encode('utf-8'))
    receivedResponse = clientSocket.recv(1024)
    text = receivedResponse.decode('utf-8')
    print("<<", text)

clientSocket.close()
