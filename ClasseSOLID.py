import sqlite3

class ConectandoBD:
    def __init__(self):
        self.__conexao = None
        self.cursor = None
    def conectar(self):
        self.__conexao = sqlite3.connect('eccomerceSOLID.db')
        self.cursor = self.__conexao.cursor()
    def desconectar(self):
        self.__conexao.commit()
        self.__conexao.close()

    def criarTabelas(self, nomeTabela: str, colunas: str):
        self.conectar()
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {nomeTabela}(
        {colunas}
        );
        ''')
        self.desconectar()

class Estoque(ConectandoBD):
    def __init__(self):
        super().__init__()
        self.nomeLoja = "Spartan's Store"
        self.endereco = "Rua X, 0"
        self.telefone = "(00) 0000-0000"
        self.cnpj = "01. 234. 567/0001-89"
        self.criarTabelas('ESTOQUE', 'nomeProduto TEXT PRIMARY KEY, qtd INTEGER NOT NULL, valor REAL NOT NULL')
    def inserir(self, nome: str, quantidade: int,preco: float):
        try:
            self.conectar()
            itens = (nome, quantidade, preco)
            self.cursor.execute(f'''
            INSERT INTO ESTOQUE (nomeProduto, qtd, valor) VALUES {itens};
            ''')
            self.desconectar()
        except sqlite3.IntegrityError:
            print('Produto já cadastrado!')
            self.desconectar()
    def adicionarQtd(self, nome: str, quantidade: int):
        try:
            self.conectar()
            self.cursor.execute(f'''
            UPDATE ESTOQUE SET qtd = qtd + {quantidade} WHERE nomeProduto = '{nome}';
            ''')
            self.desconectar()
        except sqlite3.IntegrityError:
            print('Produto não cadastrado!')
            self.desconectar()
    def listar(self):
        self.conectar()
        self.cursor.execute('SELECT * FROM ESTOQUE;')
        retorno = self.cursor.fetchall()
        for linha in retorno:
            print(linha)
        self.desconectar()
        return retorno

    def listarItemEspecifico(self, nome: str):
        self.conectar()
        self.cursor.execute(f'''
        SELECT * FROM ESTOQUE WHERE nomeProduto = '{nome}';
        ''')
        retorno = self.cursor.fetchall()[0]
        for linha in self.cursor.fetchall():
            print(linha)
        self.desconectar()
        return retorno

    def deletar(self, nome: str):
        self.conectar()
        self.cursor.execute(f'''
        DELETE FROM ESTOQUE WHERE nomeProduto = '{nome}';
        ''')
        self.desconectar()
    def atualizar(self,nome: str, quantidade: int,preco: float):
        try:
            self.conectar()
            self.cursor.execute(f'''
            UPDATE ESTOQUE SET nomeProduto = '{nome}', valor = {preco}, qtd = {quantidade} WHERE nomeProduto = '{nome}';
            ''')
            self.desconectar()
        except sqlite3.IntegrityError:
            print('Produto não cadastrado!')
            self.desconectar()

class Cliente(ConectandoBD):
    def __init__(self):
        super().__init__()
        self.criarTabelas('CLIENTE', '''nome TEXT NOT NULL, cpf TEXT NOT NULL PRIMARY KEY, email TEXT NOT NULL,
        password TEXT NOT NULL, telefone TEXT NOT NULL, estado TEXT NOT NULL, cidade TEXT NOT NULL,
        cep TEXT NOT NULL, bairro TEXT NOT NULL, rua TEXT NOT NULL, numero INTEGER NOT NULL,
        complemento TEXT NOT NULL''')
    def inserir(self, nome: str, cpf: str, email: str, password: str, telefone: str, estado: str, cidade: str,
                cep: str, bairro: str, rua: str, numero: int, complemento: str):
        try:
            self.conectar()
            self.cursor.execute(f'''
            INSERT INTO cliente(nome,cpf,email,password,telefone,estado,cidade,cep,bairro,rua,numero,
            complemento) VALUES ('{nome}','{cpf}','{email}','{password}','{telefone}','{estado}','{cidade}','{cep}','{bairro}',
            '{rua}',{numero},'{complemento}');
            ''')
            self.desconectar()
        except sqlite3.IntegrityError:
            print('Cliente já cadastrado!')

    def atualizar(self, nome: str, cpf: str, email: str, password: str, telefone: str, estado: str, cidade: str,
                cep: str, bairro: str, rua: str, numero: int, complemento: str):
        try:
            self.conectar()
            self.cursor.execute(f'''
            UPDATE cliente SET nome = '{nome}', email = '{email}', password = '{password}', telefone = '{telefone}',
            estado = '{estado}', cidade = '{cidade}', cep = '{cep}', bairro = '{bairro}', rua = '{rua}', numero = {numero},
            complemento = '{complemento}' WHERE cpf = '{cpf}';
            ''')
            self.desconectar()
        except sqlite3.IntegrityError:
            print('Cliente não cadastrado!')

    def listar(self):
        self.conectar()
        self.cursor.execute('SELECT * FROM cliente;')
        retorno = self.cursor.fetchall()
        for linha in self.cursor.fetchall():
            print(linha)
        self.desconectar()
        return retorno

    def listarEspecifico(self, cpf: str):
        self.conectar()
        self.cursor.execute(f'''
        SELECT * FROM cliente WHERE cpf = '{cpf}';
        ''')
        retorno = self.cursor.fetchall()[0]
        for linha in self.cursor.fetchall():
            print(linha)
        self.desconectar()
        return retorno

    def deletar(self, cpf: str):
        self.conectar()
        self.cursor.execute(f'''
        DELETE FROM cliente WHERE cpf = '{cpf}';
        ''')
        self.desconectar()


class Funcionario(ConectandoBD):
    def __init__(self):
        super().__init__()
        self.salario = float(2000)
        self.criarTabelas('FUNCIONARIO', '''nome TEXT NOT NULL, cpf TEXT NOT NULL PRIMARY KEY, email TEXT NOT NULL,
        ocupacao TEXT NOT NULL, salario REAL NOT NULL, cep TEXT NOT NULL, rua TEXT NOT NULL, numero INTEGER NOT NULL,
        complemento TEXT NOT NULL''')

    def calcularSalario(self, cpf: str):
        salario = self.salario * 0.8
        return salario

    def inserir(self, nome: str, cpf: str, email: str, ocupacao: str, cep: str, rua: str, numero: int,
                complemento: str):
        try:
            self.conectar()
            self.cursor.execute(f'''
            INSERT INTO funcionario(nome,cpf,email,ocupacao,salario,cep,rua,numero,complemento) VALUES ('{nome}','{cpf}',
             '{email}','{ocupacao}',{self.salario},'{cep}','{rua}',{numero},'{complemento}');''')
            self.desconectar()
        except sqlite3.IntegrityError:
            print('Funcionário já cadastrado!')

    def listar(self):
        self.conectar()
        self.cursor.execute('SELECT * FROM funcionario;')
        for linha in self.cursor.fetchall():
            print(linha)
        self.desconectar()
    def deletar(self, cpf: str):
        self.conectar()
        self.cursor.execute(f'''
        DELETE FROM funcionario WHERE cpf = '{cpf}';
        ''')
        self.desconectar()

class Gerente(Funcionario):
    def __init__(self):
        super().__init__()
        self.criarTabelas('GERENTE', '''nome TEXT NOT NULL, cpf TEXT NOT NULL PRIMARY KEY, email TEXT NOT NULL,
        ocupacao TEXT NOT NULL, salario REAL NOT NULL, cep TEXT NOT NULL, rua TEXT NOT NULL, numero INTEGER NOT NULL,
        complemento TEXT NOT NULL''')

    def calcularSalario(self, cpf: str):
        salario = self.salario * 4
        return salario

    # def inserir(self, nome: str, cpf: str, email: str, ocupacao: str, salario: float, cep: str, rua: str, numero: int,
    #             complemento: str):
    #     try:
    #         self.conectar()
    #         self.cursor.execute(f'''
    #         INSERT INTO FUNCIONARIO (nome,cpf,email,ocupacao,salario,cep,rua,numero,complemento) VALUES ('{nome}','{cpf}',
    #          '{email}','{ocupacao}',{salario},'{cep}','{rua}',{numero},'{complemento}');''')
    #         self.desconectar()
    #     except sqlite3.IntegrityError:
    #         print('Gerente já cadastrado!')

    # def listar(self):
    #     self.conectar()
    #     self.cursor.execute('SELECT * FROM FUNCIONARIO;')
    #     for linha in self.cursor.fetchall():
    #         print(linha)
    #     self.desconectar()
    # def deletar(self, cpf: str):
    #     self.conectar()
    #     self.cursor.execute(f'''
    #     DELETE FROM FUNCIONARIO WHERE cpf = '{cpf}';
    #     ''')
    #     self.desconectar()

