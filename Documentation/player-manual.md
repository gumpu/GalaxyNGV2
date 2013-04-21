vi: spell spl=en ft=markdown

#Player Manual

For GalaxyNG V2

Version 0.1

April 2013

##Introduction

GalaxyNG is a multiplayer game of interstellar war.  The objective of the game
is to conquer the galaxy.

Players email a GalaxyNG server to register for games, submit orders and
receive turn reports.  The server automatically processes turns and responds
to player email.  Most games run one to five turns per week and can last from
a few months to a year or more.  The Game Master (GM) maintains the server,
selects game options, creates the galaxy, answers player questions and solves
problems.

###The Galaxy

The area of the galaxy in which the game is played is a square (for the sake
of simplicity the third dimension is ignored) which contains a number of
habitable planets.  Planets are used to build ships, conduct technology
research, produce capital or produce materials.  Ships explore the galaxy,
colonize uninhabited planets, haul cargo, conduct warfare and conquer planets
inhabited by other nations.  Technology improvements allow ships to fly faster
and farther, haul more cargo and fight better.

###Players

Each player is the leader of one nation.  Players can communicate by sending
messages or email to each other.  Players are anonymous but can choose to
reveal their identities to other players.  Players can provide their real name
to the GM for inclusion in the Hall of Fame without breaking their anonymity.

###Victory and Defeat

The game can be won by a single nation or by an alliance of nations, depending
upon the game settings.  Nations are ranked based on the total production of
their planets.  A nation is eliminated if it owns no planets and has no ships.
The game is complete when all surviving players agree to end it and notify the
game master.

###Names

Nations, planets, ship types and fleets can be named.  Names may be no more than
twenty characters (a character is a letter, digit, or underscore) and may not
include spaces.  Names must be unique.  For example, a nation cannot have the
same name as a fleet.  Each player should provide a name by which their nation
will be known, e.g. Mutant\_Camels or Zzyaxians - if this is not done they will
simply be known by number, e.g. Nation\_4 or Nation\_5.  Ship types are given names
when designed and can be renamed.  Planets are numbered at the start of the
game and can be given new names by their current owner.

###Units of Measure

Distances are measured in light-years.  Each unit of population represents ten
million people and each unit of capital or materials represents ten million
tons.  Each turn represents about four years of time.

The game engine stores numbers in double precision format but
truncates values reported to players to two decimal places.
For example, drive technology 2.4389 will be reported as 2.43 and a ship
designed with shields mass 18.11999999 will be reported as shields mass 18.11.
Note that galaxy size, planet coordinates and resources are the exceptions - a
planet reported at 138.44,43.29 with 4.30 resources is actually at that
location and will not be found at 138.4426,43.28934 with 4.3032 resources.
Negative numbers are not used in GalaxyNG.

##Planets

Planets are located in the galaxy by X and Y coordinates.  Planets have seven
characteristics: owner, size, population, industry, resources, production and
stockpiles.

###Owner

Inhabited planets are owned by one nation at a time (except in the special case
of a standoff when an inhabited planet is unowned).  Uninhabited planets are
not owned by any nation.

###Size

Planets vary in size from 0.01 to 1000.00 (GMs can create larger planets).
The size of a planet reflects the habitability of the terrain, the suitability
of the climate for agriculture, and other features.  At the beginning of the
game, the galaxy is usually divided into inhabited planets (home planets),
uninhabited development planets (size 200.00 to 1000.00) and uninhabited stuff
planets (size 0.01 to 200.00).

###Population

Each inhabited planet has a population, which can never be larger than the
planet's size but may be smaller.  A planet with zero population is
uninhabited.  Home planets are fully populated at the beginning of the game.
Each planet's population grows by 8% per turn.  Excess population is
stockpiled as colonists.  Each unit of colonists represents eight
population.

###Industry

Each inhabited planet has industry, which can never be larger than the
planet's population but may be smaller.  If population exceeds industry, the
industry may be increased by adding capital.  If there is not an existing
stockpile of capital, it may be produced at the planet or be shipped in from
another planet by cargo ships.  For example, if a size 500 planet with 500
population and 200 industry produces 75 capital, the industry will increase to
275.  If a size 500 planet with 200 population and 200 industry has a
stockpile of 100 capital, on the following turn the population and industry
will both increase to 216 and there will be 84 capital left (because
population grows by 8% per turn).

