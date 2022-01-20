import datetime

from Generators import *
from Databases import *
from Table import *
from Column import *

# https://faker.readthedocs.io/en/master/providers.html
# TODO: Create table if no exists maybe
db = Sqlite3DB(True, False)
db.connect(dbName=r"C:\Users\PhatPhuckDave\PycharmProjects\pokeSuka\db.sqlite3")

# team = Table("pokemon_team")
# team.addColumns([
# 	Column("id", SerialGenerator(1), True),
# 	Column("name", FakeNameGenerator()),
# 	Column("user_id", SetGenerator(db.getPkSet(user), True)),
# ])
sequences = [
	[i for i in range(1000)],
	[i for i in range(1000)],
	[i for i in range(1000)],
	[i for i in range(1000)],
]
pokemon = Table("pokemon_pokemon")
pokemon.addColumns([
	Column("id", SerialGenerator(1), True),
	Column("name", FakeFirstNameGenerator()),
	Column("team_fk_id", ConstantGenerator(0)),
	Column("front", SequentialPatternGenerator(r"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/%s.png", sequences[0])),
	Column("back", SequentialPatternGenerator(r"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/%s.png", sequences[1])),
	Column("front_shiny", SequentialPatternGenerator(r"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/%s.png", sequences[2])),
	Column("back_shiny", SequentialPatternGenerator(r"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/%s.png", sequences[3])),
	Column("height", RandomFloatGenerator(0, 500)),
	Column("weight", RandomFloatGenerator(0, 100)),
])
# type = Table("pokemon_type")
# type.addColumns([
# 	Column("id", SerialGenerator(1), True),
# 	Column("type", RandomIntegerGenerator(1, 20000)),
# 	Column("poke_fk_id", SetGenerator(db.getPkSet(pokemon), True)),
# ])

# db.wipeTable(team)
db.wipeTable(pokemon)
# db.wipeTable(type)

# db.setTable(user)
# for i in range(100):
# 	db.insertRow()

# db.insertRows(team, 100)
db.insertRows(pokemon, 300)
# db.insertRows(type, 300)