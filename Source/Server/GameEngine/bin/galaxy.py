#!/usr/bin/env python
# vi: spell spl=en

"""
galaxy

Usage:
    galaxy create <name>
    galaxy run <name>
    galaxy map <name>
    galaxy report <name>
"""

import argparse
import random
import pickle as p
from ngengine.game import Game
from ngengine.creation_options import CreationOptions
from docopt import docopt

def old():
    parser = argparse.ArgumentParser()
    # parser.add_argument( '--dump',   help="Dump game data", metavar="GAME_NAME" )
    parser.add_argument( 'command',    help="create | run | dump | map | report" )
    parser.add_argument( 'game_name',  help="Name of the game" )

    # This makes debugging much easier.
    random.seed(11111967)

    args = parser.parse_args()

    if args.command:
        print ("Command " + args.command)
    if args.game_name:
        print ("Gamename {}".format(args.game_name))

    if args.command == 'create':
        game = Game()
        game.create(CreationOptions())
        with open('/tmp/test.pickle', 'wb') as f:
            p.dump( game, f )
    elif args.command == 'run' :
        with open('/tmp/test.pickle', 'rb') as f:
            game = p.load(f)
            game.turn[0].report()
    elif args.command == 'map':
        with open('/tmp/test.pickle', 'rb') as f:
            game = p.load( f )
            with open('map.csv', 'w') as mf:
                game.map( mf )
    elif args.command == 'report':
        with open('/tmp/test.pickle', 'rb') as f:
            game = p.load( f )
            turn_reports = game.report()
            for a_report in turn_reports:
                with open('/tmp/%s.txt' % a_report.nation.name, 'w') as report_file:
                    a_report.report_in_text( report_file )


if __name__ == "__main__":
    arguments = docopt(__doc__, version='galaxy 0.1')
    game_name = arguments["<name>"]
    filename = "/tmp/{}.pickle".format(game_name)
    print(arguments)
    if arguments['create']:
        game = Game()
        game.create(CreationOptions())
        with open(filename, 'wb') as f:
            p.dump( game, f )
    elif arguments['run']:
        with open(filename, 'rb') as f:
            game = p.load(f)
            # TODO read orders
            game.run(None)
        with open(filename, 'wb') as f:
            p.dump(game, f)
    elif arguments['report']:
        with open(filename, 'rb') as f:
            game = p.load(f)
            turn_reports = game.report()
            for a_report in turn_reports:
                with open('/tmp/{}.txt'.format(a_report.nation.name), 'w') as report_file:
                    a_report.report_in_text(report_file)
    elif arguments['map']:
        with open(filename, 'rb') as f :
            game = p.load(f)
            with open('map.csv', 'w') as mf:
                game.map(mf)
    else:
        pass




