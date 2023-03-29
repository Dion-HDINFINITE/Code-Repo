import sqlite3

class Settings:

    CONN = sqlite3.connect('employee.db')
    CUR = CONN.cursor()


    MENU = """
    (1) SHOW ALL EMPLOYEES
    (2) ADD NEW EMPLOYEE
    (3) FIND EMPLOYEE BY NAME
    (4) UPDATE SALARY EMPLOYEE
    (5) REMOVE EMPLOYEE
    (Q) EXIT.
    """