import sqlite3

#clase para simular erro
class Cliente_concorrente:
    def __init__(self,nome):
        self.nome = nome


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
         

#-------------testando clientes---------------------

dao = ClienteDAO()

#clientes funcionais
p1 = Cliente(None,"Robesval", "robesval@gmail.com", 12345)
p2 = Cliente(None,"Clodovil","clodovio@gmail.com", 98765)
p3 = Cliente(None,"Marivalda","marivalda@gmail.com", 4002)
p4 = Cliente(None,"Aderbal","aderbal@gmail.com",8002)

#para inclui-los no banco de dados
#dao.create(p1)
#dao.create(p2)
#dao.create(p3)
#dao.create(p4)

#objetos incorretos
o5 = Cliente|Cliente_concorrente("intruso1")
o6 = Cliente|Cliente_concorrente("intruso2")

#lista para adicionar apenas clientes corretos
clientes = [p1,p2,p3,p4,o5,o6]

