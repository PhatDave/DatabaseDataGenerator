from Table import *
from Query import *


class Database:
	def __init__(self):
		self.__connection = None


class PostgreSQLDB(Database):
	import postgresql
	global postgresql

	def __init__(self, override=False):
		self.__connection = None
		self.__tables = []
		self.override = override
		# db = postgresql.open('pq://demo:demo@127.0.0.1:5432/carService')

	def connect(self, user="demo", password="demo", ip="127.0.0.1", port="5432", dbName="demo"):
		self.__connection = postgresql.open(f'pq://{user}:{password}@{ip}:{port}/{dbName}')

	def addTable(self, table):
		if not isinstance(table, Table):
			# TODO: Raise exception instead of return
			return
		self.__tables.append(table)

	def insertRow(self):
		queries = self.__generateQueries()
		for query in queries:
			try:
				self.__connection.execute(query.query)
			except postgresql.exceptions.UniqueError:
				if self.override:
					pkColumn = query.table.getPkColumnName()
					pk = query.values[query.names.index(pkColumn)]
					self.__connection.execute(f"DELETE FROM users WHERE {pkColumn}={pk};")
					self.__connection.execute(query.query)
		return

	def __generateQueries(self):
		queries = []
		for table in self.__tables:
			query = Query()
			query.generate(table)
			queries.append(query)
		return queries
