import io

class ErrorLogger:
	def __init__(self, path):
		self.__path = path
		print(f"Opening: '{self.__path}' for appending")
		self.__file = open(self.__path, "a")

	def log(self, line):
		if not line.endswith("\n"):
			line = line + "\n"

		self.__file.write(line)

	def close(self):
		print(f"Closing file: '{self.__path}'")
		self.__file.close()
