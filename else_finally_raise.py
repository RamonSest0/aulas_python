# Exercício 1 — Conversão e confirmação

def converter_valor(valor):
    try:
        valor_convertido = float(valor)
    except ValueError:
        print("Você digitou uma valor inválido. Tente um número inteiro.")
        return False
    else: 
        print(f"Conversão realizada com sucesso! O valor convertido é: {valor_convertido:.2f}.")
        return valor_convertido
    finally:
        print("Processo de conversão encerrado.")

# Exercício 2 — Cadastro de produto

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

# Exercício 3 — Retirada de estoque

estoque = {
    "cloro": 10,
    "algicida": 5,
    "elevador_de_ph": 8
}

def retirar_estoque(estoque, produto, quantidade):

    if produto not in estoque:
        raise KeyError("Nome do produto inválido.")

    if quantidade <= 0:
        raise ValueError("A quantidade não pode ser igual ou menor que 0.")

    if quantidade > estoque[produto]:
        raise ValueError(f"Estoque insuficiente. Há apenas {estoque[produto]} no estoque.")

    estoque[produto] -= quantidade
    return estoque

try:
    retirar_estoque(estoque, "cloro", -1)
except ValueError as error:
    print(error)
except KeyError as error:
    print(error)
else: 
    print("Retirada feita com sucesso.")




    