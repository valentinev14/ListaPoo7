class Categoria:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)
    
    def __str__(self):
        return f"{self.__id} - {self.__descricao}"
    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    
    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Descrição deve ser informada")
        self.__descricao = descricao
    
    def get_id(self): return self.__id
    
    def get_descricao(self): return self.__descricao
    
    def to_json(self):
        dic = {}
        dic["id"] = self.__id
        dic["descricao"] = self.__descricao
        return dic
    
    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"])