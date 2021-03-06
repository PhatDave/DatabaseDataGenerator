# DatabaseDataGenerator

# https://pypi.org/project/DatabaseDataGenerator

## Generates large amounts of fake data for testing purposes

## Currently only supports postgresql & sqlite3!

---

Example of use can be found in main.py

Generators can be found in Generators.py

The majority of generators are wrappers of [Faker](https://faker.readthedocs.io/en/master/index.html)

---

## Another example

```py
from DataGenerator import *
from DataGenerator.Generators import *
from DataGenerator.Table import *
from DataGenerator.Column import *
# Currently I don't know how to handle imports any better

# Initialize database where insertion replaces rows which already exist (with same pk)
db = Databases.PostgreSQLDB(override=True)
db.connect(user="demo", password="demo", ip="127.0.0.1", port="5432", dbName="demo")

# db = Sqlite3DB(True, False)
# db.connect(dbName=r"demo.sqlite3")

# Create a table object which will signify the existance of that table in the database
# In other words, when queries are generated these are the tables that are inserted to
some_table = Table("some_table_name")
# INSERT INTO some_table_name VALUES ...

# A database can have multiple tables and they will all be added rows simultaneously though this is untested yet
db.setTable(some_table)

# Adding columns to a table can either be done in batch (like below) or one by one
# Columns have a name and a generator, they can also be the primary key (the pk comes into play when override is enabled and rows will be overriden by removing the row by the PK column)
some_table.addColumns([
	Column("id", SerialGenerator(1), True),
	Column("some_data", RandomStringGenerator()),
])
# Example of adding one column
some_table.addColumn(Column("some_other_data", RandomIntegerGenerator(1e3, 1e6)))

# From here calling db.insertRow() will insert a single row, call it multiple times to insert mutliple rows
for i in range(100):
	db.insertRow()

# Can also be used to insert 200 rows to some_table
db.insertRows(some_table, 200)
```

---

## **`Database`**

**`Database(bool override, bool wipe)`**

Wipe will drop every table when `Database.setTable` is called
Override will drop replace every item which would conflict generated query (such as id's being overridden), currently deprecated by wipe

**`Database.setTable(Table table)`**

Sets the table which `Database.insertRow` will affect which is currently deprecated by `Database.insertRows()`

**`Database.connect(args) -> None`**
    
Connects to the database, arguments depend on the connection interface, see example above

**`Database.wipeTable(Table table) -> None`**
    
Drops all entries in a table, see main.py for example

**`Database.insertRows(Table table, int nRows) -> None`**

Inserts n rows into table in database, requires configured table before usage

**`Database.getPkSet(Table table) -> Set`**

Mainly used with `SetGenerator` to satisfy foreign keys to ensure a 1:1 or 1:N relationship, see example below
```py
user = Table("user")
user.addColumns([
	Column("id", SerialGenerator(1), True),
])
shirt = Table("shirt")
shirt.addColumns([
	Column("id", SerialGenerator(1), True),
	Column("user_fk", SetGenerator(db.getPkSet(user), True)),
])
```

## **`Table`**

**`Table(String name)`**

The given name must mimic the database's table name and will be used in the query

**`Table.fromCsv(String filename)`**

Reads the csv and adds as many columns as the csv, such created columns have `SetGenerator`s assigned according to the data in the csv's column

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

SetGenerator(chSet, destructive=False)
# For destructive=True entries are removed from the set as they are picked
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

FakeEmailGenerator()
# FakeEmailGenerator()
# david56@example.net
# kaufmangrace@example.com
# lisaschmidt@example.com

FakeIPv4Generator()
# FakeIPv4Generator()
# 100.239.243.174
# 212.240.225.211
# 22.42.176.240

FakeIPv6Generator()
# FakeIPv6Generator()
# b2ce:dcd2:83de:657:310a:3279:95f4:91db
# 6532:eec7:d615:7bf5:814c:3be9:9a65:606e
# be69:81ab:9d91:5896:7413:451c:24ac:a95b

FakeMacGenerator()
# FakeMacGenerator()
# 6f:6c:d4:44:0d:89
# 73:6e:6e:c8:0a:cf
# 3e:e6:83:34:43:69

FakeUriGenerator()
# FakeUriGenerator()
# http://www.smith.org/tag/home/
# https://www.gutierrez-calhoun.org/about.htm
# https://www.vincent-jennings.com/list/main/app/home.php

FakeUrlGenerator()
# FakeUrlGenerator()
# http://williams.com/
# https://waters.com/
# https://www.williams.com/

FakeUsernameGenerator()
# FakeUsernameGenerator()
# prussell
# evanmartinez
# huntbrandi

FakeCreditCardNumberGenerator()
# FakeCreditCardNumberGenerator()
# 4591224799613
# 4396095491829044
# 3520959742328224

FakeDateGenerator()
# FakeDateGenerator()
# 1996-05-08
# 1983-04-23
# 1984-06-12

FakeCurrentDecadeDateGenerator()
# FakeCurrentDecadeDateGenerator()
# 2021-04-12
# 2020-11-02
# 2020-04-11

FakeCurrentMonthDateGenerator()
# FakeCurrentMonthDateGenerator()
# 2022-01-16
# 2022-01-04
# 2022-01-17

FakeCurrentYearDateGenerator()
# FakeCurrentYearDateGenerator()
# 2022-01-06
# 2022-01-08
# 2022-01-04

FakeVehicleModelGenerator()
# FakeVehicleModelGenerator()
# Express 1500 Passenger
# Explorer Sport Trac
# Santa Fe Sport

FakeVehicleMakeGenerator()
# FakeVehicleMakeGenerator()
# Chevrolet
# Ram
# Lexus

FakeLicensePlateGenerator()
# FakeLicensePlateGenerator()
# FF1 5232
# XU2 X0Q
# PC 66274

PrettyTimeGenerator()
# PrettyTimeGenerator(imin, imax)
# 9h 55m 8s
# 4d 7h 33m 39s
# 21d 11h 2m 25s

# Note, all the datetime objects the following generators generate are automatically converted to strings for use in the query
FakeDateTimeGenerator()
# FakeDateTimeGenerator()
# 1416-09-27 10:31:54
# 1318-06-06 00:06:24
# 1701-04-08 02:42:37

FakeCurrentDecadeDateTimeGenerator()
# FakeCurrentDecadeDateTimeGenerator()
# 2020-04-09 15:18:36
# 2021-08-25 21:12:06
# 2021-08-26 18:40:42

FakeCurrentYearDateTimeGenerator()
# FakeCurrentYearDateTimeGenerator()
# 2022-01-05 18:46:21
# 2022-01-13 13:00:15
# 2022-01-16 00:20:28

FakeCurrentMonthDateTimeGenerator()
# FakeCurrentMonthDateTimeGenerator()
# 2022-01-19 08:15:51
# 2022-01-12 19:07:15
# 2022-01-03 21:36:32
```