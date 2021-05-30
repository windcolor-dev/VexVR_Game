import socket

# Don't change these unless
# you are connecting to a 
# different server.
socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverIp = 'localhost'
serverPort = 25565

def main():
    socketObject.connect((serverIp, serverPort))
    socketObject.send(b'get-items')
    data = socketObject.recv(1024)
    print('The drawing theme is ' + data.decode() + '!')
    quit()
main()
    
