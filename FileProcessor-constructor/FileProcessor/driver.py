import ingest
import persist

print("This is my driver program")

class DriverProgram:
    def __init__(self,fileType):
        print("I am within the constructor")
        self.file_type = fileType
    def my_function(self):
        print("inside my function . Processing "+self.file_type + " file")
        reader = ingest.FileReader(self.file_type)
        writer = persist.PersistData("postgres")
        reader.read_file()
        writer.store_data()

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    print("Entering the main method")
    print_hi('PyCharm')
    driver = DriverProgram("csv")
    driver.my_function()


