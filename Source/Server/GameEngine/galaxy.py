#!/usr/bin/env python
# vi: spell spl=en


import argparse
import cPickle as p
from elements.game import Game
from elements.creation_options import CreationOptions

parser = argparse.ArgumentParser()
# parser.add_argument( '--dump',   help="Dump game data", metavar="GAME_NAME" )
parser.add_argument( 'command',    help="create | run | dump | map" )
parser.add_argument( 'game_name',  help="Name of the game" )

args = parser.parse_args()

if args.command:
    print "Command ", args.command
if args.game_name:
    print "Gamename ", args.game_name

if args.command == 'create':
    game = Game()
    game.create( CreationOptions() )
    with open('test.pickle', 'w') as f:
        p.dump( game, f )
elif args.command == 'run' :
    with open('test.pickle', 'r') as f:
        game = p.load(f)
        game.turn[0].report()
elif args.command == 'map':
    with open('test.pickle', 'r') as f:
        game = p.load( f )
        with open('map.csv', 'w') as mf:
            game.map( mf )

