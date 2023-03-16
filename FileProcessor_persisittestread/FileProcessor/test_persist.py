import unittest
from processor import persist
import psycopg2

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


if __name__ == '__main__':
    unittest.main()