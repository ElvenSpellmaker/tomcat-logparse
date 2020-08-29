class TomcatDetection:
	def detect_error(self, string):
		return self.__find_string("ERROR", string) or self.__find_string("Exception:", string)

	def detect_tomcat_started(self, string):
		return self.__find_string("INFO: Server startup in:", string)

	def __find_string(self, search, subject):
		return subject.find(search) != -1
