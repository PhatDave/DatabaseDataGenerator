from Column import *


class Table:
	def __init__(self, name):
		self.name = name
		self.columns = []

	def addColumn(self, column):
		if not isinstance(column, Column):
			# TODO: Raise exception instead of return
			return
		self.columns.append(column)

	def addColumns(self, columns):
		for i in columns:
			self.addColumn(i)

	def getPkColumnName(self):
		for i in self.columns:
			if i.pk:
				return i.name
		return ""