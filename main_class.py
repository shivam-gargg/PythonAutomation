import logging


class MainClass:

	def get_logger(self):
		logger = logging.getLogger(__name__)
		file_name = logging.FileHandler('file.log')
		logger.addHandler(file_name)
		logger.setLevel(logging.INFO)
		return logger