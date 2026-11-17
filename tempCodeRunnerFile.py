def cadastrar_produto(nome, quantidade, preco):
    if not nome.strip():
        raise ValueError("Você digitou um nome vazio. tente novamente")

    if quantidade < 0:
        raise ValueError("Quantidade não pode ser um número negativo.")

    if preco < 0:
        raise ValueError("O preço não pode ser negativo.")

    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    return produto

print(cadastrar_produto("cloro", 2, -1))