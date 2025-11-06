import sqlite3


con = sqlite3.connect("teste.db")

cur = con.cursor()

cur.execute(
"""CREATE TABLE IF NOT EXISTS Cliente(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
email TEXT,
telefone INTEGER
);
""")
cur.executemany('INSERT INTO Cliente(nome,email, telefone)VALUES (?,?,?)' ,

[("carlos","carlos@gmail.com", 81900000000),
("ana","ana@gmail.com",81911111111),
("teo","teo@gmail.com",81922222222)]
)

con.commit()

cur.execute("SELECT * FROM Cliente")

res = cur.fetchall()

for dados in res:
    print(dados)


cur.execute("UPDATE Cliente SET telefone = ? WHERE nome = ?", (81933333333,"ana"))

con.commit()

cur.execute("SELECT * FROM Cliente")

res = cur.fetchall()

for dados in res:
    print(dados)

cur.execute("DELETE FROM Cliente WHERE nome = ? ", ("teo",))
con.commit()

cur.execute("SELECT * FROM Cliente")

res = cur.fetchall()

for dados in res:
    print(dados)

con.close()