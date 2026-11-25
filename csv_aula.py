import csv
from pathlib import Path

# Desafio 1

def registrar_cliente(nome, telefone, cidade):

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

    criar_cabecalho = (not caminho.exists() or caminho.stat().st_size == 0)
        

    with caminho.open("a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=header)

        if criar_cabecalho:
            escritor.writeheader()

        escritor.writerow(cliente)

    return True

# Desafio 2

def listar_clientes():

    caminho = Path("dados/clientes.csv")
    cliente_encontrado = False

    try:
        with caminho.open("r", newline="", encoding="utf-8") as arquivo:

            clientes = csv.DictReader(arquivo)

            for cliente in clientes:
                print(f"Nome: {cliente['nome']} "
                    f"Telefone: {cliente['telefone']} "
                    f"cidade: {cliente['cidade']}")
                cliente_encontrado = True

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return False
        
    if not cliente_encontrado:
        print("Nenhum cliente encontrado.")

    return cliente_encontrado

registrar_cliente("Ramon", "2199999", "Jacuí")
             
print(listar_clientes())
