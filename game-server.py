import socket
import random
import time
from multiprocessing import Process


# List for sending drawing things to clients.
itemsList = ['Face', 'House', 'Triangle', 'Fish', 'Book']

# Variables for setting the connection address.
serverIp = 'localhost'
serverPort = 25565

# Other variables
player2points = 0
player1points = 0
randomInList = 'filler'

timesWinnerQueried = 0
timesItemsQueried = 0

drawingTopic = ''

connectionData = None

# Start listening to connections
socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObject.bind((serverIp, serverPort))
socketObject.listen(25)
print('Socket created on port ' + str(serverPort))

# Returns the winner
def getPoints():
    if player1points > player2points:
        return 'Player 1 wins!'
    if player2points > player1points:
        return 'Player 2 wins!'
    if player2points == player1points:
        return 'It''s a tie!'
        
# Main function thats starts the main listener
def main():
    listener1 = Process(target=mainListener)
    
    listener1.start()

# Try to return the winner after both people have voted
def tryGet():
    global connectionData
    global timesWinnerQueried

    while not timesWinnerQueried >1:
        time.sleep(1)

    if timesWinnerQueried > 1:
            connectionData.send(getPoints().encode())
            print('The game has ended! The server will now stop.')
            quit()
        
# Listens for data
def mainListener():
    global timesWinnerQueried
    global timesItemsQueried
    global drawingTopic
    global connectionData
    
    while True :
        (connection, address) = socketObject.accept()
        data = connection.recv(2048)
       
        if 'get-items' in data.decode():
            if timesItemsQueried > 0:
                connection.send(drawingTopic.encode())
            else:
                randomInList = itemsList[random.randrange(0, 4)]
                drawingTopic = randomInList
                connection.send(randomInList.encode())
                timesItemsQueried = timesItemsQueried + 1
      
        if '1, ' in data.decode():
            timesWinnerQueried = timesWinnerQueried + 1
            if timesWinnerQueried == 2:
                connection.send(getPoints().encode())
                connection.close()
                listener2 = Process(target=tryGet)
                listener2.start() 
            else:
                player2points = data.decode().replace('1, ', '')        
                connectionData = connection
                connection.send(b'none-yet')
             

        if '2, ' in data.decode():
            timesWinnerQueried = timesWinnerQueried + 1
            if timesWinnerQueried == 2:
                connection.send(getPoints().encode())
                connection.close()
                listener2 = Process(target=tryGet)
                listener2.start() 
            else:
                player1points = data.decode().replace('2, ', '')  
                connectionData = connection
                connection.send(b'none-yet')
# Starts the program
main()
