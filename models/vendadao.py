from venda import Venda

import json

class VendaDAO:
    arquivo = "vendas.json"
    objetos = []

    @classmethod
    def inserir(cls, obj: Venda):
        cls.abrir()
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[Venda]:
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id: int) -> Venda | None:
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: Venda):
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            aux.set_data(obj.get_data())
            aux.set_carrinho(obj.get_carrinho())
            aux.set_total(obj.get_total())
            aux.set_id_cliente(obj.get_id_cliente())
            cls.salvar()

    @classmethod
    def excluir(cls, id: int):
        id_busca = id.get_id() if isinstance(id, Venda) else id
        aux = cls.listar_id(id_busca)
        if aux is not None:
            cls.objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open(cls.arquivo, mode="r", encoding="utf-8") as f:
                dados = json.load(f)
                for dic in dados:
                    cls.objetos.append(Venda.from_json(dic))
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open(cls.arquivo, mode="w", encoding="utf-8") as f:
            json.dump([obj.to_json() for obj in cls.objetos], f, indent=4, ensure_ascii=False)