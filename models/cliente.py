from datetime import date
from utils.helper import data_string, string_data


class Cliente:
    counter: int = 1001

    def __init__(self: object, nome: str, cpf: str, dt_nascimento: str) -> None:
        self.__codigo: int = Cliente.counter
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__dt_nascimento: date = string_data(dt_nascimento)
        self.__dt_cadastro: date = date.today()
        Cliente.counter += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def dt_nascimento(self: object) -> str:
        return data_string(self.__dt_nascimento)

    @property
    def dt_cadastro(self: object) -> str:
        return data_string(self.__dt_cadastro)

    def __str__(self: object) -> str:
        return f'Id: {self.codigo} \nNome: {self.nome} \n' \
               f'Data Nascimento: {self.dt_nascimento} \nData Cadastro: {self.dt_cadastro}'
