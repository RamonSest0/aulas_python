# Exercício 1 — Conversão de valores

def converter_preco(preco):
    try:
        preco_convertido = float(preco)
        return preco_convertido
    except ValueError:
        print("Não foi possível realizar a conversão.")
        return False

# Exercício 2 — Cálculo de faturamento

def calcular_faturamento(faturamento, qtd_servicos):
    try:
        return faturamento / qtd_servicos
    except ZeroDivisionError:
        print("Não é possível relizar o calculo com '0' serviços.")
        return False

# Exercício 3 — Consulta de clientes

clientes = {
    "Ana": "1111",
    "Ramon": "2222",
    "Pedro": "3333"
}

def verificar_telefone(nome):
    try:
        telefone = clientes[nome]
        return telefone
    except KeyError:
        print("Nome inválido.")
        return False

# Exercício 4 — Desafio de integração

def cadastrar_idade(idade):
    try:
        idade_convertida = int(idade)
    except ValueError:
        print("Você digitou um caractere inválido. Digite um número inteiro.")
        return False

    if 18 >= idade_convertida <= 100:
        return idade_convertida
    else:
        print("Idade menor que 18 ou maior que 100.")
        return False

estoque = {
    "cloro": 10,
    "algicida": 5,
    "elevador_de_ph": 8
}

def retirar_estoque(estoque, produto, quantidade):
    try:

        if not isinstance(quantidade, int) or       isinstance(quantidade, bool):
            print("A quantidade deve ser um número inteiro.")
            return estoque
        
        if quantidade <= 0:
            print(f"Não é possível retirar {quantidade} do estoque. Estoque não alterado.")
            return estoque

        if quantidade > estoque[produto]:
            print(f"Quantidade desejada é maior que o número disponível no estoque: {estoque[produto]}. Estoque não alterado.")
            return estoque
        
        estoque[produto] -= quantidade
        print(f"Retirada de {quantidade} {produto}(s) feito com sucesso.")
        return estoque
    
    except KeyError: 
        print("Produto inválido. Estoque não alterado.")
        return estoque
    except TypeError:
        print("A quantidade digitada não é um número. Estoque não alterado.")
        return estoque

print(retirar_estoque(estoque, "cloro", 5))





