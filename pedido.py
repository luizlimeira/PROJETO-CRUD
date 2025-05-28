import json
import os




print("Olá tudo bem? antes de realizar o pedido, Qual nome você deseja na comanda?")
x = input("Digite nome: ")



print("PRONTO!!! Agora vamos ao pedido... ")
precos = {
    'id1': 60.0,
    'id2': 70.0,
    'id3': 89.9,
    'id4': 45.0,
    'id5': 15.0,
    'id6': 20.0,
    'id7': 25.0,
    'id8': 17.0,
    'id9': 9.5,
    'id10': 9.5,
    'id11': 7.9,
}
arquivo_pedidos = "pedido.json"

if os.path.exists(arquivo_pedidos):
    with open(arquivo_pedidos, "r") as file:
        try:
            my_dict = json.load(file)
        except json.JSONDecodeError:
            my_dict = {"pessoas": []}
else:
    my_dict = {"pessoas": []}


novo_pedido = {
    "nome": x,
    "pedidos": pedidos_cliente,
    "valor_total": round(valor_total, 2)
}

my_dict["pessoas"].append(novo_pedido)


with open(arquivo_pedidos, "w") as file:
    json.dump(my_dict, file, indent=4, ensure_ascii=False)

print("\nPedido salvo com sucesso!")