###Resources

Each planet has a resources value which indicates how rich it is in metals,
coal, oil, wood and other products.  Home planets have a resources value of
10.00.  Other planets have a resources value between 0.01 and 10.00, with the
average being 1.00.  Planets high in resources can easily produce materials
such as sheet steel, copper wire and
plastics.  Materials are necessary to build ships and produce capital.

###Stockpiles

Each planet may have stockpiles of colonists, capital and materials.
Population increases beyond the planet's size are converted into colonists.
Eight population are converted into one colonist.  These are people
automatically stored in containers in deep freeze.  Excess capital and
materials are stockpiled at a one-to-one ratio.  Stockpiles may be saved for
later use or transported to other planets by cargo ships.


##Ships

Ships are organized into groups and fleets which are used for exploration,
scouting, attack, defence and cargo transport.  Ships have the following
characteristics: ship type (name, drive mass, attacks, weapons mass, shields
mass, cargo mass and ship mass), group number, fleet name, drive technology,
weapons technology, shields technology, cargo technology, cargo carried type,
cargo carried mass, destination planet, and distance to destination planet.
Ships can be built at planets.

###Ship Types

Each player can design ship types, which are unique to that player, by
specifying: name, drive mass (the power of the hyperdrive engines), attacks
(the number of guns), weapons mass (the strength of the guns), shields mass
(the power of the shields generator), and cargo mass (the size of the cargo
bay).  Drive mass, weapons mass, shields mass, and cargo mass must equal zero
or be equal to or greater than one.  Thus, drive mass 0.00 and 1.50 are
allowed but drive mass 0.75 is not.  Attacks must be an integer.  Some example
ship types are:

                       D    A     W      S      C
    Drone            1.00   0   0.00   0.00   0.00
    Flak             1.00   0   0.00   2.00   0.00
    FastFlak         1.01   0   0.00   1.01   0.00
    Fighter          2.48   1   1.20   1.27   0.00
    Gunship          4.00   2   2.00   4.00   0.00
    Destroyer        6.00   3   4.00   4.00   0.00
    Cruiser         16.50  30   1.50   9.75   0.00
    BattleCruiser   49.50  25   3.00   9.50   1.00
    Battleship      33.00   3  25.00  16.00   1.00
    BattleStation   99.00   1  50.00  49.00   0.00
    OrbitalFort      0.00  11  10.00  39.00   0.00
    SpaceGun         0.00   1   9.90   9.90   0.00
    Hauler           2.00   0   0.00   0.00   1.00
    Freighter       30.00   0   0.00   9.50  10.00
    MegaFreighter  120.00   0   0.00  38.43  39.57

Players can change the name of an existing ship type.  Ship types can be
eliminated if no ships of that type exist or are under construction.

###Groups

A nation can have hundreds or even thousands of ships, which would be
inconvenient to handle individually.  Hence ships are handled in groups, which
can contain one or more ships all of the same type, in the same place,
carrying the same quantity and type of cargo (if any) and built with the same
technology levels.

Groups can be ordered to travel to another planet, 
intercept other ships, reverse course, 
break off ships into a new group, join a fleet, leave a fleet, upgrade
technology levels, load cargo, or unload cargo.  Groups may also be scrapped,
which automatically unloads all cargo and deposits the materials used to
produce the ships at the current planet.  If routes have been established,
groups will follow them.

Each group is assigned a number, which is used to issue orders to ships in the
corresponding group.  When new groups are created, they are assigned a number
N+1, where N is the highest numbered group in existence.  Whenever a group
number is required as an order parameter, the keyword MAX may be used instead.
This will apply the order to the group with the highest group number, i.e. the
most recently created group.

In several phases of the turn, groups containing identical ships, carrying
identical cargo (if any), in the same place and in the same fleet (if
applicable) will be merged using the lower group number.  For example, if
group 5 containing 48 ships is merged with group 12 containing 52 ships, group
5 will contain 100 ships and group 12 will be eliminated.

