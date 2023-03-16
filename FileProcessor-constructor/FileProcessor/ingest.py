class FileReader:
    def __init__(self,fileType):
        print("I am within the FileReader constructor")
        self.file_type = fileType

    def read_file(self):
        print("Reading a " + self.file_type + " file")