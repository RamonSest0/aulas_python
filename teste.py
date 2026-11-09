def modificar(lista):
    print("ID dentro da função:", id(lista))

    lista = ["Mouse", "Webcam"]

    print("ID após atribuição:", id(lista))


produtos = ["Teclado", "Monitor"]

print("ID original:", id(produtos))

modificar(produtos)

print("ID final:", id(produtos))