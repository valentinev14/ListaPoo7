class VendaItem:
    def __init__(self, id: int, q: int, p: float):
        self.set_id(id)
        self.set_qtd(q)
        self.set_preco(p)
        self.set_id_venda(0)
        self.set_id_produto(0)

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_qtd(self) -> int:
        return self.__qtd

    def set_qtd(self, qtd: int):
        self.__qtd = qtd

    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco: float):
        self.__preco = preco

    def get_id_venda(self) -> int:
        return self.__id_venda

    def set_id_venda(self, id_venda: int):
        self.__id_venda = id_venda

    def get_id_produto(self) -> int:
        return self.__id_produto

    def set_id_produto(self, id_produto: int):
        self.__id_produto = id_produto

    def __str__(self) -> str:
        return (
            f"ID: {self.__id} - Qtd: {self.__qtd} - "
            f"Preço: R$ {self.__preco:.2f} - ID Venda: {self.__id_venda} - "
            f"ID Produto: {self.__id_produto}"
        )

    def to_json(self) -> dict:
        return {
            "id": self.__id,
            "qtd": self.__qtd,
            "preco": self.__preco,
            "id_venda": self.__id_venda,
            "id_produto": self.__id_produto,
        }

    @staticmethod
    def from_json(dic: dict) -> "VendaItem":
        item = VendaItem(dic["id"], dic["qtd"], dic["preco"])
        item.set_id_venda(dic["id_venda"])
        item.set_id_produto(dic["id_produto"])
        return item