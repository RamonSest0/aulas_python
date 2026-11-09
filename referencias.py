# Exercício 1 — Identificando referências

def adicionar(lista):
    lista.append("Mouse")

def substituir(lista):
    lista = ["Webcam", "Headset"]


produtos = ["Teclado", "Monitor"]

adicionar(produtos)
print(produtos) # ["Teclado", "Monitor", "Mouse"]
# Temos esse resultado porque na função modificamos a nossa lista original, afinal recebemos como parâmetro
# uma referência a lista original

substituir(produtos)
print(produtos) # ["Teclado", "Monitor", "Mouse"]
# Nesse segundo caso, dentro da função, não alteramos a lista original, apenas fizemos uma atribuição
# onde lista recebe ["Webcam", "Headset"].
# Interessante notar que o VScode deixa isso bem claro
# pois a lista fica apagada dentro dela, mesmo usando o mesmo nome...

# Exercício 2 — O efeito colateral

def aumentar_precos(produtos):
    for produto in produtos:
        produto["preco"] += 10


estoque = [
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 100}
]

aumentar_precos(estoque)

print(estoque) # conseguimos alterar porque estamos trabalhando com a referência a lista original, fazendo uma modificação em um objeto mutável interno na lista original
# nesse caso um diccionário. É diferente de fazer 
# produtos = ...

# Exercício 3 — Um desafio de raciocínio

def adicionar_produto(produtos):
    produtos.append(
        {"nome": "Fone", "preco": 65}
    )

novo_estoque = estoque.copy()

adicionar_produto(novo_estoque)

print(novo_estoque)
print(estoque)



