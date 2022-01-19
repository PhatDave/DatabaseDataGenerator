from Generators import *


class Column:
	def __init__(self, name, generator=None, pk=False):
		self.name = name
		self.pk = pk

		self.__generator = None
		if generator is not None:
			self.assignGenerator(generator)

	def assignGenerator(self, generator):
		if not isinstance(generator, Generator):
			# TODO: Raise exception instead of return
			return
		self.__generator = generator

	def generate(self):
		return self.__generator.generate()