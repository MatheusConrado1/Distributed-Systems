from TcpClient import Client
import threading
import time

def client_thread():
    client = Client()
    client.sendReq()

clients = []

initial_time = time.time()

for i in range(100):
    thread = threading.Thread(target=client_thread)
    clients.append(thread)

cont_success = 0

for client in clients:
    client.start()

for client in clients:
    client.join()

final_time = time.time()

var_time = final_time - initial_time
print(f"Tempo de execução: {var_time:.2f}s")
