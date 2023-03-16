import logging
import logging.config

class PersistData:
    logging.config.fileConfig("resources/configs/logging.conf")
    def __init__(self,dbType):
        logging.debug("within persist data construcor")
        self.db_type=dbType
    def store_data(self):
        logging.debug("storing data to "+self.db_type)