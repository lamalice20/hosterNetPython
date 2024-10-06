import socket 

class socketChatClient:
    def __init__(self, host: str, port: int):
        self.adress = (host, port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STEAM)

    def startChatClient(self):
        self.client.connect(self.adress)
        
        while True:
            self.client.sendall(bytes(input('Msg: '), "utf-8"))
            msg = self.client.recv(1024).decode("utf-8")
            if msg == "stop":
                self.client.close()
                break
            else:
                print(msg)
