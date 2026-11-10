equipamento = {
    "cliente": "Carlos",
    "equipamento": "Notebook",
    "marca": "Dell",
    "modelo": "Inspiron"
}

def apresentar_equipamento(cliente, equipamento, marca, modelo):
    print(cliente, equipamento, marca, modelo)

apresentar_equipamento(**equipamento)