If the SortGroups option is turned on, at the end of each turn groups will be
automatically sorted and renumbered as follows: Owner's groups at owner's
planets; Owner's groups at other nation's planets; Owner's groups at uninhabited
planets; Owner's groups in fleets.

###Fleets

Fleets contain groups, allowing players to gather different ship types
together in a single unit.  Many of the orders for groups can also be used for
fleets.  Players can create, eliminate, merge and rename fleets.  Fleets can
be ordered to travel to another planet, intercept other ships, or reverse
course.  The slowest group in the fleet
sets the maximum speed for the entire fleet.

A group in a fleet that is given a send or intercept order is automatically
removed from the fleet.  Ships in a fleet that are broken from groups are also
removed from the fleet.  Groups in fleets that are ordered to upgrade, load or
unload cargo remain in the fleet.  Groups in fleets will not travel on routes.

###Technology

Technology determines the effectiveness of ships.  There are four
technologies: drive, weapons, shields and cargo.  Each nation begins the game
with 1.00 levels in each technology.  Technology can be increased by ordering
planets to conduct research.

Ships are assigned the technology levels of the nation at the time they are
produced.  As the nation's technology level increases, ships can be upgraded at
planets owned by the player.

A ship with drive technology 4.00 is twice as fast as an equivalent ship with
drive technology 2.00, a ship with weapons technology 1.50 has a 50% more
powerful attack than the same ship with weapons technology 1.00, and so forth.
Ships without a component are considered to have a matching technology of
zero.  For example, a ship with weapons mass zero is considered to have
weapons technology zero.

###Ship Mass

Ship types with zero or one attack have a ship mass of drive mass + weapon
mass + shield mass + cargo mass.  Each additional attack beyond the first adds
50% of the weapon mass to the ship mass.  For example:

                      D   +     W   +    Additional    +     S   +   C   =  Ship
                                          Attacks                           Mass
    Drone            1.00 +    0.00 +        0         +    0.00 +  0.00 =   1.00
    Flak             1.00 +    0.00 +        0         +    2.00 +  0.00 =   3.00
    FastFlak         1.01 +    0.00 +        0         +    1.01 +  0.00 =   2.02
    Fighter          2.48 +    1.20 +        0         +    1.27 +  0.00 =   4.95
    Gunship          4.00 +    2.00 + ( 1 *  2.00 / 2) +    4.00 +  0.00 =  11.00
    Destroyer        6.00 +    4.00 + ( 2 *  4.00 / 2) +    4.00 +  0.00 =  18.00
    Cruiser         16.50 +    1.50 + (29 *  1.50 / 2) +    9.75 +  0.00 =  49.50
    BattleCruiser   49.50 +    3.00 + (24 *  3.00 / 2) +    9.50 +  1.00 =  99.00
    Battleship      33.00 +   25.00 + ( 2 * 25.00 / 2) +   16.00 +  1.00 =  99.00
    BattleStation   99.00 +   50.00 +        0         +   49.00 +  0.00 = 198.00
    OrbitalFort      0.00 +   10.00 + (10 * 10.00 / 2) +   39.00 +  0.00 =  99.00
    SpaceGun         0.00 +    9.90 +        0         +    9.90 +  0.00 =  19.80
    Hauler           2.00 +    0.00 +        0         +    0.00 +  1.00 =   3.00
    Freighter       30.00 +    0.00 +        0         +    9.50 + 10.00 =  49.50
    MegaFreighter  120.00 +    0.00 +        0         +   38.43 + 39.57 = 198.00


###Movement

Ships are equipped with hyperspace drives, except ships with a drive mass of
zero which remain forever at the planet where they were built.  Hyperspace
travel is only possible from one planet to another.  Groups always travel at
maximum speed in hyperspace, unless they are part of a fleet.  Groups in
hyperspace cannot participate in combat.  Groups in hyperspace cannot be
issued any orders, except reverse.

Groups can be sent to other planets.

