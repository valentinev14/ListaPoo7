from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.categoria import Categoria
from models.categoriadao import CategoriaDAO
from models.produto import Produto
from models.produtodao import ProdutoDAO
from models.venda import Venda
from models.vendadao import VendaDAO
from models.vendaitem import VendaItem
from models.vendaitemdao import VendaItemDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(c)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)


    @staticmethod
    def categoria_inserir(descricao):
        c = Categoria(0, descricao)
        CategoriaDAO().inserir(c)
    @staticmethod
    def categoria_listar():
        return CategoriaDAO().listar()
    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO().listar_id(id)
    @staticmethod
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO().atualizar(c)
    @staticmethod
    def categoria_excluir(id):
        CategoriaDAO().excluir(id)


    @staticmethod
    def produto_inserir(descricao, preco, estoque, id_categoria):
        p = Produto(0, descricao, preco, estoque, id_categoria)
        ProdutoDAO().inserir(p)
    @staticmethod
    def produto_listar():
        return ProdutoDAO().listar()
    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO().listar_id(id)
    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        p = Produto(id, descricao, preco, estoque, id_categoria)
        ProdutoDAO().atualizar(p)
    @staticmethod
    def produto_excluir(id):
        ProdutoDAO().excluir(id)
    @staticmethod
    def produto_reajustar(percentual):
        for p in ProdutoDAO().listar():
            p.set_preco(round(p.get_preco() * (1 + percentual / 100), 2))
            ProdutoDAO().atualizar(p)

    @staticmethod
    def venda_inserir(id_cliente):
        if ClienteDAO().listar_id(id_cliente) is None:
            raise ValueError("Cliente não encontrado")
        v = Venda(0)
        v.set_id_cliente(id_cliente)
        VendaDAO().inserir(v)

    @staticmethod
    def venda_listar():
        return VendaDAO().listar()

    @staticmethod
    def venda_listar_id(id):
        return VendaDAO().listar_id(id)

    @staticmethod
    def venda_atualizar(id, data, carrinho, total, id_cliente):
        if ClienteDAO().listar_id(id_cliente) is None:
            raise ValueError("Cliente não encontrado")
        v = Venda(id)
        v.set_data(data)
        v.set_carrinho(carrinho)
        v.set_total(total)
        v.set_id_cliente(id_cliente)
        VendaDAO().atualizar(v)

    @staticmethod
    def venda_excluir(id):
        for item in VendaItemDAO().listar():
            if item.get_id_venda() == id:
                VendaItemDAO().excluir(item.get_id())
        VendaDAO().excluir(id)

    @staticmethod
    def venda_recalcular_total(id_venda):
        venda = VendaDAO().listar_id(id_venda)
        if venda is not None:
            total = 0.0
            for item in VendaItemDAO().listar():
                if item.get_id_venda() == id_venda:
                    total += item.get_qtd() * item.get_preco()
            venda.set_total(round(total, 2))
            VendaDAO().atualizar(venda)

    @staticmethod
    def vendaitem_inserir(qtd, id_venda, id_produto):
        if VendaDAO().listar_id(id_venda) is None:
            raise ValueError("Venda não encontrada")
        produto = ProdutoDAO().listar_id(id_produto)
        if produto is None:
            raise ValueError("Produto não encontrado")
        vi = VendaItem(0, qtd, produto.get_preco())
        vi.set_id_venda(id_venda)
        vi.set_id_produto(id_produto)
        VendaItemDAO().inserir(vi)
        Service.venda_recalcular_total(id_venda)

    @staticmethod
    def vendaitem_listar():
        return VendaItemDAO().listar()

    @staticmethod
    def vendaitem_listar_id(id):
        return VendaItemDAO().listar_id(id)

    @staticmethod
    def vendaitem_atualizar(id, qtd, id_venda, id_produto):
        item_atual = VendaItemDAO().listar_id(id)
        if item_atual is None:
            raise ValueError("Item de venda não encontrado")
        if VendaDAO().listar_id(id_venda) is None:
            raise ValueError("Venda não encontrada")
        produto = ProdutoDAO().listar_id(id_produto)
        if produto is None:
            raise ValueError("Produto não encontrado")
        id_venda_anterior = item_atual.get_id_venda()
        vi = VendaItem(id, qtd, produto.get_preco())
        vi.set_id_venda(id_venda)
        vi.set_id_produto(id_produto)
        VendaItemDAO().atualizar(vi)
        Service.venda_recalcular_total(id_venda_anterior)
        if id_venda != id_venda_anterior:
            Service.venda_recalcular_total(id_venda)

    @staticmethod
    def vendaitem_excluir(id):
        item = VendaItemDAO().listar_id(id)
        if item is not None:
            id_venda = item.get_id_venda()
            VendaItemDAO().excluir(id)
            Service.venda_recalcular_total(id_venda)
