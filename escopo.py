# Exercício 2 — Sistema de ordens de serviço

def calcular_total(mao_de_obra, pecas):
    valor_total = mao_de_obra + pecas
    return valor_total

def criar_ordem(cliente, equipamento, mao_de_obra, pecas):
    ordem_de_servico = {}

    ordem_de_servico["nome"] = cliente
    ordem_de_servico["equipamento"] = equipamento
    ordem_de_servico["mao_de_obra"] = mao_de_obra
    ordem_de_servico["pecas"] = pecas
    ordem_de_servico["total"] = calcular_total(mao_de_obra, pecas)

    return ordem_de_servico


def exibir_ordem(ordem):

    for chave, valor in ordem.items():
        print(chave, valor)

ordem_1 = criar_ordem("Ramon", "Celular", 200, 180)

exibir_ordem(ordem_1)

# Exercício 3 — Desafio integrador

clientes = [
    {
        "nome": "Carlos",
        "servicos": [
            {"descricao": "Limpeza", "valor": 150},
            {"descricao": "Manutenção", "valor": 200}
        ]
    },
    {
        "nome": "Mariana",
        "servicos": [
            {"descricao": "Limpeza", "valor": 120}
        ]
    }
]

def calcular_faturamento(servicos):
    qtn_servicos = len(servicos)
    faturamento_total = 0

    for servico in servicos:
        faturamento_total += servico["valor"]
    
    return faturamento_total
        
def gerar_relatorio(cliente):
    relatorio_cliente = {}

    relatorio_cliente["nome"] = cliente["nome"]
    relatorio_cliente["quantidade_servicos"] = len(cliente["servicos"])

    relatorio_cliente["faturamento_total"] = calcular_faturamento(cliente["servicos"])

    return relatorio_cliente

def gerar_relatorios(clientes):
    relatorios = [
        gerar_relatorio(cliente)
        for cliente in clientes
    ]

    return relatorios

print(gerar_relatorios(clientes))