from pathlib import Path

def verificar_arquivo(arquivo):
    caminho = Path(arquivo)

    if caminho.exists():
        if caminho.is_file():
            return True
        else:
            return False
    else:
        print("Arquivo não encontrado")
        return None

print(verificar_arquivo("servicos.txt"))