class LogarCliente(Cliente):
    def __init__(self):
        super().__init__()

    def logar(self, email: str, password: str):
        self.conectar()
        self.cursor.execute(f'''
        SELECT * FROM cliente WHERE email = '{email}' AND password = '{password}';
        ''')
        retorno = self.cursor.fetchall()
        if len(retorno) == 0:
            # print('Cliente não cadastrado!')
            self.desconectar()
            return False
        else:
            # print('Cliente logado com sucesso!')
            ...
        self.desconectar()
        return retorno
    def deslogar(self):
        return False

class Carrinho(Estoque,LogarCliente):
    def __init__(self,email,password):
        super().__init__()
        self.__carrinho = {}
        self.__logado = False
        if LogarCliente.logar(self, email, password):
            self.__logado = True

    def addCarrinho(self, produto: str, quantidade: int):
        if self.__logado:
            try:
                itemEstoque = self.listarItemEspecifico(produto)
                preco = itemEstoque[2]
                qtdeEstoque = itemEstoque[1] - quantidade
                if qtdeEstoque >= 0:
                    if self.__carrinho.get(produto) is None:
                        self.__carrinho[produto] = quantidade
                    else:
                        self.__carrinho[produto] += quantidade
                    self.atualizar(produto, qtdeEstoque, preco)
                else:
                    print('Quantidade indisponível no estoque!')
            except IndexError:
                print('Produto não cadastrado!')

    def removerItem(self, produto: str, quantidade: int):
        if self.__logado:
            if self.__carrinho.get(produto) is None:
                print('Produto não está no carrinho!')
            else:
                itemEstoque = self.listarItemEspecifico(produto)
                preco = itemEstoque[2]
                qtdeEstoque = itemEstoque[1] + quantidade
                self.atualizar(produto, qtdeEstoque, preco)
                del self.__carrinho[produto]

    def getCarrinho(self):
        if self.__logado:
            return self.__carrinho

    def limparCarrinho(self):
        if self.__logado:
            self.__carrinho = {}

    def calcularTotal(self):
        if self.__logado:
            total = 0
            for produto, quantidade in self.__carrinho.items():
                itemEstoque = self.listarItemEspecifico(produto)
                preco = itemEstoque[2]
                total += preco * quantidade
            print(f'Total: R${total}')
            return total

