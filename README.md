        DOCUMENTAÇÃO PROJETO 4 SISTEMA CADASTRO DE CLIENTES
--------Entrega_2---Foco em padrão DAO------------

Classe Cliente: ligada diretamente aos objetos

class Cliente:
    class Cliente:
    def __init__(self, id, nome, email,telefone ):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone


Classe ClienteDAO: para cumprir os métodos CRUD e conectar com o banco de dados
------init e método conctar-----------------
def __init__(self, db_name = "prototipo.db"):
        self.db_name = db_name
    
    def conectar(self):
        return sqlite3.connect(self.db_name)



--------------CRUD(ja imbutidos com método conectar)---------

-------------------CREATE-----------------
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


--------READ--------------------------

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

---------UPDATE-------------------------

def update(self,cliente):
        con =self.conectar()
        cur = con.cursor() 
        
        cur.execute('UPDATE Cliente SET nome = ?, email = ?, telefone = ? WHERE id = ?', (cliente.nome,cliente.email,cliente.telefone, cliente.id))
        
        con.commit()
        con.close()


   ---------DELETE-------------------------

def delete(self,id):
         con = self.conectar()
         cur = con.cursor()
         
         cur.execute('DELETE FROM Cliente WHERE id = ?', (id,))
         
         con.commit()
         con.close()
