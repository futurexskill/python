import logging

class FileReader:
    logging.basicConfig(level="WARNING")
    def __init__(self,fileType):
        logging.debug("I am within the FileReader constructor")
        self.file_type = fileType

    def read_file(self):
        logging.debug("Reading a " + self.file_type + " file")