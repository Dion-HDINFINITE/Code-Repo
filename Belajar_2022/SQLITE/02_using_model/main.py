
import sqlite3

from employee import Employee

conn = sqlite3.connect('employee.db')

cur = conn.cursor()

emp0 = Employee('Anas', 'Azhar', 3000000)
emp1 = Employee('Budi', 'Suseno', 4000000)
emp2 = Employee('Cindy', 'Siregar', 5000000)

cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
    first TEXT,
    last TEXT,
    salary INTEGER
    )
    """)

cur.execute("INSERT INTO employees VALUES ('{}', '{}', '{}')".format(emp0.first, emp0.last, emp0.salary))

conn.commit()


cur.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp1.first, emp1.last, emp1.salary))

conn.commit()


cur.execute("INSERT INTO employees VALUES (:first, :last, :salary)", {"first":emp2.first, "last":emp2.last, "salary":emp2.salary})

conn.commit()

cur.execute("SELECT * FROM employees WHERE salary > :salary", {"salary":500_000})

emps = cur.fetchall()

for first, last, salary in emps:
    print(first, last, salary)
print()

conn.close()