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

	def new_file_path(self, src_path, dest_path):
		if not src_path in self.__files:
			raise Exception(f"File '{src_path}' is not open!")

		log = self.__files[src_path]
		del self.__files[src_path]
		self.__files[dest_path] = log

		log.new_file_path(dest_path)

	def close_file(self, path):
		if not path in self.__files:
			raise Exception(f"File '{path}' is not open!")

		self.__files[path].close()
		del self.__files[path]

	def close_all(self):
		for file in list(self.__files):
			self.close_file(file)
