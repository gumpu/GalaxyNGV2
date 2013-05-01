#!/usr/bin/env python

import json
import random

class Planet( object ):
    def __init__( self ):
        self.x = random.randint( 0, 100 )
        self.y = random.randint( 0, 100 )
        self.key = 'p{}{}'.format( self.x, self.y )

class Universe( object ):
    def __init__( self ):
        self.size = 100
        self.planets = {}
        for i in xrange(10):
            p = Planet()
            self.planets[ p.key ] = p

def convert_to_builtin_type( obj ):
    # Convert objects to a dictionary of their representation
    # d = { '__class__':obj.__class__.__name__ }
    d = { }
    d.update(obj.__dict__)
    return d

if __name__=='__main__':

    uni = Universe()
    print json.dumps( uni, indent=4, default=convert_to_builtin_type )

