# Exercício 1 — Calculadora de serviços

def calcular_servico(valor, desconto):
    return valor - desconto


preco_servico = 200
desconto = 25
valor_final = calcular_servico(preco_servico, desconto)

print(f'Valor original: R${preco_servico},00')
print(f'Desconto: R${desconto},00')
print(f'Valor final: R${valor_final},00')

# Exercício 2 — Retornando múltiplos valores

estoque = [
    {"nome": "Mouse", "preco": 50, "quantidade": 10},
    {"nome": "Teclado", "preco": 100, "quantidade": 5},
    {"nome": "Monitor", "preco": 800, "quantidade": 2}
]

def analisar_estoque(produtos):
    unidades = len(produtos)
    total_estoque = 0

    for produto in produtos:
        total_estoque += produto["preco"] * produto["quantidade"]

    return unidades, total_estoque

unidades, valor_total = analisar_estoque(estoque)

print(f'Atualmente temos {unidades} produtos no estoque. O valor total do estoque é de: R${valor_total},00.')

# Exercício 3 — Funções trabalhando juntas

def calcular_desconto(preco, porcentagem_desconto):
    desconto = preco * porcentagem_desconto / 100
    # calculando o valor de desconto com base na porcentagem

    return preco - desconto

def calcular_comissao(preco_final):
    return preco_final * 0.10

preco_final = calcular_desconto(250, 10) # segundo valor é a porcentagem de desconto

comissao = calcular_comissao(preco_final)

print(f'O valor final do serviço com o desconto é: R${preco_final}. Comissão gerada: R${comissao}')

# Exercício 4 — Desafio conceitual

def adicionar(a, b):
    resultado = a + b
    print(resultado)


valor = adicionar(10, 20)

print(valor) # Será exibido 30 e embaixo None
# conteudo de valor será None, pois não retornamos um valor
# Para retornar valor da soma: return resultado ou return a + b


