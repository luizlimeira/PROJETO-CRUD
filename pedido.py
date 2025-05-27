import json
import os

ARQUIVO_CARDAPIO = os.path.join(os.path.dirname(__file__), 'cardapio.json')



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
