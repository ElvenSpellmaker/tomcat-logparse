import time

class FileSystemObserver:
	def __init__(self, src_path, observer, handler):
		self.__src_path = src_path
		self.__event_handler = handler
		self.__event_observer = observer

	def run(self):
		self.start()
		try:
			while True:
				time.sleep(1)
		except KeyboardInterrupt:
			self.stop()

	def start(self):
		self.__schedule()
		self.__event_observer.start()

	def stop(self):
		self.__event_observer.stop()
		self.__event_observer.join()
		self.__event_handler.close_all()

	def __schedule(self):
		self.__event_observer.schedule(
			self.__event_handler,
			self.__src_path,
			recursive=True
		)
