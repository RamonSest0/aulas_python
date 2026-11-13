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

    if qtn_servicos == 0:
       return 0
    
    return faturamento_total
        
def gerar_relatorio(cliente):
    relatorio_cliente = {}

    relatorio_cliente["nome"] = cliente["nome"]
    relatorio_cliente["quantidade_servicos"] = len(cliente["servicos"])

    relatorio_cliente["faturamento_total"] = calcular_faturamento(cliente["servicos"])

    return relatorio_cliente



def gerar_relatorios(clientes):
    relatorios = [
        gerar_relatorio(relatorio)
        for relatorio in clientes
    ]
    # for relatorio in clientes:
    #    relatorios.append(gerar_relatorio(relatorio))

    return relatorios

print(gerar_relatorios(clientes))