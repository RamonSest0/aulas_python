# Prática rápida

def ler_servicos():
    try:
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            servicos = arquivo.read()
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return False

    return servicos


print(ler_servicos())
    