from models import Base, Pedido, ItemPedido
from database import engine
from control import PedidoControl

# Criar tabelas no banco, se não existirem
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    control = PedidoControl()

    pedido1 = Pedido(cliente='Katerina')
    pedido1.itens = [
        ItemPedido(produto='Cadeira', quantidade=3, preco=600.00,categoria="moveis"),
        ItemPedido(produto='Caneta', quantidade=10, preco=10.00,categoria="papelaria"),
        ItemPedido(produto='Borracha', quantidade=5, preco=5.00,categoria="papelaria")

    ]

    
    control.salvar_pedido(pedido1)

    pedido2 = Pedido(cliente='Irina')
    pedido2.itens = [
        ItemPedido(produto='Iphone', quantidade=1, preco=5000.00,categoria="eletronicos"),
        ItemPedido(produto='Carro', quantidade=1, preco=10000.0,categoria="carros"),
        ItemPedido(produto='fone de ouvido', quantidade=2, preco=500,categoria="eletronicos"),
        ItemPedido(produto='camisa', quantidade=1, preco=100.00,categoria="roupas")

    ]

    
    control.salvar_pedido(pedido2)

    print("============== lista de pedidos apos realizar o pedido do Katerina e da Irina ===========")
    pedidos = control.listar_pedidos_com_itens()
    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente} ")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}")
    

    control.deletar_pedido(pedido2)

    print("============== lista de pedidos apos deletar o pedido da Irina ===========")
    pedidos = control.listar_pedidos_com_itens()
    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente} ")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}")
    

    control.atualizar_pedido(pedido1, "Sasha");

    print("============== lista de pedidos apos atualizar o pedido do Katerina que vira Sasha ===========")
    pedidos = control.listar_pedidos_com_itens()
    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente} ")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}")
    


    control.fechar()


