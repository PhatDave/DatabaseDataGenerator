import postgresql

from Generators import *
from Databases import *
from Table import *
from Column import *

# https://faker.readthedocs.io/en/master/providers.html
db = PostgreSQLDB(True)
db.connect(dbName="carService")

users = Table("users")
db.addTable(users)
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

for i in range(100):
	db.insertRow()