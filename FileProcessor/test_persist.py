import unittest
from processor import persist
import psycopg2
import json

class PersistDataTest(unittest.TestCase):
    def test_read_from_pg(self):
        dbObject = persist.PersistData("postgres")
        courses = dbObject.read_from_pg("futureschema.futurex_course_catalog")
        print(len(courses[0]))
        self.assertEqual(len(courses[0]),5)

    def test_read_from_pg_2(self):
        dbObject = persist.PersistData("postgres")

        with self.assertRaises(psycopg2.errors.UndefinedTable):
            dbObject.read_from_pg("futureschema.table_invalid")

    def test_write_from_json_to_pg(self):
        dbObject = persist.PersistData("postgres")

        with self.assertRaises(KeyError):
            dbObject.write_from_json_to_pg("futureschema.futurex_course_catalog",
                                           {})

    def test_write_from_json_to_pg_2(self):
        dbObject = persist.PersistData("postgres")
        course_json = json.dumps({"course_name": "New course 20", "author_name": "futurex","course_section": {"section1": ' \
                      '"Value", "section2": "Value3"},"creation_date": "2021-03-20"} )

        dbObject.write_from_json_to_pg("futureschema.futurex_course_catalog",
                                           course_json)

if __name__ == '__main__':
    unittest.main()