# Exercício 1 — Fundamentos

def apresentar(*args):
    # for info in args: apenas um teste aleatório kkk
    #     print(info)
    print(args)

apresentar("Ramon", 26, "Piscineiro", "Jacuí")
# O resultado é um tupla pois *args empacota os argumentos posicionais em uma tupla
# Sendo assim, quanto pedimos para imprimir args, temos uma tupla como resultado

# Exercício 2 — Aplicação

produtos = ['Notebook', 'Mouse', 'Teclado']
precos = [2500, 80, 150]

dados_produtos = dict(zip(produtos, precos))

def mostrar_produtos(**kwargs):
    for produto, preco in kwargs.items():
        print(f"Produto: {produto} - Preço: {preco}")

mostrar_produtos(**dados_produtos)

# Exercício 3 — Desafio

def cadastrar_clientes(nome, idade, *args, **kwargs):
    dados_clientes = {}
    dados_clientes["cliente"] = nome
    dados_clientes["idade"] = idade
    dados_clientes["telefones"] = list(args)

    for chave, valor in kwargs.items():
        dados_clientes[chave] = valor

    print(dados_clientes)

cadastrar_clientes(
    "Ramon", 26, 
    "219888888", "359777777",
    cidade="Jacuí", profissao="Piscineiro" 
    )