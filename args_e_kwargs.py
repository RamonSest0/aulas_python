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

def cadastrar_equipamento(cliente, equipamento, *acessorios, **informacoes):

    print(f"Nome do clinte: {cliente}.")
    print(f"Equipamento: {equipamento}")

    print("lista de acessórios:")

    for acessorio in acessorios:
        print(acessorio)

    print("Informações adiconais:")

    for informacao, descricao in informacoes.items():
        print(f"{informacao}: {descricao}")



cadastrar_equipamento("Carlos", "Notebook", "Carregador", "Mouse", "Bolsa", marca="dell", modelo="Inspirion", defeito="Tela não liga" )    


equipamento = {
    "cliente": "Carlos",
    "equipamento": "Notebook",
    "marca": "Dell",
    "modelo": "Inspiron"
}

def apresentar_equipamento(cliente, equipamento, marca, modelo):
    print(cliente, equipamento, marca, modelo)

apresentar_equipamento(**equipamento)

# Desafio de consolidação

def cadastrar_servico(cliente, *servicos, desconto=0, **detalhes):
    print(f"Cliente: {cliente}")
    print(f"Serviços: {servicos}")
    print(f"Desconto: {desconto}")
    print(f"Detalhes: {detalhes}")

servicos_contratados = ["Limpeza", "Aspiração"]

informacoes = {
    "desconto": 30,
    "cidade": "Jacuí",
    "valor": 250
}

cadastrar_servico("Carlos", *servicos_contratados, **informacoes) # quando desempacotamos informacoes ele vai gerar um sequencia de argumentos nomeados, desconto=30, cidade="Jacuí", valor=250 
# Assim, desconto vai "entrar" no parametro desconto, e o restante dos argumentos desempacotados em **detalhes

