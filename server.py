import socket
  
# import threading library
import threading
  
# Choose a port that is free
PORT = 5000
  
# An IPv4 address is obtained
# for the server.   
SERVER = socket.gethostbyname(socket.gethostname())
  
# Address is stored as a tuple
ADDRESS = (SERVER, PORT)
  
# the format in which encoding
# and decoding will occur
FORMAT = "utf-8"
  
# Lists that will contains
# all the clients connected to 
# the server and their names.
clients, names = [], []
  
# Create a new socket for
# the server 
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
  
# bind the address of the 
# server to the socket 
server.bind(ADDRESS)
  
# function to start the connection
def startChat():
    
    print("server is working on " + SERVER)
      
    server.listen()
      
    while True:
        
       
        conn, addr =  server.accept()
        conn.send("NAME".encode(FORMAT))
          

        name = conn.recv(1024).decode(FORMAT)
          
    
        names.append(name)
        clients.append(conn)
          
        print(f"Name is :{name}")
          
        broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))
          
        conn.send('Connection successful!'.encode(FORMAT))
          
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