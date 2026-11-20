# Exercício 1

def registrar_servico(nome, servico, preco):
    with open("servicos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} - {servico} - R${preco:.2f}\n")

    return True
    
# Exercício 2

def listar_servicos():
    try:
        with open("servicos.txt", "r", encoding="utf-8") as arquivo:
            for servico in arquivo:
                print(servico.strip())
    except FileNotFoundError:
         print("Arquivo não encontrado.")
         return None

    return True

listar_servicos()
