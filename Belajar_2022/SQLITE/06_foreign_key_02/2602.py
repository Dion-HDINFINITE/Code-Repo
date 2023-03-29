import sqlite3

conn = sqlite3.Connection("2602.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    street TEXT,
    city TETX,
    state TEXT,
    credit_limit REAL
)
""")

cur.execute("""
CREATE TABLE customers(
VALUES
('Pedro Augusto da Rocha', 'Rua Pedro Carlos Hoffman', 'Porto Alegre', 'RS', 700.00),
('Antonio Carlos', 'Av. Pinherios', 'Belo Horizonte', 'MG', 350.00),
('Luiza Augusta Mhor', 'Rua Salto Grande', 'Niteroi', 'RJ', 4000,00),
('Jane Ester', 'Av 7 de setembro', 'Erechim', 'RS', 800.00),
('Marcos Antônio dos Santos', 'Av Farrapos', 'Porto Alegre', 'RS', 4250.25)
)
""")

conn.commit()
conn.close()