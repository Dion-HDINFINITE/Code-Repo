import sqlite3

connection = sqlite3.connect("employee.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
    first TEXT,
    last TEXT,
    salary INTEGER
    )
    """)

# cursor.execute("INSERT INTO employees VALUES ('anisa', 'azhari', 8000000)") #CREATE

# for row in emps:
#     print(row)

cursor.execute("SELECT * FROM employees WHERE last='azhari'")

emps = cursor.fetchone()
print(emps)

connection.commit()

connection.close()