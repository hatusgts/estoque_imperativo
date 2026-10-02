import os

from operacoes import (
    cadastrar_produto,
    consultar_produto,
    registrar_entrada,
    registrar_saida,
    listar_produtos,
    listar_criticos,
)


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


def ler_inteiro(mensagem):
    texto = input(mensagem)
    try:
        return int(texto)
    except ValueError:
        return None


def exibir_produto(codigo, produto):
    print(f"[{codigo}] {produto['nome']} - {produto['qtd']} {produto['unidade']} "
          f"(mínimo: {produto['minimo']} {produto['unidade']})")


def opcao_cadastrar():
    codigo = input("Código: ").strip()
    nome = input("Nome: ").strip()
    unidade = input("Unidade: ").strip()
    qtd_inicial = ler_inteiro("Quantidade inicial: ")
    minimo = ler_inteiro("Estoque mínimo: ")

    if qtd_inicial is None or minimo is None:
        print("Valores numéricos inválidos.")
        return

    _, msg = cadastrar_produto(codigo, nome, unidade, qtd_inicial, minimo)
    print(msg)


def opcao_consultar():
    codigo = input("Código: ").strip()
    ok, resultado = consultar_produto(codigo)
    if ok:
        exibir_produto(codigo, resultado)
    else:
        print(resultado)


def opcao_entrada():
    codigo = input("Código: ").strip()
    quantidade = ler_inteiro("Quantidade: ")
    if quantidade is None:
        print("Quantidade inválida.")
        return
    _, msg = registrar_entrada(codigo, quantidade)
    print(msg)


def opcao_saida():
    codigo = input("Código: ").strip()
    quantidade = ler_inteiro("Quantidade: ")
    if quantidade is None:
        print("Quantidade inválida.")
        return
    _, msg = registrar_saida(codigo, quantidade)
    print(msg)


def opcao_listar():
    produtos = listar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        exibir_produto(produto["codigo"], produto)


def opcao_criticos():
    criticos = listar_criticos()
    if not criticos:
        print("Nenhum produto em nível crítico.")
        return
    for produto in criticos:
        exibir_produto(produto["codigo"], produto)


def exibir_menu():
    print("\n=== Controle de Estoque ===")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Registrar entrada")
    print("4 - Registrar saída")
    print("5 - Listar produtos")
    print("6 - Listar produtos críticos")
    print("0 - Sair")


def main():
    opcoes = {
        1: opcao_cadastrar,
        2: opcao_consultar,
        3: opcao_entrada,
        4: opcao_saida,
        5: opcao_listar,
        6: opcao_criticos,
    }

    while True:
        limpar_tela()
        exibir_menu()
        opcao = ler_inteiro("Opção: ")

        if opcao == 0:
            print("Encerrando.")
            break

        acao = opcoes.get(opcao)
        if acao is None:
            print("Opção inválida.")
            pausar()
            continue

        limpar_tela()
        acao()
        pausar()


if __name__ == "__main__":
    main()
