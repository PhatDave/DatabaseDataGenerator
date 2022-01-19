import postgresql

# db = postgresql.open('pg://user:password@host:port/db')
from Generators import *
from Databases import *
from Table import *
from Column import *

db = postgresql.open('pq://demo:demo@127.0.0.1:5432/carService')
# test = db.prepare('SELECT * FROM cars')
# column_names
# column_types
# parameter_types

# mkemp = db.prepare("INSERT INTO users(id) VALUES ($1)")
#
# for i in range(1000, 10000):
# 	mkemp(i)
#
# print(mkemp)

db = PostgreSQLDB()
db.connect(dbName="carService")

users = Table("users")
db.addTable(users)
users.addColumns([
	Column("id", SerialGenerator(1300)),
	Column("city", RandomGenerator(255)),
	Column("country", RandomGenerator(255)),
	Column("postal_number", RandomGenerator(10, False, False, True)),
	Column("street", RandomGenerator(255)),
])

db.insertRow()