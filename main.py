from classe1 import Ecommerce, Comprar
a = Ecommerce()
b = Comprar()

# a.cadastrarCliente('João', '123.456.789-00', 'joao@gmail.com','123456','(00) 0000-0000','SP','São Paulo',
#                    '00000-000','Bairro X', 'Rua dos Bobos', 123, 'A')
# a.cadastrarItem('bala', 100,0.5)
b.addItemCarrinho('bala', 5)
a.cadastrarCliente('Maria', '000.123.456-78', 'joao@gmail.com','123456','(00) 0000-0000','SP','São Paulo',
                   '00000-000','Bairro X', 'Rua dos Bobos', 123, 'A')

print(a.obterListaDeClientes())
print(a.obterCliente('123.456.789-00'))
print(b.enviarPedido('123.456.789-00'))
# a.adicionarItem('bala', 100)
# a.addItemCarrinho('bala', 5)
# a.addItemCarrinho('Celular', 1)
# a.removerItemCarrinho('bala', 6)
# print(a.verCarrinho())
# print(a.calcularTotalDaCompra())
# a.cancelarCompra()
# a.removerItemCarrinho('bala', 5)
# print(a.obterListaDeItens())
# a.cadastrarItem('bala', 50, 0.1)
# a.cadastrarItem('Celular', 100, 1500)
# print(a.obterListaDeItensEspecifico('bala'))
# a.adicionarItem('bala', 10)
# print(a.obterListaDeItens())
#
# # a.removerItem('bala')
# print(a.obterListaDeItens())
# print(a.calcularTotalDaCompra())




