import datetime

from Generators import *
from Databases import *
from Table import *
from Column import *

# https://faker.readthedocs.io/en/master/providers.html
db = Sqlite3DB(True, True)
db.connect(dbName="demo.db")

users = Table("pokemon")
users.addColumns([
	Column("poke_id", SerialGenerator(1), True),
	Column("name", Fake()),
	Column("country", FakeCountryGenerator()),
	Column("postal_number", RandomIntegerGenerator(1e4, 1e5)),
	Column("street", FakeStreetGenerator()),
	Column("first_name", FakeFirstNameGenerator()),
	Column("last_name", FakeLastNameGenerator()),
	Column("street_number", RandomIntegerGenerator(0, 1000)),
])

db.wipeTable(cars)
db.wipeTable(users)

db.setTable(users)
for i in range(1000):
	db.insertRow()

db.setTable(cars)

for i in range(1000):
	db.insertRow()
