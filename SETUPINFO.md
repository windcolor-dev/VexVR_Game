# Setup Info

One player (or someone else) runs the server with game-server.py. Two players get the files in the player1 or player2 directory. 
You will need to setup the variables in voting/get-item scripts so that they connect to the correct address and port. 
Both people launch the get-items.py script to get the topic. (The game-server.py script will need to be started
for this to work) Then, after players are done drawing and have seen their opponent's drawing, they launch the vote
script (voting.py) once they have set the points variable to the amount of points they think their opponent's drawing deserves.
(Scale of 1-3) The server needs to be restarted after each game.


