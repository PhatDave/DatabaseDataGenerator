import datetime

from Generators import *
from Databases import *
from Table import *
from Column import *

# https://faker.readthedocs.io/en/master/providers.html
# TODO: Create table if no exists maybe
db = Sqlite3DB(True, False)
db.connect(dbName=r"C:\Users\PhatPhuckDave\PycharmProjects\pokemonGo\db.sqlite3")

user = Table("auth_user")
user.addColumns([
	Column("id", SerialGenerator(3), True),
	Column("password", RandomStringGenerator(88)),
	Column("is_superuser", ConstantGenerator(1)),
	Column("username", FakeUsernameGenerator()),
	Column("last_name", FakeLastNameGenerator()),
	Column("first_name", FakeFirstNameGenerator()),
	Column("email", FakeEmailGenerator()),
	Column("is_staff", ConstantGenerator(1)),
	Column("is_active", ConstantGenerator(1)),
	Column("date_joined", ConstantGenerator("2022-01-20 12:01:31.883462")),
])

team = Table("pokemon_team")
team.addColumns([
	Column("id", SerialGenerator(1), True),
	Column("name", FakeNameGenerator()),
	Column("user_id", SetGenerator(db.getPkSet(user), True)),
])
pokemon = Table("pokemon_pokemon")
pokemon.addColumns([
	Column("id", SerialGenerator(1), True),
	Column("name", FakeFirstNameGenerator()),
	Column("team_fk_id", SetGenerator(db.getPkSet(team))),
])
type = Table("pokemon_type")
type.addColumns([
	Column("id", SerialGenerator(1), True),
	Column("type", RandomIntegerGenerator(1, 20000)),
	Column("poke_fk_id", SetGenerator(db.getPkSet(pokemon), True)),
])

db.wipeTable(team)
db.wipeTable(pokemon)
db.wipeTable(type)

# db.setTable(user)
# for i in range(100):
# 	db.insertRow()

db.insertRows(team, 100)
db.insertRows(pokemon, 300)
db.insertRows(type, 300)