Groups can be ordered to intercept alien ships at a target planet.
Intercepting groups will attempt to follow alien ships leaving the target
planet, but can only intercept at destination planets within two turns range
of the intercepting group.  The intercepting group will be sent toward
whichever destination planet is within two turns range and has the largest
total mass (ship mass plus cargo carried mass) of alien ships departing toward
it from the target planet that turn.  If all destination planets are farther
than two turns range, or if no alien groups leave the target planet, the
intercepting group will be sent to the target planet.  Note that the total
mass of ships leaving the target planet is the sole determinant of potential
interception locations.  If a single Probe departs a target planet and 2,000
ships remain behind, the intercepting group will follow the Probe.

Groups in hyperspace that are more than four turns from their destination
planet may be ordered to reverse course and return to their planet of origin.
This is useful for retrieving groups accidentally sent to the wrong planet.

###Speed

Ships move a number of light years per turn according to the following formula:

Speed = 20 * drive technology * (drive mass / (ship mass + effective cargo carried mass)).

Note that unless your drive technology is very high, large ships should have
correspondingly large drives or they will be very slow.  On the other hand the
fastest ships you can possibly build (all numbers except drive mass being zero
in the design) can only travel at a speed of twenty times your drive
technology.  For example, using the ship types above and assuming drive
technology 1.00:

                   20 * Drive * (  Drive / (   Ship +   Effective   )) = Speed
                         Tech       Mass       Mass   Cargo Carried
    Drone          20 *  1.00 * (   1.00 / (   1.00 +      0.00     )) = 20.00
    Flak           20 *  1.00 * (   1.00 / (   3.00 +      0.00     )) =  6.66
    FastFlak       20 *  1.00 * (   1.01 / (   2.02 +      0.00     )) = 10.00
    Fighter        20 *  1.00 * (   2.48 / (   4.95 +      0.00     )) = 10.02
    Gunship        20 *  1.00 * (   4.00 / (  11.00 +      0.00     )) =  7.27
    Destroyer      20 *  1.00 * (   6.00 / (  18.00 +      0.00     )) =  6.66
    Cruiser        20 *  1.00 * (  16.50 / (  49.50 +      0.00     )) =  6.66
    BattleCruiser  20 *  1.00 * (  49.50 / (  99.00 +      0.00     )) = 10.00
    Battleship     20 *  1.00 * (  33.00 / (  99.00 +      0.00     )) =  6.66
    BattleStation  20 *  1.00 * (  99.00 / ( 198.00 +      0.00     )) = 10.00
    OrbitalFort    20 *  1.00 * (   0.00 / (  99.00 +      0.00     )) =  0.00
    SpaceGun       20 *  1.00 * (   0.00 / (  19.80 +      0.00     )) =  0.00
    Hauler         20 *  1.00 * (   2.00 / (   3.00 +      0.00     )) = 13.33
    Freighter      20 *  1.00 * (  30.00 / (  49.50 +      0.00     )) = 12.12
    MegaFreighter  20 *  1.00 * ( 120.00 / ( 198.00 +      0.00     )) = 12.12

Note that, when fully loaded, cargo ships can be much slower.  For example:

    BattleCruiser  20 *  1.00 * (  49.50 / (  99.00 +      1.10     )) =  9.79
    Battleship     20 *  1.00 * (  33.00 / (  99.00 +      1.10     )) =  6.52
    Hauler         20 *  1.00 * (   2.00 / (   3.00 +      1.10     )) =  9.75
    Freighter      20 *  1.00 * (  30.00 / (  49.50 +     20.00     )) =  8.63
    MegaFreighter  20 *  1.00 * ( 120.00 / ( 198.00 +    196.14     )) =  6.09

###Locating Ships

Each nation's administrative staff will keep a record of its own ships on
planets or in hyperspace.  Planet owners have full knowledge of all ships
orbiting their planets.  Players also receive complete reports on ships at
planets visited by their own ships.

Locating alien ships in hyperspace is much more problematic.  Detectors to
accurately locate the position of alien ships in hyperspace are installed on
each planet.  Accurate readings of mass, speed, origin and distance from
destination can be obtained for ships heading directly toward a detector (i.e.
inbound to a planet).  A rough indication of the location of other alien
groups is indicated on the text map, but their mass, speed
and direction of travel are unknown.

###Cargo

