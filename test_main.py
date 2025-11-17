import unittest 
from main import Cliente, clientes 
#classe para testar o cadastro de clientes 
class Test_prot(unittest.TestCase): 
    def test_inst(self): 
        for d in clientes: 
            with self.subTest(nome=d.nome): 
                print(d.nome) 
                self.assertIsInstance(d,Cliente) 
if __name__ == "__main__": unittest.main()