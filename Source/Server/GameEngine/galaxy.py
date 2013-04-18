#!/usr/bin/env python
# vi: spell spl=en


import argparse

parser = argparse.ArgumentParser()
parser.add_argument( '--create', help="Create a new game", metavar="GAME_NAME" )
parser.add_argument( '--run',    help="Run a turn", metavar="GAME_NAME" )
parser.add_argument( '--dump',   help="Dump game data", metavar="GAME_NAME" )
# parser.add_option("-n", "--name", dest="gamename",
#                   help="Name of the game", metavar="NAME")
# 
# parser.add_option("-q", "--quiet",
#                   action="store_false", dest="verbose", default=True,
#                   help="don't print status messages to stdout")

#
# actions 
#  create
#  run
#

(options, args) = parser.parse_args()

print "Gamename ", options.gamename

