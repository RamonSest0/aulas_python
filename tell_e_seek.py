# Exercício 1 — ler_primeiro_servico()

def ler_primeiro_servico():
    try:
        with open("servicos.txt", "r", encoding="utf-8") as arquivo:
            servico = arquivo.readline()
            posicao_servico = arquivo.tell()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None

    return servico.strip(), posicao_servico

# Exercício 2 — reler_servicos()

def reler_servicos():
    try:
        with open("servicos.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
            arquivo.seek(0)

            for servico in arquivo:
                print(servico.strip())

    except FileNotFoundError:
        print("Arquivo não encontrado.")
