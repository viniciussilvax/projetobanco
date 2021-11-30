from models.cliente import Cliente
from utils.helper import formato_moeda


class Conta:
    id: int = 10

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.id
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.id += 1

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> float:
        self.__limite = valor

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    def __str__(self: object) -> str:
        return f'ID Conta: {self.numero}\nCliente: {self.cliente.nome}\nSaldo Total: {formato_moeda(self.saldo_total)}'
