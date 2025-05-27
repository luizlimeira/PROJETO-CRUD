import json



with open("pedido.json", "w") as file:
    json.dump(my_dict, file, indent=5)

print("\nPedido salvo com sucesso! Obrigado.")