Cargo ships can load stockpiles of colonists, capital and
materials to transport them to other planets where they
can be unloaded.  Each ship may only carry one type of
cargo at a time.  The base amount of cargo a ship can carry is determined by
the following formula: base cargo = cargo mass + cargo mass^2/10.  Thus, at
cargo technology 1.00, some examples would be:

                   Cargo + Cargo Mass^2/10 =  Base Cargo
                    Mass                        Carried
    BattleCruiser   1.00 +       0.10      =      1.10
    Battleship      1.00 +       0.10      =      1.10
    Hauler          1.00 +       0.10      =      1.10
    Freighter      10.00 +      10.00      =     20.00
    MegaFreighter  39.57 +     156.57      =    196.14

Cargo technology increases the amount of cargo that a ship can carry.  Thus, a
Hauler with cargo technology 2.00 can carry 2.20 cargo and a Freighter with
cargo technology 3.00 can carry 60.00 cargo.  This does not slow down the
ships, as the cargo carried is divided by the cargo technology to obtain the
effective cargo carried.  Thus, at cargo technology 3.00, a Freighter carrying
60.00 cargo has an effective cargo carried of 20.00, while the same Freighter
carrying 35.00 cargo has an effective cargo carried of 11.66.

Colonists that are unloaded at an uninhabited planet will claim the planet for
their nation.  Each colonist becomes eight population.  Capital and materials
unloaded at an uninhabited planet will be stockpiled until the planet is
colonized.

###Routes

Colonists, capital, materials, and empty routes can be established between
planets.  Each planet can be the origin for only one route of each type.  A
planet can be the destination of an unlimited number of routes.  For example,
colonists routes can be set from planets 105, 82 and 243 to planet 56 but
planet 105 cannot simultaneously have a colonists route to planet 97.  Players
may only establish routes from their own planets, however any planet may be
the destination of a route.

Cargo ships that are not in fleets and have not been ordered to travel between
planets will automatically follow routes.  They will load cargos, travel to
destination planets, and unload cargos.  Cargo ships that are already loaded
will also follow routes.

Routes are assigned to cargo ships in the following order of priority:
colonists, capital, materials and empty.  Ships are used in order by group
number to full capacity, if possible.  For example, planet 105 has colonists
and capital routes to planet 56, an empty route to planet 74, forty cargo
ships with 2.00 capacity each, 10.00 colonists and 31.00 capital.  Five cargo
ships will carry colonists to planet 56, sixteen cargo ships will carry
capital to planet 56 and the remaining nineteen cargo ships will travel empty
to planet 74.  However, if there is an additional cargo ship with capacity
40.00 and a lower group number than the 2.00 capacity ships, it will be used
to carry 10.00 colonists to planet 56.  If it has a higher group number, it
will travel empty to planet 74.

All ships, regardless of origin planet, that arrive at a destination planet
for a route will be unloaded if they carry the appropriate cargo.  Unloading
at route destinations occurs regardless of the status of the autounload
option.


##Production

The productive capacity of a planet is determined mostly by its industry value
and partly by its population.  Each unit of industry on a planet yields one
production unit, and every four units of population over and above industry
yields an additional production unit.  The formula is:

    Production = Industry + (Population - Industry)/4

or, put another way:

    Production = (Industry * .75) + (Population * .25)

For example, a planet with 500.00 population and 500.00 industry has 500.00
production (500 + 0), a planet with 500.00 population and 250.00 industry has
312.50 production (250 + 250/4) and a planet with 500.00 population and 0
industry has 125.00 production (0 + 500/4).

A planet can be ordered to produce materials, capital,
technology research or ships.  Each planet can only perform one type of
production per turn, however two planets can produce two things in one turn or
one planet can produce two things in two turns.  A planet will continue
producing the same thing until it is ordered to change production, thus new
production orders are not required for each planet each turn.

###Materials

Materials production is determined by the resources values of the planet,
which equals the number of materials that will be produced per point of
production devoted to the task.  For example, a planet with 5.00 resources and
100.00 production will produce 500.00 materials, while a planet with 0.10
resources would only produce 10.00 materials.

###Capital

