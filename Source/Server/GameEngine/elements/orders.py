# vi: spell spl=en

class Orders(object):

    def __init__(self, nation):
        self.nation = nation
        self.lines  = []
        self.errors = []

    def execute(self, phase, a_game):
        pass

    def syntax_check(self):
        """Check the syntax of all lines in this ordes.

        Orders can still fail because of semantic reasons
        later.
        """
        pass

    def add_line(self, line):
        pass

