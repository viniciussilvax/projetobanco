from typing import List
from time import sleep
from os import system

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
        efetuar_saque()
    elif op == 3:
        efetuar_deposito()
    elif op == 4:
        efetuar_transferencia()
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
    system('clear')


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


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta: '))

        conta: Conta = buscar_conta_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print('Conta inexistente!')
    else:
        print('Sem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta: '))

        conta: Conta = buscar_conta_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor para o depósito: '))

            conta.depositar(valor)

        else:
            print(f'Conta {conta} não encontrada!')
    else:
        print('Não existem contas cadastradas!')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_origem: int = int(input('Informe o número da sua conta: '))
        conta_origem: Conta = buscar_conta_numero(numero_origem)

        if conta_origem:
            numero_destino: int = int(input('Informe a conta destino: '))
            conta_destino: Conta = buscar_conta_numero(numero_destino)

            if conta_destino:
                valor: float = float(input('Informe o valor da transferência: '))
                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'Conta {conta_destino} não encontrada!')
        else:
            print(f'Conta {numero_origem} não encontrada!')

    else:
        print('Sem contas cadastradas!')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Contas Cadastradas: ')

        for conta in contas:
            print(conta)
            print('----------')
            sleep(1)

    else:
        print('Nenhuma conta cadastrada!')
    sleep(2)
    menu()


def buscar_conta_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
