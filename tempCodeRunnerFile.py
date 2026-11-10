def cadastrar_servico(cliente, *servicos, desconto=0, **detalhes):
    print(f"Cliente: {cliente}")
    print(f"Serviços: {servicos}")
    print(f"Desconto: {desconto}")
    print(f"Detalhes: {detalhes}")

servicos_contratados = ["Limpeza", "Aspiração"]

informacoes = {
    "desconto": 30,
    "cidade": "Jacuí",
    "valor": 250
}

cadastrar_servico("Carlos", *servicos_contratados, **informacoes)