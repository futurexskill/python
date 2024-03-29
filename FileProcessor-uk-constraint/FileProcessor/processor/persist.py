import logging
import logging.config
import configparser
import psycopg2

class PersistData:
    logging.config.fileConfig("processor/resources/configs/logging.conf")
    logger = logging.getLogger("Persist")
    config = configparser.ConfigParser()
    config.read('processor/resources/fileprocessor.ini')

    def __init__(self,dbType):
        self.logger.debug("within persist data construcor")
        self.db_type=dbType
    def store_data(self):

        try:
            target_table = self.config.get("DATABASE_CONFIGS","PG_TABLE")
            self.logger.debug("target table name is "+target_table)
            self.logger.debug("storing data to "+self.db_type)
            self.write_to_pg(target_table)
            self.read_from_pg(target_table)

        except Exception as exp:
            self.logger.error("An error has occured "+str(exp))

    def write_to_pg(self,target_table):
        connection = psycopg2.connect(user='postgres',
                                      password='admin',
                                      host='localhost',
                                      database='postgres')

        cursor = connection.cursor()

        print("Inserting to PG")

        cursor.execute("select max(course_id) from "+target_table)
        max_course_id = cursor.fetchone()[0]
        print("max_course_id is "+str(max_course_id))

        insert_query = "INSERT INTO "+target_table \
                       + " (course_id, course_name, author_name, course_section" \
                       ", creation_date) VALUES (%s, %s, %s, %s,%s)"

        insert_tuple = (max_course_id+1, 'Java Microservices 2', 'FutureX', '{}', '2020-10-20')

        cursor.execute(insert_query, insert_tuple)

        cursor.close()

        connection.commit()


    def read_from_pg(self,target_table):
        connection = psycopg2.connect(user='postgres',
                                      password='admin',
                                      host='localhost',
                                      database='postgres')

        cursor = connection.cursor()

        select_query = "select * from "+target_table

        cursor.execute(select_query)

        #print(cursor.fetchone())
        records = cursor.fetchall()
        for item in records:
            print(item)
            print("Printed a record")

        cursor.close()

        connection.commit()


