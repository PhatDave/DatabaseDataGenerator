import postgresql

from Generators import *
from Databases import *
from Table import *
from Column import *

db = postgresql.open('pq://demo:demo@127.0.0.1:5432/carService')

db = PostgreSQLDB(True)
db.connect(dbName="carService")

users = Table("users")
db.addTable(users)
users.addColumns([
	Column("id", SerialGenerator(1), True),
	Column("city", RandomGenerator(10)),
	Column("country", RandomGenerator(10)),
	Column("postal_number", RandomIntegerGenerator(1e4, 1e5)),
	Column("street", RandomGenerator(10)),
	Column("first_name", FakeFirstNameGenerator()),
	Column("last_name", FakeLastNameGenerator()),
])

for i in range(2):
	db.insertRow()