from Table import *
from Query import *


class Database:
	def __init__(self):
		self.__connection = None


class PostgreSQLDB(Database):
	import postgresql
	global postgresql

	def __init__(self, override=False, wipe=False):
		self.__connection = None
		self.__table = None
		self.__wipe = wipe
		self.__override = override

	def connect(self, user="demo", password="demo", ip="127.0.0.1",
				port="5432", dbName="demo"):
		self.__connection = postgresql.open(
			f'pq://{user}:{password}@{ip}:{port}/{dbName}')

	def setTable(self, table: Table):
		self.__table = table
		if self.__wipe:
			self.wipeTable(table)

	def wipeTable(self, table: Table):
		self.__connection.execute(f"DELETE FROM {table.name} *;")

	def insertRow(self):
		query = self.__generateQuery()
		try:
			self.__connection.execute(query.query)
		except postgresql.exceptions.UniqueError:
			if self.__override:
				pkColumn = query.table.getPkColumnName()
				pk = query.values[query.names.index(pkColumn)]
				self.__connection.execute(
					f"DELETE FROM {query.table.name} WHERE {pkColumn}={pk};")
				self.__connection.execute(query.query)
		return

	def __generateQuery(self):
		query = Query()
		query.generate(self.__table)
		return query

	def getPkSet(self, table: Table):
		test = self.__connection.prepare(
			f"SELECT {table.getPkColumnName()} FROM {table.name}")
		arr = test()
		arr = [i[0] for i in arr]
		return set(arr)
