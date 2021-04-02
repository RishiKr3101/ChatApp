import socket
  
<<<<<<< HEAD

import threading

PORT = 5000

SERVER = socket.gethostbyname(socket.gethostname())

ADDRESS = (SERVER, PORT)

=======
import threading
  
PORT = 5000
  
   
SERVER = socket.gethostbyname(socket.gethostname())
  

ADDRESS = (SERVER, PORT)
  
>>>>>>> b0d886abb6412d04f36032a62fe0973be9acd998
FORMAT = "utf-8"
  

clients, names = [], []
  
<<<<<<< HEAD
=======

>>>>>>> b0d886abb6412d04f36032a62fe0973be9acd998
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
  

server.bind(ADDRESS)
  

def startChat():
    
    print("SERVER STARTED at " + SERVER)
    print("WAITING FOR CONNECTIONS:")
      
    server.listen()
      
    while True:
        
       
        conn, addr =  server.accept()
        conn.send("NAME".encode(FORMAT))
          

        name = conn.recv(1024).decode(FORMAT)
          
    
        names.append(name)
        clients.append(conn)
          
        print(f"Name is :{name}")
          
        broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))
          
        conn.send('[CONNECTED]'.encode(FORMAT))
          
        thread = threading.Thread(target = handle,
                                  args = (conn, addr))
        thread.start()
          
        print(f"active connections {threading.activeCount()-1}")
  
def handle(conn, addr):
    
    print(f"new connection {addr}")
    connected = True
      
    while connected:
        message = conn.recv(1024)
          
        broadcastMessage(message)
      
    conn.close()
  

def broadcastMessage(message):
    for client in clients:
        client.send(message)
  

startChat()
