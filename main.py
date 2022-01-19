import datetime

import postgresql

from Generators import *
from Databases import *
from Table import *
from Column import *

# https://faker.readthedocs.io/en/master/providers.html
db = PostgreSQLDB(True, True)
db.connect(dbName="carService")

users = Table("users")
users.addColumns([
	Column("id", SerialGenerator(1), True),
	Column("city", FakeCityGenerator()),
	Column("country", FakeCountryGenerator()),
	Column("postal_number", RandomIntegerGenerator(1e4, 1e5)),
	Column("street", FakeStreetGenerator()),
	Column("first_name", FakeFirstNameGenerator()),
	Column("last_name", FakeLastNameGenerator()),
	Column("street_number", RandomIntegerGenerator(0, 1000)),
])
cars = Table("cars")
cars.addColumns([
	Column("id", SerialGenerator(1), True),
	Column("color", SetGenerator({"red", "blue", "yellow", "green", "purple"})),
	Column("manufacturer_model", RandomIntegerGenerator(0, 6)),
	Column("production_year", RandomIntegerGenerator(1990, 2020)),
	Column("registration", FakeLicensePlateGenerator()),
	Column("userid", SetGenerator(db.getPkSet(users), False)),
])

db.wipeTable(cars)
db.wipeTable(users)

db.setTable(users)
for i in range(1000):
	db.insertRow()

db.setTable(cars)

for i in range(1000):
	db.insertRow()
