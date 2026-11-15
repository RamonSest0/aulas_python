clientes = [
    {
        "nome": "Ana",
        "telefone": "1111",
        "servicos": [
            {"descricao": "limpeza", "valor": 150},
            {"descricao": "aspiracao", "valor": 80}
        ]
    },
    {
        "nome": "Ramon",
        "telefone": "2222",
        "servicos": [
            {"descricao": "limpeza", "valor": 200}
        ]
    },
    {
        "nome": "Pedro",
        "telefone": "3333",
        "servicos": []
    }
]

# Exercício A — Calcular faturamento

def calcular_faturamento(cliente):
    faturamento = 0

    if not cliente["servicos"]:
        return faturamento

    for servico in cliente["servicos"]:
        faturamento += servico["valor"]

    return faturamento

# Exercício B — Gerar relatório

def gerar_relatorio(clientes):
    relatorios = []

    for cliente in clientes:
        relatorios.append({
            "nome": cliente["nome"],
            "quantidade_servicos": len(cliente["servicos"]),
            "faturamento": calcular_faturamento(cliente)
        })

    return relatorios

# Exercício C — Um pouco mais de arquitetura

def filtrar_clientes(clientes, faturamento_minimo):
    clientes_filtrados = [
        cliente 
        for cliente in clientes 
        if calcular_faturamento(cliente) >= faturamento_minimo
    ]

    return clientes_filtrados

# Desafio bônus — Packing e unpacking

def cadastrar_cliente(nome, telefone, *servicos, **dados_adicionais):
    cliente = {
        "nome": nome,
        "telefone": telefone,
        "servicos": list(servicos),
        "dados_adicionais": dados_adicionais,
    }

    return cliente

novo_cliente = cadastrar_cliente(
    "Carla",
    "4444",
    {"descricao": "limpeza", "valor": 120},
    {"descricao": "aspiracao", "valor": 80},
    cidade="Jacuí",
    origem="indicação"
)

# Preveja os resultados antes de executar e explique por que cada um acontece.

print(gerar_relatorio(clientes)) # Uma lista contendo um dicionario de cada cliente, com nome, quantidade de servicos e faturamento. Acontece pois nossa função trabalha com a lista principal e gera uma nova lista com essas informacoes.

print(filtrar_clientes(clientes, 150)) # cria uma lista filtrada apenas com ifromações dos clientes conde o faturamento foi igual ou superior a 150. Isso acontece pois usamos list comprehension com um filtro, se aproveitando da função que calcula o faturamento

print(calcular_faturamento(novo_cliente)) # 200. Pois será o total do valor de faturamento de novo_cliente

