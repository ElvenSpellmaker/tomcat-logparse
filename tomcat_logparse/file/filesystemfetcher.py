import os

class FileSystemFetcher:
	def watch_all(self, path, log_watcher):
		files = []
		for root, dirs, files in os.walk(path):
			for file in files:
				filepath = os.path.join(root, file)
				log_watcher.watch_file(filepath)
