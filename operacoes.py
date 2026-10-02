from dados import estoque
from validacoes import codigo_existe, quantidade_valida, saldo_suficiente


def cadastrar_produto(codigo, nome, unidade, qtd_inicial, minimo):
    if codigo_existe(codigo):
        return (False, "Produto já cadastrado.")

    if not quantidade_valida(qtd_inicial) and qtd_inicial != 0:
        return (False, "A quantidade inicial deve ser um inteiro maior ou igual a zero.")

    if not isinstance(minimo, int) or isinstance(minimo, bool) or minimo < 0:
        return (False, "O estoque mínimo deve ser um inteiro maior ou igual a zero.")

    estoque[codigo] = {
        "nome": nome,
        "unidade": unidade,
        "qtd": qtd_inicial,
        "minimo": minimo,
    }
    return (True, "Produto cadastrado com sucesso.")


def consultar_produto(codigo):
    if not codigo_existe(codigo):
        return (False, "Produto não cadastrado.")

    return (True, estoque[codigo])


def registrar_entrada(codigo, quantidade):
    if not codigo_existe(codigo):
        return (False, "Produto não cadastrado.")

    if not quantidade_valida(quantidade):
        return (False, "A quantidade deve ser um inteiro maior que zero.")

    estoque[codigo]["qtd"] += quantidade
    return (True, "Entrada registrada com sucesso.")


def registrar_saida(codigo, quantidade):
    if not codigo_existe(codigo):
        return (False, "Produto não cadastrado.")

    if not quantidade_valida(quantidade):
        return (False, "A quantidade deve ser um inteiro maior que zero.")

    if not saldo_suficiente(codigo, quantidade):
        saldo_atual = estoque[codigo]["qtd"]
        return (False, f"Saída recusada: há apenas {saldo_atual} em estoque.")

    estoque[codigo]["qtd"] -= quantidade

    if estoque[codigo]["qtd"] <= estoque[codigo]["minimo"]:
        return (True, "Saída registrada. ATENÇÃO: nível crítico.")

    return (True, "Saída registrada com sucesso.")


def listar_produtos():
    return [
        {"codigo": codigo, **dados}
        for codigo, dados in estoque.items()
    ]


def listar_criticos():
    return [
        {"codigo": codigo, **dados}
        for codigo, dados in estoque.items()
        if dados["qtd"] <= dados["minimo"]
    ]
