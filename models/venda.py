from datetime import datetime

class Venda:
    def __init__(self, id: int):
        self.set_id(id)
        self.set_data(datetime.now())
        self.set_carrinho(True)
        self.set_total(0.0)
        self.set_id_cliente(0)

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_data(self) -> datetime:
        return self.__data

    def set_data(self, data: datetime):
        self.__data = data

    def get_carrinho(self) -> bool:
        return self.__carrinho

    def set_carrinho(self, carrinho: bool):
        self.__carrinho = carrinho

    def get_total(self) -> float:
        return self.__total

    def set_total(self, total: float):
        self.__total = total

    def get_id_cliente(self) -> int:
        return self.__id_cliente

    def set_id_cliente(self, id_cliente: int):
        self.__id_cliente = id_cliente

    def __str__(self) -> str:
        data_fmt = self.__data.strftime("%d/%m/%Y %H:%M")
        return (
            f"ID: {self.__id} - Data: {data_fmt} - "
            f"Carrinho: {self.__carrinho} - Total: R$ {self.__total:.2f} - "
            f"ID Cliente: {self.__id_cliente}"
        )

    def to_json(self) -> dict:
        return {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "carrinho": self.__carrinho,
            "total": self.__total,
            "id_cliente": self.__id_cliente,
        }

    @staticmethod
    def from_json(dic: dict) -> "Venda":
        venda = Venda(dic["id"])
        venda.set_data(datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
        venda.set_carrinho(dic["carrinho"])
        venda.set_total(dic["total"])
        venda.set_id_cliente(dic["id_cliente"])
        return venda