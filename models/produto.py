class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_categoria(id_categoria)
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - R$ {self.__preco:.2f} - {self.__estoque} - {self.__id_categoria}"
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Descrição deve ser informada")
        self.__descricao = descricao
    def set_preco(self, preco):
        if preco < 0: raise ValueError("Preço não pode ser negativo")
        self.__preco = preco
    def set_estoque(self, estoque):
        if estoque < 0: raise ValueError("Estoque não pode ser negativo")
        self.__estoque = estoque
    def set_id_categoria(self, id_categoria):
        if id_categoria <= 0: raise ValueError("Categoria deve ser informada")
        self.__id_categoria = id_categoria
    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_preco(self): return self.__preco
    def get_estoque(self): return self.__estoque
    def get_id_categoria(self): return self.__id_categoria
    def to_json(self):
        dic = {}
        dic["id"] = self.__id
        dic["descricao"] = self.__descricao
        dic["preco"] = self.__preco
        dic["estoque"] = self.__estoque
        dic["id_categoria"] = self.__id_categoria
        return dic
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["id_categoria"])
