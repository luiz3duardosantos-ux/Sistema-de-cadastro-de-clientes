import sqlite3
esc = 0
clientes = []
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
    def __init__(self, db_name = "Dados_Clientes.db"):
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

    def deletall(self):
         con = self.conectar()
         cur = con.cursor()
         
         cur.execute('DELETE FROM Cliente')
         
         con.commit()
         con.close()
         

dao = ClienteDAO()
while esc != 5:
    print("\n-------------MENU PRINCIPAL--------------\n")
    print("Digite 1 para criar e adicionar clientes")  
    print("Digite 2 para mostrar tabela de clientes")  
    print("Digite 3 para atualizar dados de clientes")  
    print("Digite 4 para deletar clientes")  
    print("Digite 5 para sair\n")  
    try:
        esc = int(input("Opção: "))
    except ValueError:
        pass

    if esc > 5 or esc < 1:
        print("\nPor favor, selecione uma opção valida!\n") 
    else:
        if esc == 1: 
              nome = (input("Digite o nome:"))
              email = input("Digite o email:")
              try:
                telefone = int(input("Digite o telefone:"))
              except ValueError:
                  print("\nPor favor,digite apenas numeros!")
                  telefone = int(input("Digite o telefone:"))
              p1 = Cliente(None,nome,email,telefone)
              dao.create(p1) 
              clientes.append(p1)
              print("\n------Cliente adicionado com sucesso!---------")
        if esc == 2:
            print("--------------Clientes----------")
            print("Formato: ID; nome; email; telefone")
            if len(clientes) != 0:
                 for d in dao.read():
                   print(f"{d.id}; {d.nome}; {d.email}; {d.telefone}")
                #except sqlite3.OperationalError:
                 print("Nenhum cliente adicionado!")
            else: print()
        if esc == 3:
            if len(clientes) != 0:
                try:
                    id = int(input("Digite o ID do cliente a ser alterado:"))
                    print()
                except ValueError:
                    print("ID invalido!")
                    id = int(input("Digite corretamente o ID do cliente a ser alterado:"))
                novo_nome = input("Digite novo nome:")
                novo_email = input("Digite novo email:")
                try:
                    novo_telefone = int(input("digite novo telefone:"))
                except ValueError:
                    print("apenas numeros!")
                    novo_telefone = int(input("digite novo telefone:"))
                p1 = Cliente(id,novo_nome,novo_email,novo_telefone)
                dao.update(p1)
                print("\n-------Informações alteradas com suceeso!---------")
            else: print("Nenhum cliente para ser atualizado!")
        if esc == 4:
            if len(clientes) > 0:
                try:
                    del_id = int(input("Digite o ID do cliente a ser deletado:"))
                except ValueError:
                    print("ID invalido!")
                    del_id = int(input("Digite corretamente o ID do cliente a ser deletado:"))
                dao.delete(del_id)
                print("--------Cliente deletado com sucesso!-------")
            else: print("Nenhum cliente para ser deletado!")

print("\nAÇÃO FINALIZADA!")
try:
    dao.deletall()
except sqlite3.OperationalError:
    pass