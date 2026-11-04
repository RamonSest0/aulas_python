produtos = {
    'nome': 'cloro',
    'preco': 85.50,
    'estoque': 12,
    'disponivel': True
}

print(f'Nome do produto: {produtos['nome']}. Preço: {produtos['preco']}')
produtos['estoque'] = 20
produtos['categoria'] = 'produtos quimicos'
produtos.pop('disponivel')
print(produtos)

clientes = {
    1: {
        'nome': 'Ramon',
        'cidade': 'Jacuí',
        'telefone': 2177777777
    },
    2: {
        'nome': 'Jorge',
        'cidade': 'Paraíso',
        'telefone': 218888888
    },
    3: {
        'nome': 'Marcos',
        'cidade': 'Jacuí',
        'telefone': 219999999
    },
}


clientes[4] = {
    'nome': 'Tiafoe',
    'cidade': 'USA',
    'telefone': 216666666
    }
clientes[3]['cidade'] = 'Itamogi'
clientes.pop(1)

for chave, valor in clientes.items():
    # print(chave, valor)
    print(f'Identificador {chave}. Nome: {valor['nome']}.')


servico ={
    'cliente_1': {
    'nome': 'Ramon',
    'servico': 'Piscina',
    'valor': 120.00,
    'telefone': 219999999,
    'pagamento': 'Pendente'
    },

    'cliente_2': {
    'nome': 'Jorge',
    'servico': 'Sofá',
    'valor': 120.00,
    'telefone': 21555555555,
    'pagamento': 'Pago'
    },

    'cliente_3': {
    'nome': 'Tiago',
    'servico': 'Piscina',
    'valor': 180.00,
    'pagamento': 'Pendente'
    },
} 

for chave, valor in servico.items():
    if valor['pagamento'] == 'Pendente':
        valor['pagamento'] = 'Pago'

    print(chave, valor, valor.get('telefone', 'Telefone não existe.'))





    
    





    





 





