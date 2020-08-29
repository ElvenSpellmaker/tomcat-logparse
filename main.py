#!/bin/python -tt

import sys

from watchdog.observers import Observer

from tomcat_logparse.file.filesystemfetcher import FileSystemFetcher
from tomcat_logparse.file.filesystemhandler import FileSystemHandler
from tomcat_logparse.file.filesystemobserver import FileSystemObserver
from tomcat_logparse.log.errorlogger import ErrorLogger
from tomcat_logparse.log.logwatcher import LogWatcher
from tomcat_logparse.tomcat.tomcatlogger import TomcatLogger

if len(sys.argv) > 3:
	raise Exception('Please provide a maximum of one directory to scan and one logfile to log into!')

src_path = sys.argv[1] if len(sys.argv) >= 2 else '/tmp/tomcat-logs'
logfile = sys.argv[2] if len(sys.argv) == 3 else '/tmp/errchecker-log.txt'

observer = Observer()

log_watcher = LogWatcher()

# Sets up the handler the observer sends events to
# Adds the Tomcat logger to the handler
error_logger = ErrorLogger(logfile)
tomcat_logger = TomcatLogger(error_logger)
handler = FileSystemHandler(log_watcher, tomcat_logger)

# Get files in the directory and populate LogWatcher instance
files = FileSystemFetcher().watch_all(src_path, log_watcher)

# Observe the filesystem for any changes in the filesystem
FileSystemObserver(src_path, observer, handler).run()
