class PersistData:
    def __init__(self,dbType):
        print("within persist data construcor")
        self.db_type=dbType
    def store_data(self):
        print("storing data to "+self.db_type)