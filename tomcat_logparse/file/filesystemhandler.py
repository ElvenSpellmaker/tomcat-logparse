from watchdog.events import FileSystemEventHandler

class FileSystemHandler(FileSystemEventHandler):
	def __init__(self, log_watcher, output_logger):
		self.__log_watcher = log_watcher
		self.__output_logger = output_logger

	def on_created(self, event):
		if event.is_directory:
			return

		self.__log_watcher.watch_file(event.src_path)

	def on_modified(self, event):
		if event.is_directory:
			return

		for line in self.__log_watcher.get_file(event.src_path).get_new_lines():
			self.__output_logger.parse_line(line)

	def on_deleted(self, event):
		self.__log_watcher.close_file(event.src_path)

	def on_moved(self, event):
		self.__log_watcher.new_file_path(event.src_path, event.dest_path)

	def close_all(self):
		self.__log_watcher.close_all()
		self.__output_logger.close()