class Descontos(Carrinho):
    def __init__(self,email,password):
        super().__init__(email,password)
        self.__desconto = 0

    def desconto(self, cpf: str):
        # if self.__logado:
        cliente = self.listarEspecifico(cpf)
        if cliente[1] == 'GERENTE':
            self.__desconto = 0.2
        elif cliente[1] == 'FUNCIONARIO':
            self.__desconto = 0.1
        else:
            self.__desconto = 0

    def getDesconto(self):
        # if self.__logado:
        return self.__desconto

class Compra(Descontos):
    def __init__(self,email,password):
        super().__init__(email,password)
        self.cpf = self.logar(email,password)[0][1]
        print(self.cpf)
    def finalizarCompra(self, cpf: str, total: float, carrinho: dict):
        if self.cpf == cpf:
            cliente = self.listarEspecifico(cpf)
            desc = self.getDesconto()
            totalPagar = total - (total * desc)

            if cliente != []:
                print('Cliente encontrado!')
                print(f'{cliente[0]} pagará R${totalPagar:.2f}')
                print('-' * 50)
                print('Nota fiscal:')
                for produto, quantidade in carrinho.items():
                    print(f'{produto} - {quantidade}')
                print(f'Total: R${total:.2f}')
                print('-' * 50)
                print('Finalizando compra...')
                print(f'Enviando compra para o CEP {cliente[7]} da rua {cliente[8]} nº {cliente[9]} complemento '
                      f'{cliente[10]}')
                print('Compra finalizada!')
                self.limparCarrinho()
            else:
                print('Cliente não encontrado!')

