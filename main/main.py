

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    my_course={"BD":"A Big Data Hadoop Spark Project",
               "ML":'Machine Learning Model Deployment',
               "java": 'A Java Spring Boot Microservices project'}
    print(my_course["java"])
    my_course['spark'] = "PySpark coding Framework"
    print(my_course)
    my_course['spark'] = "Spark Scala coding Framework"
    print(my_course)
    del my_course['ML']
    print(my_course)
    course_exist = my_course.get("spark")
    if course_exist:
        print(course_exist)
    else:
        print("Course does not exist")




if __name__ == '__main__':
    print_hi('PyCharm ..')

