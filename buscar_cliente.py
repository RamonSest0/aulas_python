import csv
from pathlib import Path

def buscar_cliente(nome_pocurado):
    caminho = Path("dados/clientes.csv")

    if not caminho.exists() or caminho.stat().st_size == 0:
        print("Arquivo não encontrado.")
        return None

    with caminho.open("r", newline="", encoding="utf-8") as arquivo:
        clientes = csv.DictReader(arquivo)
        print(clientes)

        for cliente in clientes:
            if cliente["nome"].lower() == nome_pocurado.lower():
                return cliente

        return None # Caso o o for não encontre o cliente retorna...

cliente = buscar_cliente("Ramon")

if cliente is not None:
    print("Cliente encontrado:")
    print(cliente)
else:
    print("Cliente não encontrado")