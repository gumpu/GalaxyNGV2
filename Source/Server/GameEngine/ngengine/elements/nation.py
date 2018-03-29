# vi: spell spl=en

class Nation(object):

    def __init__( self, key, name ):
        self.key  = key
        self.name = name
        self.drive_tech   = 1.0
        self.weapons_tech = 1.0
        self.shield_tech  = 1.0
        self.cargo_tech   = 1.0

