#Architecture

The game has a client server architecture.

The game master runs the server.  Each player runs a client.

The server part consists of a game engine and a web server.  The game engine
creates new games and runs turns.

The web server serves the client-code and turn data for each particular
player.

The webserver at start up of a client, provides the client with enough
information for it to run off-line.

The player uses the client to view its current situation and to create orders
for the coming turn.

When finished the orders are posted to the webserver and stored on disk.

A few times a week the game engines reads all orders and runs a turn.


##Client

TODO

##Technology

Client and server exchange data in JSON format.

The game server stores game data in python pickle format.

The web server and game engine are written in Python.

The client is written in Javascript.


##Limits

Why have limits?  They make it easier to design and implement an application.
They also encourage more creativity from the players.

Current limits:

1. The size of a planet is in the range [10,2000].
2. The size of the galaxy is in the range [50, 5000].
3. Names of game elements are limited to 32 characters.


vi: spell spl=en ft=markdown
