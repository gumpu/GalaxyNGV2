# vi: spell spl=en

class Shiptype(object):

    def __init__(self, key, name, drive, attacks, weapon, shield, cargo ):
        self.key     = key
        self.name    = name
        self.drive   = drive
        self.attacks = attacks
        self.weapon  = weapon
        self.shield  = shield
        self.cargo   = cargo

    def mass(self):
        """Mass of a ship of this type.

        Without any cargo.
        """
        m = ( self.drive + self.weapon +
                0.5*(self.attacks - 1)*self.weapon + 
                self.shield + self.cargo )
        return m

