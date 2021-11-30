from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('==============================')
    print('===========Terminal===========')
    print('==============================')

    print('Selecione uma opção: ')
    print('1 - Criar Conta')
    print('2 - Efetuar Saque')
    print('3 - Efetuar Depósito')
    print('4 - Efetuar Transferência')
    print('5 - Listar Contas')
    print('6 - Sair Sistema')

    op: int = int(input())
    if op == 1:
        criar_conta()
    elif op == 2:
        sacar()
    elif op == 3:
        depositar()
    elif op == 4:
        transferir()
    elif op == 5:
        listar_contas()
    elif op == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção Inválida')
        sleep(1)
        menu()


def criar_conta() -> None:
    print('Informe os dados do Cliente: ')
    nome: str = input('Nome Cliente: ')
    cpf: str = input('CPF Cliente: ')
    nascimento: str = input('Data Nascimento Cliente: ')

    cliente: Cliente = Cliente(nome, cpf, nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso. ')
    print('Dados Conta: ')
    print('--------------------------')
    print(conta)
    sleep(2)
    menu()


def sacar() -> None:
    pass


def depositar() -> None:
    pass


def transferir() -> None:
    pass


def listar_contas() -> None:
    pass


def buscar_conta_numero(numero: int) -> Conta:
    pass


if __name__ == '__main__':
    main()
