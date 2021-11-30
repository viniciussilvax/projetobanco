from datetime import datetime, date


def data_string(data: date) -> str:
    """ Muda a data para o formata pt-br """
    return data.strftime('%d/%m/%Y')


def string_data(data: str) -> date:
    """ Muda a data gerada para string """
    return datetime.strptime(data, '%d/%m/%Y')


def formato_moeda(valor: float) -> str:
    """ Formata o valor real informado em estilo moeda """
    return f'R$ {valor:,.2f}'
