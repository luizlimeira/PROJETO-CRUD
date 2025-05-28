from ficha import *
from cardapio import *

def main():
    while True:
        print("\n==== SISTEMA DO RESTAURANTE ====")
        print("1. Gerenciar Cardápio")
        print("2. Gerenciar Fichas Técnicas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cardapio()

        elif opcao == "2":
            menu_fichas()

        elif opcao == "0":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()