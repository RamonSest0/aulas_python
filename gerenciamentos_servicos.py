# Exercício 1 — Planejamento

# Exercício 2 — Contrato de função

def cadastrar_cliente(nome, telefone):
    cliente = {
        "nome": nome,
        "telefone": telefone,
        "servicos": []
    }

    return cliente

# Exercício 3 — Registro de serviço

def registrar_servico(cliente, descricao, valor):
    servicos = {
        "descricao": descricao,
        "valor": valor
    }

    cliente["servicos"].append(servicos)

    return "Operação realizada com sucesso!"

cliente_1 = cadastrar_cliente("Ramon", "21988888888")

print(registrar_servico(cliente_1, "manutenção", 200))

print(cliente_1)

