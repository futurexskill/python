import logging
import logging.config

class PersistData:
    logging.config.fileConfig("resources/configs/logging.conf")
    logger = logging.getLogger("Persist")

    def __init__(self,dbType):
        self.logger.debug("within persist data construcor")
        self.db_type=dbType
    def store_data(self):

        try:
            self.logger.debug("storing data to "+self.db_type)
            var1 = 100/0
        except Exception as exp:
            self.logger.error("An error has occured "+str(exp))