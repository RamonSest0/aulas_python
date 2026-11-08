# Exercício 1 — Manipulação do estoque
estoque = [
    {
        "nome": "Mouse",
        "preco": 68.00,
        "quantidade": 15
    },
    {
        "nome": "Teclado",
        "preco": 150.00,
        "quantidade": 8
    },
    {
        "nome": "Monitor",
        "preco": 750.00,
        "quantidade": 4
    }
]

estoque.append({
    "nome": "Headset",
    "preco": 120.00,
    "quantidade": 10
})

estoque.extend([
    {
    "nome": "GPU",
    "preco": 1200.00,
    "quantidade": 5
},

    {
    "nome": "Cooler",
    "preco": 50.00,
    "quantidade": 18
}
])

estoque.insert(1, {
    "nome": "Webcam",
    "preco": 40.00,
    "quantidade": 21
})

for produto in estoque:
    if produto["nome"] == "Monitor":
        estoque.remove(produto)
        break

print(len(estoque))

# Exercício 2 — Consultas e ordenação

nomes_produtos = []

for produto in estoque:
    nomes_produtos.append(produto["nome"])

nomes_produtos_ordenada = nomes_produtos.copy()

nomes_produtos_ordenada.sort()
nomes_produtos.reverse()

if "Mouse" in nomes_produtos:
    print(f"Mouse está na lista e aparece {nomes_produtos.count("Mouse")} vez(es)")

print(nomes_produtos)
print(nomes_produtos_ordenada)

# Exercício 3 — Referências e cópias

from copy import deepcopy

estoque_copia = deepcopy(estoque)

for produto in estoque_copia:
    if produto["nome"] == "Mouse":
        produto["preco"] = 70.00
        break

print(estoque)
print(estoque_copia)

# alteramos as duas listas porque fizemos uma cópia rasa da nossa lista
# as estruturas de dados internas (nesse caso dicts) ainda apontam para o mesmo objeto na memória
# Por isso ao alterar a cópia alteramos a principal tbm

# com deepcopy() resolvemos esse problema :)





