import io

class Logfile:
	def __init__(self, path):
		self.__path = path
		print(f"Opening: '{self.__path}'")
		self.__file = open(self.__path, "r")
		self.__file.seek(0, io.SEEK_END)

	def getNewLines(self):
		print(f"Reading new lines from: '{self.__path}'")
		yield from self.__file

	def close(self):
		print(f"Closing file: '{self.__path}'")
		self.__file.close()
