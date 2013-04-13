#
# vi: spell spl=en


from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--name", dest="gamename",
                  help="Name of the game", metavar="NAME")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

print "Gamename ", options.gamename

