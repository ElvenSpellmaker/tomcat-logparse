from tomcat_logparse.tomcat.tomcatdetection import TomcatDetection

class TomcatLogger:
	def __init__(self, logger):
		self.__tomcat_detection = TomcatDetection()
		self.__logger = logger
		self.__exceptions_counter = 0

	def parseLine(self, line):
		if self.__tomcat_detection.detect_error(line):
			print(f"Exception found: {line}")
			self.__logger.log(f"Exception found: {line}")
			self.__exceptions_counter += 1
			return

		if self.__tomcat_detection.detect_tomcat_started(line):
			print(f"TOMCAT IS STARTED - Exceptions: {self.__exceptions_counter}")
			self.__logger.log(f"TOMCAT IS STARTED - Exceptions: {self.__exceptions_counter}")
			self.__exceptions_counter = 0
			return

	def close(self):
		self.__logger.close()
