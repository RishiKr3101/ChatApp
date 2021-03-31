import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.1.1"
        self.port =5555
        self.addr = (self.server, self.port)
        self.msg = self.connect()
    
    def getMsg(self):
        return self.msg
        

    def connect(self):
        try:
            self.client.connect(self.addr)
            g=self.client.recv(2048)
            print("yuss")
            return g
        
        except:
            print ("error")
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        
        except socket.error as e:
            print(e)
    
    
