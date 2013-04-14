Architecture
============

The game has a client server architecture.

The game master runs the server.
Each player runs a client.

The server part consists of a game engine and a web server.  The game engine
creates new games and runs turns.  Game data is stored in a SQL database
(sqlite).

The webserver serves the client-code and turn data for a particular player.
The webserver at start up of a client, provides the client with enough
information for it to run off-line.

The player uses the client to view its current situation and to create orders
for the coming turn.


vi: spell spl=en ft=markdown
