def validar_cliente(nome, telefone):
    if nome and telefone:
       return True
    else:
        return False

print(validar_cliente('nome', ''))