Producing 1.00 capital requires 5.00 production and 1.00 materials.  If the
planet does not have a stockpile of materials, some production will
automatically be diverted to producing materials.  For example, a planet with
1000.00 production and a stockpile of 200.00 materials will produce 200.00
capital.  With no stockpile of materials and 10.00 resources, 196.08 capital
will be produced.  With 0.10 resources, the planet will produce 66.67 capital.

###Technology

A planet can research one of the four technologies each turn.  It costs
5,000.00 production to increase drive, weapons, or shields technology by one
point and 2,500.00 production to increase cargo technology by one point.
Fractional increases are effective immediately: if you spend 500.00 production
on research into Weapons, your weapons technology will go up by 0.10.
Research takes effect on the following turn and applies to all new and
upgraded ships, regardless of which planet conducted the research.

###Ship Building

A planet can produce one type of ship each turn.  The production cost of a
ship is equal to its ship mass times ten.  In addition, one unit of materials
is required for every unit of mass.  If the planet does not have a stockpile
of materials, some production will automatically be diverted to producing
materials.

                      Mass  Production  Materials
    Drone             1.00     10.00       1.00
    Flak              3.00     30.00       1.00
    FastFlak          2.02     20.20       2.02
    Fighter           4.95     49.50       4.95
    Gunship          11.00    110.00      11.00
    Destroyer        18.00    180.00      18.00
    Cruiser          49.50    495.00      49.50
    BattleCruiser    99.00    990.00      99.00
    Battleship       99.00    990.00      99.00
    BattleStation   198.00   1980.00     198.00
    OrbitalFort      99.00    990.00      99.00
    SpaceGun         19.80    198.00      19.80
    Hauler            3.00     30.00       3.00
    Freighter        49.50    495.00      49.50
    MegaFreighter   198.00   1980.00     198.00

For example: If a planet with 1000.00 production and 10.00 resources with no
stockpile of materials was producing Drones, it would produce 99.01 per turn.
About 9.90 production would be diverted to producing 99.01 materials to build
the Drones.  The same planet with 0.10 resources would only produce 50.00
Drones per turn.

Excess ship production is carried forward into the next turn.  If the planet
continues producing the same ship type, the fractional production is added to
the current turn production.  For example, a planet with 750 production and
10.00 resources with no stockpile of materials would produce 1.50 Cruisers per
turn.  One Cruiser would be produced on the first turn and two Cruisers would
be produced on the second turn.  A ship which is built over several turns will
be assigned the technology levels of the nation at the start of the final turn.
If the planet's production is changed, the extra ship production is lost and
any materials produced on the previous turn are added to the planet's
stockpiles.

###Upgrading Groups

Groups can be upgraded at the owning player's planets.  Groups that are
upgraded cannot be ordered to travel to another planet or intercept an enemy
group, however they will be sent on routes and participate in combat.  Ships
in the group will be upgraded to the owning player's technology levels as of
the beginning of the turn (if they are already at the current technology
levels, nothing will happen). The cost of upgrading a ship is equal to a
fraction of the production cost of a new ship of the same type.  Ugrades do
not require materials.  The exact formula for the cost is:

    Upgrade cost = 10 * ((1 - ship drive tech / current drive tech) * ship drive mass +
    (1 - ship weapons tech / current weapons tech) * ship weapons mass +
    (1 - ship shields tech / current shields tech) * ship shields mass +
    (1 - ship cargo tech / current cargo tech) * ship cargo mass)

If the planet does not have enough production to upgrade the entire group,
then as many ships as can be completely upgraded will be broken into a new
group and upgraded.  Alternatively, if a specific number of ships are ordered
upgraded (including 0 to explicitly specify the entire group), exactly that
many ships will be upgraded, even if only enough production points are
available to do a partial upgrade.  Groups that are partially upgraded have
their each technology increased by the percentage of production points
available.  The exact formula for a partial
upgrade for each technology is:

    Tech increase = (production available / full upgrade cost) * (current tech - ship tech)

Production spent on upgrading groups during a turn is deducted from the
planet's production for that turn.  Thus, if a planet uses 35% of its
production on upgrades, it can only produce 65% as many materials, capital,
technology or ships as normal.  If a planet uses its entire production on
upgrades, it produces nothing that turn.


##Combat

