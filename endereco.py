from project.models.enums import unidadeFederativa



class Endereco:

    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: unidadeFederativa) -> None:
        
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
 