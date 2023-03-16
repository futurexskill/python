import logging
class PersistData:
    logging.basicConfig(level="WARNING")
    def __init__(self,dbType):
        logging.debug("within persist data construcor")
        self.db_type=dbType
    def store_data(self):
        logging.debug("storing data to "+self.db_type)