###War and Alliances

At the start of the game all nations are assumed to be at war with all the other
nations (except in team games).  Alliances may be declared at the beginning of
any turn.  Ships will not initiate combat with allied ships, nor will they
bomb allied planets.  However, there is no way to tell if the allied nation has
also declared an alliance until warships are encountered.  Ships will always
shoot back if fired on (battles will be fought just as if both sides were at
war with each other; declaring an alliance puts warships at no disadvantage in
combat).  Having declared an alliance, war may be declared again at the start
of any subsequent turn and vice versa.

###Fighting Battles

Battles occur whenever a ship with weapons encounters an enemy ship at a
planet.  Ships in hyperspace cannot participate in battles.  In each battle
round, randomly select a ship from all surviving ships that have not yet
attacked (note that if a ship is destroyed before it gets a chance to fire it
will not attack).  For each gun on the ship, randomly select a surviving enemy
ship and fire a shot.  Repeat until all ships have fired.  Battle rounds
continue until the battle is either a standoff or a win.  A battle is a
standoff if all remaining ships are invulnerable to enemy attacks.  A battle
is won if all remaining ships belong to nations that are allied with each other.

Attack and defence strengths are calculated using the following forumlae:

    attack strength = (weapons mass * weapons technology)
    defence strength = ((shield mass * shields technology) / 
               (ship mass + effective cargo carried mass)^(1/3)) * 30^(1/3).

If a shot is successful, the enemy ship is destroyed.  The attack forumula is:

    p[kill] = (log[4](attack strength / defence strength) + 1) / 2

Where log[4](x) is the log with base 4 of x, 
which can be computed with log(x)/log(4).
If the attack strength is four times as strong as the defence strength, the
attack will always succeed.  If the defence strength is four times as strong
as the attack strength, the attack will always fail.  The numbers are
calculated so that if a ship type 10 1 10 10 0 fires at an identical ship, it
will have a 50% chance of destroying the target.

###Bombing Planets

After all battles are resolved, ships with weapons bomb enemy planets,
reducing population and industry by 75%.  Bombed planets produce capital until
ordered to produce something else on later turns.

If only one nation has ships with weapons orbiting a bombed planet, that nation
becomes the new owner of the planet.  If two or more allied nations have ships
with weapons orbiting a bombed planet, the nation that issued a victory command
becomes the new owner.  If no nation issued a victory command, the nation that
appears first in the nations table of the turn report receives the planet.  If
more than one nation issued a victory command, or if there was a standoff, the
planet becomes unowned and produces nothing
until it is claimed by the first nation that unloads colonists at the planet.

##Turn Sequence

1. Planetary production orders are assigned.  Note that production occurs
   later in the turn.
2. Messages are sent.
3. Alliances and war are declared.
4. Groups with weapons attack enemy ships, causing combat.  This can happen if
   a player declares war on the current turn.  It can also happen if a player
   built a ship with weapons at a planet with enemy ships in orbit at the end
   of the previous turn.
5. Groups with weapons bomb enemy planets.  This can happen if a player declares war on the current turn.
6. Groups load or unload cargo.
7. Groups are upgraded.
8. Groups and fleets sent to planets enter hyperspace.
9. Routes are assigned to planets. Cargo ships are assigned cargos and destinations, load cargo (if necessary) and enter hyperspace.
10. Groups and fleets with intercept orders are assigned destinations and enter hyperspace.
11. Groups and fleets move through hyperspace, possibly arriving at planets.
12. Groups with weapons attack enemy ships, causing combat.
13. Groups with weapons bomb enemy planets.
14. Planets produce materials or capital, conduct research, or build ships.
15. Population growth occurs.
16. Ships at route destinations unload cargo.
    All ships unload cargo if the autounload option is turned on.
17. Identical groups are merged.
18. Groups are renumbered if the sortgroups option is turned on.
19. Nations, planets, ships and fleets are renamed.


A number of things follow from this:

1. COL, CAP and MAT transported to a planet do not effect the planet's
   production until the following turn.
2. A cargo ship can be loaded, sent to another planet and unloaded in a single
   turn.
3. One ship can bomb two planets in the same turn (though this is rare).






