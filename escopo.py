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


def exibir_ordem():
    ordem_de_servico = criar_ordem("Ramon", "Celular", 200, 180)

    for chave, valor in ordem_de_servico.items():
        print(chave, valor)

exibir_ordem()