from tomcat_logparse.log.logfile import Logfile

class LogWatcher:
	def __init__(self):
		self.__files = {}

	def watch_file(self, path):
		logfile = Logfile(path)
		self.__files[path] = logfile

	def get_file(self, path):
		if not path in self.__files:
			raise Exception(f"File '{path}' is not open!")

		return self.__files[path]

	def close_file(self, path):
		if not path in self.__files:
			raise Exception(f"File '{path}' is not open!")

		self.__files[path].close()
		del self.__files[path]

	def close_all(self):
		for file in list(self.__files):
			self.close_file(file)
