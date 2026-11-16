from service import Service
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 99:
            try:
                op = UI.menu()
                if op == 1: UI.cliente_inserir()
                if op == 2: UI.cliente_listar()
                if op == 3: UI.cliente_atualizar()
                if op == 4: UI.cliente_excluir()
                if op == 5: UI.categoria_inserir()
                if op == 6: UI.categoria_listar()
                if op == 7: UI.categoria_atualizar()
                if op == 8: UI.categoria_excluir()
                if op == 9: UI.produto_inserir()
                if op == 10: UI.produto_listar()
                if op == 11: UI.produto_atualizar()
                if op == 12: UI.produto_excluir()
                if op == 13: UI.produto_reajustar()
            except ValueError as erro:
                print("Erro:", erro)
    @staticmethod
    def menu():
        print("Clientes: 1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir")
        print("Categorias: 5 - Inserir, 6 - Listar, 7 - Atualizar, 8 - Excluir")
        print("Produtos: 9 - Inserir, 10 - Listar, 11 - Atualizar, 12 - Excluir")
        print("Outros: 13 - Reajustar preços, 99 - Fim")
        return int(input("Informe a opção: "))

    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        Service.cliente_inserir(nome, email, fone)
    @staticmethod
    def cliente_listar():
        for c in Service.cliente_listar():
            print(c)
    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        Service.cliente_atualizar(id, nome, email, fone)
    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id a ser excluído: "))
        Service.cliente_excluir(id)


    @staticmethod
    def categoria_inserir():
        descricao = input("Informe a descrição: ")
        Service.categoria_inserir(descricao)
    @staticmethod
    def categoria_listar():
        for c in Service.categoria_listar():
            print(c)
    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        Service.categoria_atualizar(id, descricao)
    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id a ser excluído: "))
        Service.categoria_excluir(id)


    @staticmethod
    def produto_inserir():
        UI.categoria_listar()
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe o estoque: "))
        id_categoria = int(input("Informe o id da categoria: "))
        Service.produto_inserir(descricao, preco, estoque, id_categoria)
    @staticmethod
    def produto_listar():
        for p in Service.produto_listar():
            print(p)
    @staticmethod
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o id a ser atualizado: "))
        UI.categoria_listar()
        descricao = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe o novo estoque: "))
        id_categoria = int(input("Informe o novo id da categoria: "))
        Service.produto_atualizar(id, descricao, preco, estoque, id_categoria)
    @staticmethod
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o id a ser excluído: "))
        Service.produto_excluir(id)
    @staticmethod
    def produto_reajustar():
        percentual = float(input("Informe o percentual (ex: 10 reajuste, -15 promoção): "))
        Service.produto_reajustar(percentual)

UI.main()
