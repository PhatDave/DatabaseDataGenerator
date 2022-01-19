from Table import *


class Database:
	def __init__(self):
		self.__connection = None


class PostgreSQLDB(Database):
	import postgresql
	global postgresql

	def __init__(self):
		self.__connection = None
		self.__tables = []
		# db = postgresql.open('pq://demo:demo@127.0.0.1:5432/carService')

	def connect(self, user="demo", password="demo", ip="127.0.0.1", port="5432", dbName="demo"):
		self.__connection = postgresql.open(f'pq://{user}:{password}@{ip}:{port}/{dbName}')

	def addTable(self, table):
		if not isinstance(table, Table):
			# TODO: Raise exception instead of return
			return
		self.__tables.append(table)

	def insertRow(self):
		queries = self.__generateQuery()
		values = self.__generateValues()
		for i, query in enumerate(queries):
			value = values[i]
			mkemp(value)
		return

	def __generateQuery(self):
		queries = []
		for table in self.__tables:
			queries.append(f"INSERT INTO {table.name}({self.__generateColumnNames(table)}) VALUES ({self.__enumerateColumns(table)})")
		return queries

	def __generateColumnNames(self, table):
		names = ""
		for i in table.columns:
			names += i.name + ","
		names = names[:-1]
		return names

	def __enumerateColumns(self, table):
		names = ""
		for i in range(1, table.columns.__len__() + 1):
			names += f"${i},"
		names = names[:-1]
		return names

	def __generateValues(self):
		values = []
		for table in self.__tables:
			tvalues = []
			for column in table.columns:
				tvalues.append(column.generate())
			values.append(tvalues)
		return values
