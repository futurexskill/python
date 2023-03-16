import pytest
from processor import persist
import psycopg2

def test_my_test():
    assert 3 == 3

def test_read_from_pg():
    dbObject = persist.PersistData("postgres")
    courses = dbObject.read_from_pg("futureschema.futurex_course_catalog")
    print(len(courses[0]))
    assert 5 == len(courses[0])

def test_read_from_pg_2():
    dbObject = persist.PersistData("postgres")
    with pytest.raises(psycopg2.errors.UndefinedTable):
        dbObject.read_from_pg("futureschema.table_invalid")