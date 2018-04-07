# vi: spell spl=en

class Order():
    def __init__(self):
        self.for_phase = None
        self.error_message = None

    def parse(self, line, nation, game):
        pass

    def execute(self, phase, a_game):
        pass

class ProduceOrder():
    def __init__(self):
        super().__init__()

    def parse(self, line, nation, game):
        parts = line.split()
        assert(parts[0] == "produce")

class OrderList():
    def __init__(self, nation):
        self.nation = nation
        self.lines  = []
        self.orders = []
        self.errors = []

    def execute(self, phase, game):
        pass

    def syntax_check(self):
        """Check the syntax of all lines in this orders.

        Orders can still fail because of semantic reasons
        later.
        """
        for line in self.lines:
            pass

    def add(self, line):
        self.lines.append(line)

#-------------------------------------------------------------------
