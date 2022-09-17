from ClasseSOLID import *
estoque = Estoque()
estoque.inserir("Arroz", 10, 10)
cliente = Cliente()
logarCliente = LogarCliente()
email = 'joao@gmail.com'
password = '123456'
logarCliente.logar(email, password)
venda = Carrinho(email,password)
gerente = Gerente()
print()
funcionario = Funcionario()
carrinho = Carrinho(email,password)
carrinho.addCarrinho('bala', 5)
carrinho.addCarrinho('Arroz', 1)
carrinho.calcularTotal()
print(carrinho.getCarrinho())
compra = Compra(email,password)
compra.finalizarCompra('123.456.789-00', carrinho.calcularTotal(), carrinho.getCarrinho())

# cliente.inserir('João', '123.456.789-00', 'joao@gmail.com','123456','(00) 0000-0000','SP','São Paulo',
#                     '00000-000','Bairro X', 'Rua dos Bobos', 123, 'A')


