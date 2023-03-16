import logging
import logging.config


class FileReader:
    logging.config.fileConfig("processor/resources/configs/logging.conf")
    logger = logging.getLogger("Ingest")
    def __init__(self,fileType):
        self.logger.info("I am within the FileReader constructor")
        self.file_type = fileType

    def read_file(self):
        self.logger.debug("Reading a " + self.file_type + " file")