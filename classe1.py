import sqlite3

conn = sqlite3.connect('eccomerce.db')
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE IF NOT EXISTS ESTOQUE (
        nomeProduto TEXT NOT NULL PRIMARY KEY,
        qtd INTEGER NOT NULL,
        valor REAL NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CLIENTE (
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL PRIMARY KEY,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        telefone TEXT NOT NULL,
        estado TEXT NOT NULL,
        cidade TEXT NOT NULL,
        cep TEXT NOT NULL,
        bairro TEXT NOT NULL,
        rua TEXT NOT NULL,
        numero INTEGER NOT NULL,
        complemento TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS FUNCIONARIO (
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL PRIMARY KEY,
        email TEXT NOT NULL,
        ocupacao TEXT NOT NULL,
        salario REAL NOT NULL,
        cep TEXT NOT NULL,
        rua TEXT NOT NULL,
        numero INTEGER NOT NULL,
        complemento TEXT NOT NULL
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()


class Ecommerce:
    def __init__(self):
        # Ecommerce de Relógios ou Roupas
        self.nomeLoja = "Spartan's Store"
        self.endereco = "Rua dos Bobos, 0"
        self.telefone = "(00) 0000-0000"
        self.cnpj = "01. 234. 567/0001-89"



        # del self.carrinho[item]

    def obterListaDeItens(self):
        conn = sqlite3.connect('eccomerce.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM ESTOQUE
        """)
        # lendo os dados
        conn.commit()

        listaDeItens = cursor.fetchall()
        for linha in cursor.fetchall():
            print(linha)
        # if self.listaDeItens == {}:
        #     mensagem = 'Carinho vazio'
        #     return mensagem
        # listaDeItens = [i for i in self.listaDeItens]
        return listaDeItens

    def obterListaDeItensEspecifico(self, item: str):
        conn = sqlite3.connect('eccomerce.db')
        cursor = conn.cursor()

        cursor.execute(f"""
        SELECT * FROM ESTOQUE where nomeProduto = '{item}'
        """)
        # lendo os dados
        conn.commit()

        listaDeItens = cursor.fetchall()
        for linha in cursor.fetchall():
            print(linha)
        # if self.listaDeItens == {}:
        #     mensagem = 'Carinho vazio'
        #     return mensagem
        # listaDeItens = [i for i in self.listaDeItens]
        return listaDeItens

    def atualizarListaDeItensEspecifico(self):
        conn = sqlite3.connect('eccomerce.db')
        cursor = conn.cursor()

        cursor.execute(f"""
        SELECT * FROM ESTOQUE
        """)
        # lendo os dados
        conn.commit()

        listaDeItens = cursor.fetchall()
        for linha in cursor.fetchall():
            print(linha)
        self.listaDeItens = listaDeItens
        print(self.listaDeItens)

    def cadastrarItem(self, item: str, qtd: int, valor: float):
        try:
            conn = sqlite3.connect('eccomerce.db')
            cursor = conn.cursor()
            itens = (item, qtd, valor)
            # inserindo dados na tabela
            cursor.execute(f"""
            INSERT INTO ESTOQUE (nomeProduto, qtd, valor)
            VALUES {itens}""")

            # gravando no bd

            conn.commit()

            print('Dados inseridos com sucesso.')

            conn.close()
            self.atualizarListaDeItensEspecifico()
        except sqlite3.IntegrityError:
            print(f'Item {item} já cadastrado')

    def adicionarItem(self, item: str, qtd: int):
        try:
            conn = sqlite3.connect('eccomerce.db')
            cursor = conn.cursor()
            cadastrado = self.obterListaDeItensEspecifico(item)[0]
            qtd = cadastrado[1] + qtd
            # inserindo dados na tabela
            cursor.execute(f"""
            UPDATE ESTOQUE 
            SET nomeProduto = ?, qtd = ?
            WHERE nomeProduto = ?""",
            (item, qtd,item))

            # gravando no bd
            conn.commit()
            print('Dados inseridos com sucesso.')
            conn.close()
            self.atualizarListaDeItensEspecifico()
        except IndexError:
            print(f'Item {item} não cadastrado')

    def removerItem(self, item: str):
        conn = sqlite3.connect('eccomerce.db')
        cursor = conn.cursor()
        # inserindo dados na tabela
        cursor.execute(f"""
        DELETE FROM ESTOQUE WHERE nomeProduto = '{item}'
        """)

        # gravando no bd
        conn.commit()

        print('Dados inseridos com sucesso.')

        conn.close()
        self.atualizarListaDeItensEspecifico()

    def cadastrarCliente(self, nome: str, cpf: str, email: str, password: str, telefone: str, estado: str, cidade: str, cep: str, bairro: str, rua: str, numero: int, complemento: str):
        try:
            conn = sqlite3.connect('eccomerce.db')
            cursor = conn.cursor()
            cliente = (nome, cpf, email, password, telefone, estado, cidade, cep, bairro, rua, numero, complemento)
            # inserindo dados na tabela
            cursor.execute(f"""
            INSERT INTO CLIENTE (nome, cpf, email, password, telefone, estado, cidade, cep, bairro, rua, numero, complemento)
            VALUES {cliente}""")

            # gravando no bd

            conn.commit()

            print('Dados inseridos com sucesso.')

            conn.close()
        except sqlite3.IntegrityError:
            print(f'Cliente {nome} já cadastrado')

    def atualizarCliente(self, nome: str, cpf: str, email: str, password: str,
                         telefone: str ,estado: str, cidade: str,cep: str, bairro: str, rua: str, numero: int,
                         complemento: str):
        try:
            conn = sqlite3.connect('eccomerce.db')
            cursor = conn.cursor()
            itens = (nome, cpf, email,password, telefone,estado,cidade,cep,bairro,rua,numero, complemento)

            # inserindo dados na tabela
            cursor.execute(f"""
            INSERT INTO CLIENTE (nome, cpf, email,password, telefone,estado,cidade,cep,bairro,rua,numero, complemento)
            VALUES {itens}""")

            # gravando no bd

            conn.commit()

            print('Cliente cadastrado com sucesso.')

            conn.close()
        except sqlite3.IntegrityError:
            print(f'Cliente {nome} já cadastrado')

    def obterListaDeClientes(self):
        conn = sqlite3.connect('eccomerce.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM CLIENTE
        """)
        # lendo os dados
        conn.commit()

        listaDeItens = cursor.fetchall()
        for linha in cursor.fetchall():
            print(linha)
        return listaDeItens

    def obterCliente(self, cpf: str):
        conn = sqlite3.connect('eccomerce.db')
        cursor = conn.cursor()

        cursor.execute(f"""
        SELECT * FROM CLIENTE WHERE cpf = '{cpf}'
        """)
        # lendo os dados
        conn.commit()

        listaDeItens = cursor.fetchall()
        for linha in cursor.fetchall():
            print(linha)
        return listaDeItens [0]

    def deletarCliente(self, cpf: str):
        conn = sqlite3.connect('eccomerce.db')
        cursor = conn.cursor()

        cursor.execute(f"""
        DELETE FROM CLIENTE WHERE cpf = '{cpf}'
        """)
        conn.commit()


    def cadastrarFuncionario(self, nome: str, cpf: str, email: str,ocupacao: str, salario: float, cep: str, rua: str,
                             numero: int, complemento: str):
        try:
            conn = sqlite3.connect('eccomerce.db')
            cursor = conn.cursor()
            itens = (nome, cpf, email,ocupacao, salario, cep, rua, numero, complemento)

            # inserindo dados na tabela
            cursor.execute(f"""
            INSERT INTO FUNCIONARIO (nome, cpf, email,ocupacao, salario, cep, rua, numero, complemento)
            VALUES {itens}""")

            # gravando no bd

            conn.commit()

            print('Funcionario cadastrado com sucesso.')

            conn.close()
        except sqlite3.IntegrityError:
            print(f'Funcionario {nome} já cadastrado')

    def excluirFuncionario(self, cpf: str):
        conn = sqlite3.connect('eccomerce.db')
        cursor = conn.cursor()

        cursor.execute(f"""
        DELETE FROM FUNCIONARIO WHERE cpf = '{cpf}'
        """)
        conn.commit()

class Comprar:
    def __init__(self):
        self.eccomerce = Ecommerce()
        self.listaDeItens = self.eccomerce.obterListaDeItens()
        self.carrinho = {}


    def logar(self, email: str, password: str):
        conn = sqlite3.connect('eccomerce.db')
        cursor = conn.cursor()
        cursor.execute(f'''
        SELECT * FROM cliente WHERE email = '{email}' AND password = '{password}';
        ''')
        retorno = cursor.fetchall()
        if len(retorno) == 0:
            # print('Cliente não cadastrado!')
            conn.commit()
            return False
        else:
            # print('Cliente logado com sucesso!')
            ...
        conn.commit()
        return retorno
    def deslogar(self):
        return False

    def getTotalItem(self, item: str) -> float:
        try:
            item = self.eccomerce.obterListaDeItensEspecifico(item)[0]
            precoTotal = float(item[2])
            return precoTotal
        except:
            print(f'Item {item} não está no estoque')


    def verCarrinho(self):
        if self.carrinho == {}:
            mensagem = 'Carinho vazio'
            return mensagem
        listaDeItens = '*'*100

        for i in self.carrinho:
            precoItem = self.getTotalItem(i)
            listaDeItens += f'\n\n{self.carrinho[i]} {i}: R${precoItem} X {self.carrinho[i]} = R${precoItem * self.carrinho[i]}\n'
        listaDeItens += f'\nTOTAL: R${self.calcularTotalDaCompra()}\n\n{"*"*100}'
        return listaDeItens


    def calcularTotalDaCompra(self) -> float:
        total = 0.0
        for item in self.carrinho:
            qtdItem = self.carrinho[item]
            item = self.eccomerce.obterListaDeItensEspecifico(item)[0]
            try:
                precoTotal = float(item[2]) * qtdItem
                total += precoTotal
            except:
                ...
        return total

    def cancelarCompra(self):
        for item in self.carrinho:
            qtd = self.carrinho[item]
            self.eccomerce.adicionarItem(item, qtd)
        self.carrinho = {}

    def addItemCarrinho(self, item: str, qtd: int):
        try:
            estoque = self.eccomerce.obterListaDeItensEspecifico('bala')[0]
            if estoque[1] - qtd < 0:
                print(f'Não temos {qtd} {item}(s) em estoque')
            else:
                self.eccomerce.adicionarItem(item, -qtd)

                self.carrinho[item] = qtd
        except IndexError:
            print(f'Item {item} não está no estoque')

    def removerItemCarrinho(self, item: str, qtd: int):
        try:
            valorCarrinho = self.carrinho[item]
            valorCarrinho -= qtd
            if valorCarrinho <= 0:
                self.eccomerce.adicionarItem(item, self.carrinho[item])
                del self.carrinho[item]
            else:
                self.eccomerce.adicionarItem(item, qtd)
        except KeyError:
            print(f'Item {item} não está no carrinho')

    def enviarPedido(self, cpf: str):
        atributosCliente = self.eccomerce.obterCliente(cpf)
        print(self.verCarrinho())
        print(f'\nPedido enviado para o cliente {atributosCliente[0]} no endereço:\n\n'
              f'Estado: {atributosCliente[5]}\nCidade: {atributosCliente[6]}\nCEP: {atributosCliente[7]}\n'
              f'Bairro: {atributosCliente[8]}\nRua: {atributosCliente[9]}\nNúmero: {atributosCliente[10]}\n'
              f'Complemento: {atributosCliente[11]}')
        print(f'\nSerá enviado um email para {atributosCliente[2]} com mais detalhes da entrega')