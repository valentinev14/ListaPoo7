from models.vendaitem import VendaItem

import json

class VendaItemDAO:
    arquivo = "vendaitens.json"
    objetos = []

    @classmethod
    def inserir(cls, obj: VendaItem):
        cls.abrir()
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[VendaItem]:
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id: int) -> VendaItem | None:
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: VendaItem):
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            aux.set_qtd(obj.get_qtd())
            aux.set_preco(obj.get_preco())
            aux.set_id_venda(obj.get_id_venda())
            aux.set_id_produto(obj.get_id_produto())
            cls.salvar()

    @classmethod
    def excluir(cls, id: int):
        id_busca = id.get_id() if isinstance(id, VendaItem) else id
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
                    cls.objetos.append(VendaItem.from_json(dic))
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open(cls.arquivo, mode="w", encoding="utf-8") as f:
            json.dump([obj.to_json() for obj in cls.objetos], f, indent=4, ensure_ascii=False)