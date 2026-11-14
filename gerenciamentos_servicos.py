def cadastrar_cliente(nome, telefone):
    if not validar_cliente(nome, telefone):
        return None

    cliente = {
        "nome": nome,
        "telefone": telefone,
        "servicos": []
    }

    return cliente

def registrar_servico(cliente, descricao, valor):
    if not validar_servico(descricao, valor):
        return False

    servicos = {
        "descricao": descricao,
        "valor": valor
    }

    cliente["servicos"].append(servicos)

    return True

def validar_cliente(nome, telefone):
    if nome.strip() and telefone.strip():
       return True
    else:
        return False

def validar_servico(descricao, valor):
    if descricao.strip() and valor > 0:
        return True
    
    return False

cliente_1 = cadastrar_cliente("Ramon", "21988888888")
print(registrar_servico(cliente_1, "", 200))
print(registrar_servico(cliente_1, "manutenção", -1))
print(registrar_servico(cliente_1, "manutenção", 200))

print(cliente_1)

def exibir_cliente(cliente):
    print(cliente)

def gerenciar_cadastro(nome, telefone):
    cliente = cadastrar_cliente(nome, telefone)

    if cliente is None:
        return False

    exibir_cliente(cliente)

    return True

print(gerenciar_cadastro("Ramon", "2198888888"))
print(gerenciar_cadastro("Ramon", "   "))


def gerenciar_servicos(cliente, descricao, valor):
    resultado = registrar_servico(cliente, descricao, valor)

    if resultado is False:
        print("Não foi possível registrar o serviço")
        return False

    print("Registro bem sucedido!")
    return True

print(gerenciar_servicos(cliente_1, "limpeza", 150))
print(gerenciar_servicos(cliente_1, "", 150))

# Por que essa função não deveria conhecer os detalhes internos de validar_servico()?
# A função dela é apenas gerenciar a execução e decidir como usar os dados retornados. Sendo assim, não há necessidade dela conhecer os detalhes de validação. A responsabilidade de validar os dados é de outra função.
    



