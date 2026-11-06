# Exercício 1 — Fundamentos

alunos = {
    "Ramon": 8.5,
    "Julia": 9.2,
    "Carlos": 5.5,
    "Mariana": 7.0,
    "Pedro": 4.5
}

aprovados = {
    aluno: nota 
    for aluno, nota in alunos.items()
    if nota >= 7
}

print(aprovados)

# Exercício 2 — Aplicação

estoque = {
    "Tela": 250,
    "Bateria": 120,
    "Conector": 35,
    "Câmera": 180,
    "Película": 20
}

novos_precos = {
    produto: preco * 1.15
    for produto, preco in estoque.items()
    if preco < 200
}

print(novos_precos)
print(estoque)

# Exercício 3 — Desafio

produtos = ["Mouse", "Teclado", "Monitor", "Webc am"]
precos = [50, 120, 800, 150]

classificacao = {
    produto: "Barato" if preco < 100 
    else ("Intermediário" if preco <= 300 else "alto")
    for produto, preco in zip(produtos, precos)

}

print(classificacao)