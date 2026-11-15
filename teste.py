def modificar(lista):
    print("ID dentro da função:", id(lista))

    lista = ["Mouse", "Webcam"]

    print("ID após atribuição:", id(lista))


produtos = ["Teclado", "Monitor"]

print("ID original:", id(produtos))

modificar(produtos)

print("ID final:", id(produtos))

nome = True
telefone = False

if not nome:
    print(True)



# Exercício 6 — Raciocínio

# validar_cliente() deve conhecer as regras de validação, visto que é a responsabilidade é dela, cadastrar_cliente() deve apenas receber o resultado da validação. Duplicar, além de ser redundante deixaria o código maior e mais complexo sem necessidade.

# Exercício 7 — validar_servico(descricao, valor)

def validar_servico(descricao, valor):
    if descricao.strip() and valor > 0:
        return True
    
    return False

# Exercício 8 — Integração

def registrar_servico(cliente, descricao, valor):
    if not validar_servico(descricao, valor):
        return False

    servicos = {
        "descricao": descricao,
        "valor": valor
    }

    cliente["servicos"].append(servicos)

    return True

# Exercício 9 — Teste integrado

cliente_1 = cadastrar_cliente("Ramon", "21988888888")
print(registrar_servico(cliente_1, "", 200))
print(registrar_servico(cliente_1, "manutenção", -1))
print(registrar_servico(cliente_1, "manutenção", 200))

print(cliente_1)

lista_ex = [1, 2]

if not lista_ex:
    print(False)