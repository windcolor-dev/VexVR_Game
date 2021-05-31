import socket, time

# Set this to your vote.
points = 3

# Don't change these unless
# you are connecting to a 
# different server.
socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverIp = 'localhost'
serverPort = 25565

# Don't change this.
data = None

def main():
    global data
    global points
    
    print('You are Player 2.')
    print('You scored Player 1' + "'" + 's drawing with ' + str(points) + ' points.')
    socketObject.connect((serverIp, serverPort))
    pointsString = '2, ' + str(points)
    pointsByte = pointsString.encode()
    socketObject.send(pointsByte)
    
    data = socketObject.recv(2048)      
    if 'none-yet' in data.decode():
        data = socketObject.recv(2048)  
                    
        print(data.decode())  
    else:
        print(data.decode())


main()
