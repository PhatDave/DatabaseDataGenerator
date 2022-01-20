import datetime

from Generators import *
from Databases import *
from Table import *
from Column import *

# https://faker.readthedocs.io/en/master/providers.html
db = Sqlite3DB(True, True)
db.connect(dbName="demo.db")

pokemon = Table("pokemon")
pokemon.addColumns([
	Column("poke_id", SerialGenerator(1), True),
	Column("name", FakeFirstNameGenerator()),
])
type = Table("type")
type.addColumns([
	Column("type_id", SerialGenerator(1), True),
	Column("poke_fk", SetGenerator(db.getPkSet(pokemon))),
	Column("name", SetGenerator({"Fire", "Water", "Ice", "Earth", "Electric"})),
])

db.wipeTable(pokemon)
db.wipeTable(type)

db.setTable(pokemon)
for i in range(100):
	db.insertRow()

db.setTable(type)

for i in range(250):
	db.insertRow()
