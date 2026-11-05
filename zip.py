# Exercício 1 — Cadastro de pessoas

nomes = ["Ramon", "Julia", "Ivo"]
idades = [26, 23, 61]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")


# Exercício 2 — Controle de estoque

produtos = ["Tela", "Bateria", "Conector"]
precos = [250, 120, 35]
quantidades = [3, 5, 10]

for produto, preco, quantidade in zip(produtos, precos, quantidades):
    print(f"{produto} - Valor: {preco}. Quantidade no estoque: {quantidade}.")
    print(f"O valor total em estoque de {produto} é R${preco * quantidade:.2f}.") # O :.2f determina que o número seja exibido com duas casas decimais.

# Exercício 3 — Construindo um dicionário

clientes = ["Carlos", "Fernanda", "Roberto"]
telefones = ["11999999999", "11988888888", "11977777777"]

for nome, telefone in dict(zip(clientes, telefones)).items():
    print(f"Cliente: {nome}. Telefone: {telefone}.")


    



