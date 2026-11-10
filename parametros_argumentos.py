# Exercício 1 — Sistema de serviços

def calcular_manutencao(valor_base, produtos, desconto=0, taxa_extra=0):

    valor_final = valor_base + produtos + taxa_extra - desconto

    return valor_final

servico_1 = calcular_manutencao(250, 80)
servico_2 = calcular_manutencao(produtos=100, valor_base=200, taxa_extra=25)

servico_3 = calcular_manutencao(250, 80, 30, 15)
servico_4 = calcular_manutencao(taxa_extra=15, produtos=80, valor_base=250, desconto=30)

print(servico_3)
print(servico_4)