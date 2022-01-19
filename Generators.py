import random
import re
import string
from faker import Faker


class Generator:
	def __init__(self):
		pass

	def generate(self):
		pass


class RandomGenerator(Generator):
	class EmptyStringException(Exception):
		pass

	def __init__(self, length=10, hasLowercase=True, hasUppercase=False,
				 hasDigits=False):
		self.length = length
		self.hasLowercase = hasLowercase
		self.hasDigits = hasDigits
		self.hasUppercase = hasUppercase

	def generate(self):
		self.__validateChoices()
		choice = self.__getChoices()
		ran = ''.join(random.choices(choice, k=self.length))
		return ran

	def __getChoices(self):
		choice = ""
		if self.hasLowercase:
			choice += string.ascii_lowercase
		if self.hasUppercase:
			choice += string.ascii_uppercase
		if self.hasDigits:
			choice += string.digits
		return choice

	def __validateChoices(self):
		if (
				not self.hasLowercase and not self.hasUppercase and not self.hasDigits):
			raise self.EmptyStringException(
				"Random string can not be empty!")


class RandomIntegerGenerator(RandomGenerator):
	def __init__(self, imin, imax):
		super().__init__()
		self.imin = int(imin)
		self.imax = int(imax)

	def generate(self):
		ran = random.randint(self.imin, self.imax)
		return int(ran)


class SerialGenerator(Generator):
	def __init__(self, start=0, step=1):
		self.start = start
		self.step = step
		self.current = start

	def generate(self):
		output = self.current
		self.current += self.step
		return output


class SetGenerator(Generator):
	def __init__(self, chSet):
		self.chSet = list(chSet)

	def generate(self):
		return random.choice(self.chSet)


class FakeFirstNameGenerator(Generator):
	def __init__(self):
		self.__faker = Faker()

	def generate(self):
		name = self.__faker.first_name()
		return name


class FakeLastNameGenerator(Generator):
	def __init__(self):
		self.__faker = Faker()

	def generate(self):
		name = self.__faker.last_name()
		return name


class FakeNameGenerator(Generator):
	def __init__(self):
		self.__faker = Faker()

	def generate(self):
		name = f"{self.__faker.first_name()} {self.__faker.last_name()}"
		return name


class FakeCityGenerator(Generator):
	def __init__(self):
		self.__faker = Faker()

	def generate(self):
		name = self.__faker.city()
		return name
