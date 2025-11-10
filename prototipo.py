import sqlite3

#classe Cliente ligada aos objetos
class Cliente:
    def __init__(self, id, nome, email,telefone ):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        
class ClienteDAO:#classe ClienteDAO para executar as funções
    def __init__(self, db_name = "prototipo.db"):
        self.db_name = db_name
    
    def conectar(self):
        return sqlite3.connect(self.db_name)
        
    def create(self,cliente):
        con = self.conectar()
        cur = con.cursor()
        
        cur.execute(
            """CREATE TABLE IF NOT EXISTS Cliente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone INTEGER
         );
         """)
        
        cur.execute(
        "INSERT INTO Cliente (nome, email,telefone) VALUES (?,?,?)" ,(cliente.nome, cliente.email, cliente.telefone))
        
        con.commit()
        con.close()

    def read(self):
        con = self.conectar()
        cur = con.cursor()
        
        cur.execute('SELECT * FROM Cliente')
        linhas = cur.fetchall()
        lista = []
        for l in linhas:
            cliente = Cliente(l[0], l[1], l[2], l[3])
            lista.append(cliente)
            
        con.close()
        return lista

    def update(self,cliente):
        con =self.conectar()
        cur = con.cursor() 
        
        cur.execute('UPDATE Cliente SET nome = ?, email = ?, telefone = ? WHERE id = ?', (cliente.nome,cliente.email,cliente.telefone, cliente.id))
        
        con.commit()
        con.close()
       
    def delete(self,id):
         con = self.conectar()
         cur = con.cursor()
         
         cur.execute('DELETE FROM Cliente WHERE id = ?', (id,))
         
         con.commit()
         con.close()
         