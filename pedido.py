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

cardapio = [
    "1.Filé à parmegiana--> 60,0",
    "2.Peixe crocante --> 70,0",
    "3.Carne de sol do Maranhão --> 89,9",
    "4.Filé com fritas ---> 45,0",
    "5.Caldinho de feijão ---> 15,0",
    "6.Pastel de queijo ---> 20,0",
    "7.Pudim de Leite ---> 25,0",
    "8.Torta pavê de chocolate ---> 17,0",
    "9.Água mineral ---> 9,5",
    "10.Refrigerante(coca-cola, fanta, guaraná) ---> 9,5",
    "11.Café expresso ---> 7,9"
]

for item in cardapio:
    print(item)

print("____________________________________________________________________________________________________________________________\n")
print("Obs: digite 'id' antes de escolher seu número (ex: id1)")
print("Obs: caso deseje cancelar a operação digite 'sair'...")

qnt_total = 0
valor_total = 0.0
pedidos_cliente = []


while True:
    pedido = input("Qual item você deseja pedir?: ")

    if pedido == 'sair':
        print("\nPedido finalizado.")
        print(f"Total de itens pedidos: {len(pedidos_cliente)}")
        print(f"Valor total: R$ {valor_total:.2f}")
        break
    elif pedido in precos:
        print(f"{pedido.upper()} adicionado ao pedido! Valor: R$ {precos[pedido]:.2f}")
        pedidos_cliente.append(pedido)
        valor_total += precos[pedido]
    else:
        print("Erro! Digite um ID válido.")

print("\nSeu pedido atual:")
for i, item in enumerate(pedidos_cliente, 1):
    print(f"{i}. {item} - R$ {precos[item]:.2f}")


while True:
    mudar_pedido = input("\nDeseja ATUALIZAR algum pedido (digite 'update'), REMOVER (digite 'delete') ou SALVAR e sair (digite 'salvar')? ").lower()

    if mudar_pedido == 'update':
        indice = int(input("Digite o número do item que deseja atualizar (ex: 1, 2, 3...): ")) - 1
        if 0 <= indice < len(pedidos_cliente):
            novo_id = input("Digite o novo ID do item: ")
            if novo_id in precos:
                valor_total -= precos[pedidos_cliente[indice]]
                pedidos_cliente[indice] = novo_id
                valor_total += precos[novo_id]
                print("Item atualizado com sucesso!")
            else:
                print("ID inválido!")
        else:
            print("Número inválido!")

    elif mudar_pedido == 'delete':
        indice = int(input("Digite o número do item que deseja remover (ex: 1, 2, 3...): ")) - 1
        if 0 <= indice < len(pedidos_cliente):
            valor_total -= precos[pedidos_cliente[indice]]
            pedidos_cliente.pop(indice)
            print("Item removido com sucesso!")
        else:
            print("Número inválido!")

    elif mudar_pedido == 'salvar':
        break
    else:
        print("Comando inválido. Use 'update', 'delete' ou 'salvar'.")

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
