# Exercício 1 — Cadastro e consulta

clientes = ["Carlos", "Mariana", "Roberto", "Ana"]
idades = [32, 25, 41, 19]

dados = {
    chave: valor 
    for chave, valor in zip(clientes, idades)
}

def consultar_cliente(nome, dados):

    if nome in dados:
        return print(f"O cliente {nome} tem {dados[nome]} anos de idade.")

    return print(dados.get(nome, "Cliente não encontrado")) 

consultar_cliente("Roberto", dados)
consultar_cliente("Ramon", dados)

# Exercício 2 — Cadastro flexível

produtos = {}

def cadastrar_produto(nome, preco, *args, **kwargs):
    produtos["nome"] = nome
    produtos["preco"] = preco

    for chave, valor in kwargs.items():
        produtos[chave] = valor

    produtos["extras"] = list(args)

cadastrar_produto("Mouse", 68.00, "leve", "frágil", marca="Razer", categoria="Barato")
print(produtos)

# Exercício 3 — Relatório de vendas

vendas = {
    "Carlos": 1500,
    "Mariana": 2300,
    "Roberto": 900,
    "Ana": 3100,
    "Pedro": 1200
}

top_vendedores = {
    chave: valor 
    for chave, valor in vendas.items()
    if valor >= 1500
}

comissao = {
    chave: valor * 0.10 - valor # gambiarra - calculando comissao e depois removendo o valor da soma - ficando apenas valor da comissao - melhor valor * 0.10
    for chave, valor in top_vendedores.items()
}

print(top_vendedores)
print(comissao)