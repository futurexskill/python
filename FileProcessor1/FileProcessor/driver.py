import ingest
import persist

print("This is my driver program")

class DriverProgram:
    def my_function(self):
        print("inside my function")

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print("Entering the main method")
    print_hi('PyCharm')
    driver = DriverProgram()
    driver.my_function()
    reader = ingest.FileReader()
    writer = persist.PersistData()
    reader.read_file()
    writer.store_data()

