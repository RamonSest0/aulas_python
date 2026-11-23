import csv
from pathlib import Path

def registrar_cliente(nome, telefone, cidade):

    caminho = Path("dados/clientes.csv") # representa o caminho onde desajamos armazenar / não cria
    pasta = caminho.parent # Identifica a pasta / não cria

    pasta.mkdir(exist_ok=True) # O Python verifica se a pasta dados existe:
    # Se não existir, cria a pasta.
    # Se já existir, continua normalmente.

    # pasta.mkdir(parents=True, exist_ok=True)
    # se você usar mkdir(exist_ok=True) sem parents=True, ele não criará automaticamente vários níveis de diretórios intermediários ausentes.

    with caminho.open("a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow([nome, telefone, cidade])

    return True

registrar_cliente("Jorge", "2198888", "Paraiso")
