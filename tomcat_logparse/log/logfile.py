import io

class Logfile:
	def __init__(self, path):
		self.__path = path
		print(f"Opening: '{self.__path}'")
		self.__file = open(self.__path, "r")
		self.__file.seek(0, io.SEEK_END)

	def get_new_lines(self):
		print(f"Reading new lines from: '{self.__path}'")
		yield from self.__file

	def new_file_path(self, path):
		print(f"File changed path from: '{self.__path}' to '{path}'")
		self.__path = path

	def close(self):
		print(f"Closing file: '{self.__path}'")
		self.__file.close()
