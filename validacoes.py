from dados import estoque


def codigo_existe(codigo):
    return codigo in estoque


def quantidade_valida(quantidade):
    return isinstance(quantidade, int) and not isinstance(quantidade, bool) and quantidade > 0


def saldo_suficiente(codigo, quantidade):
    return estoque[codigo]["qtd"] >= quantidade
