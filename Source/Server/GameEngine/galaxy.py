#!/usr/bin/env python
# vi: spell spl=en


import argparse
import cPickle as p
from elements.game import Game

parser = argparse.ArgumentParser()
# parser.add_argument( '--dump',   help="Dump game data", metavar="GAME_NAME" )
parser.add_argument( 'command',    help="create | run | dump" )
parser.add_argument( 'game_name',  help="Name of the game" )

args = parser.parse_args()

if args.command :
    print "Command ", args.command
if args.game_name :
    print "Gamename ", args.game_name

if args.command == 'create' :
    game = Game()
    game.create( 'foo' )
    with open('test.pickel', 'w') as f :
        p.dump( game, f )
elif args.command == 'run' :
    with open('test.pickel', 'r') as f :
        game = p.load(f)
        print game.turn[0].universe.planets
