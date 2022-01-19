# PostreSQL-Random-Data-Generator

## Generates large amounts of fake data for testing purposes

## Currently only supports postgresql!

---

Example of use can be found in main.py

Generators can be found in Generators.py

---

## Another example

```py
# Initialize database where insertion replaces rows which already exist (with same pk)
db = PostgreSQL(override=True)
db.connect(user="demo", password="demo", ip="127.0.0.1", port="5432", dbName="demo")

# Create a table object which will signify the existance of that table in the database
# In other words, when queries are generated these are the tables that are inserted to
table_name = Table("some_table_name")
# INSERT INTO some_table_name VALUES ...

# A database can have multiple tables and they will all be added rows simultaneously though this is untested yet
db.addTable(table_name)

# Adding columns to a table can either be done in batch (like below) or one by one
# Columns have a name and a generator, they can also be the primary key (the pk comes into play when override is enabled and rows will be overriden by removing the row by the PK column)
some_table.addColumns([
	Column("id", SerialGenerator(1), True),
	Column("some_data", RandomStringGenerator()),
])
# Example of adding one column
some_table.addColumn(Column("some_other_data", RandomIntegerGenerator()))

# From here calling db.insertRow() will insert a single row, call it multiple times to insert mutliple rows
for i in range(100):
	db.insertRow()
```

---

## Available generators

With example output

```py
RandomStringGenerator(length=10, 
                      hasLowercase=True, 
                      hasUppercase=False,
                      hasDigits=False)
# RandomStringGenerator(24, True, True, False)                      
# CgR9MmJqbdIGmhB8tixhqetC
# 6QahKKKYKJwIfmhTYksARQK8
# KvG3YT8qU0nIqTngv4FFX8l0

RandomIntegerGenerator(min, max)
# RandomIntegerGenerator(1e2, 1e6)
# 850992
# 319942
# 568911

SerialGenerator(start=0, step=1)
# SerialGenerator()
# 0
# 1
# 2

SetGenerator(chSet)
# SetGenerator({'a', 'b', 12, 43, "testing"})
# 12
# b
# a

FakeFirstNameGenerator()
# FakeFirstNameGenerator()
# Kimberly
# Kathleen
# Ryan

FakeLastNameGenerator()
# FakeLastNameGenerator()
# Horne
# Barry
# Cantu

FakeNameGenerator()
# FakeNameGenerator()
# Julian Bryant
# Jerry King
# Debbie Hubbard

FakeCityGenerator()
# FakeCityGenerator()
# West Sarahfurt
# Susanside
# Robertmouth

FakeCountryGenerator()
# FakeCountryGenerator()
# Bulgaria
# American Samoa
# France

FakeStreetGenerator()
# FakeStreetGenerator()
# Ferguson Fords
# Thomas Summit
# Jones Walks
```