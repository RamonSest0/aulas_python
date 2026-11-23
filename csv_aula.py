import csv
from pathlib import Path

def registrar_cliente(nome, telefone, cidade):

    caminho = Path("dados/clientes.csv")
    pasta = caminho.parent

    pasta.mkdir(exist_ok=True) # cria a pasta caso ela não exista?

    with caminho.open("a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow([nome, telefone, cidade])

    return True

registrar_cliente("Jorge", "2198888", "Paraiso")
