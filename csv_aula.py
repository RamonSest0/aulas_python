import csv
from pathlib import Path

# Desafio 1

def registrar_cliente(nome, telefone, cidade):

    criar_cabecalho = True

    header = ["nome", "telefone", "cidade"]

    cliente = {
        "nome": nome,
        "telefone": telefone,
        "cidade": cidade
    }

    caminho = Path("dados/clientes.csv") # representa o caminho onde desajamos armazenar / não cria
    pasta = caminho.parent # Identifica a pasta / não cria

    pasta.mkdir(exist_ok=True) # O Python verifica se a pasta dados existe:
    # Se não existir, cria a pasta.
    # Se já existir, continua normalmente.

    # pasta.mkdir(parents=True, exist_ok=True)
    # se você usar mkdir(exist_ok=True) sem parents=True, ele não criará automaticamente vários níveis de diretórios intermediários ausentes.

    if not caminho.exists():
        criar_cabecalho = False
        

    with caminho.open("a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=header)

        if not criar_cabecalho:
            escritor.writeheader()

        escritor.writerow(cliente)

    return True

# Desafio 2

def listar_clientes():
    caminho = Path("dados/clientes.csv")

    with caminho.open("r", newline="", encoding="utf-8") as arquivo:

        clientes = csv.DictReader(arquivo)

        for cliente in clientes:
             print(f"Nome: {cliente["nome"]}. Telefone: {cliente["telefone"]}. Cidade: {cliente["cidade"]}")

listar_clientes()
