from pathlib import Path
import csv

def atualizar_cidade(nome_procurado, nova_cidade):
    caminho = Path("dados/clientes.csv")
    cliente_encontrado = False
    campos = ["nome", "telefone", "cidade"]

    if not caminho.exists():
        print("Caminho não existe.")
        return None

    if caminho.stat().st_size == 0:
        print("Arquivo vazio.")
        return None

    with caminho.open("r", newline="", encoding="utf-8") as arquivo:
        clientes = list(csv.DictReader(arquivo))

        for cliente in clientes:
            nome = cliente["nome"]
            if nome.lower() == nome_procurado.lower():
                cliente["cidade"] = nova_cidade
                cliente_encontrado = True
                print("Alteração realizada com sucesso!")

        if not cliente_encontrado:
            print("Cliente não encontrado.")
            return False
        
    reescrever_arquivo(clientes)
    return True
    
def reescrever_arquivo(clientes):
    caminho = Path("dados/clientes.csv")
    campos = ["nome", "telefone", "cidade"]

    with caminho.open("w", newline="", encoding="utf-8") as arquivo:
        escrever = csv.DictWriter(arquivo, fieldnames=campos)

        escrever.writeheader()
        escrever.writerows(clientes)
        print("Atualização do arquivo foi feita com sucesso.")
        return True

atualizar_cidade("Carlos", "Itamogi")

        





            
