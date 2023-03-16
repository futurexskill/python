import logging
import logging.config


class FileReader:
    logging.config.fileConfig("resources/configs/logging.conf")
    def __init__(self,fileType):
        logging.info("I am within the FileReader constructor")
        self.file_type = fileType

    def read_file(self):
        logging.debug("Reading a " + self.file_type + " file")