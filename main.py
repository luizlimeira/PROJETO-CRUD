from cardapio import *

# from ficha import *

# def menu_pedido():
#     while True:
#         print("\n--- PEDIDOS ---")
#         print("1. Adicionar Pedido")
#         print("2. Listar Pedido")
#         print("3. Atualizar Pedido")
#         print("4. Remover Pedido")
#         print("0. Voltar")
#         op = input("Escolha: ")

#         if op == "1":
#             # listar_pedidos()
#         elif op == "2":
#             adicionar_item()
#         elif op == "3":
#             atualizar_item()
#         elif op == "4":
#             remover_item()
#         elif op == "5":
#             filtrar_por_categoria()
#         elif op == "0":
#             break    
#         else:
#             print("Opção inválida.")

# def menu_fichas():
#     while True:
#         fichas = carregar_fichas()
        
#         print("\n--- MENU FICHAS ---")
#         print("1. Adicionar Ficha")
#         print("2. Visualizar Fichas")
#         print("3. Editar Ficha")
#         print("4. Excluir Ficha")
#         print("0. Voltar")
        
#         opcao = input("Escolha uma opção: ")
        
#         if opcao == "1":
#             fichas = adicionar_ficha(fichas)
#         elif opcao == "2":
#             visualizar_fichas(fichas)
#         elif opcao == "3":
#             editar_fichas(fichas)
#         elif opcao == "4":
#             excluir_fichas(fichas)
#         elif opcao == "0":
#             return
#         else:
#             print("\nOpção inválida!")


def menu_cardapio():
    while True:
        print("\n--- CARDÁPIO ---")
        print("1. Listar")
        print("2. Adicionar")
        print("3. Atualizar")
        print("4. Remover")
        print("5. Filtrar")
        print("0. Voltar")
        op = input("Escolha: ")

        if op == "1":
            listar_cardapio()
        elif op == "2":
            adicionar_item()
        elif op == "3":
            atualizar_item()
        elif op == "4":
            remover_item()
        elif op == "5":
            filtrar_por_categoria()
        elif op == "0":
            break    
        else:
            print("Opção inválida.")

def main():
    while True:
        print("\n==== SISTEMA DO RESTAURANTE ====")
        print("1. Gerenciar Cardápio")
        print("2. Gerenciar Pedidos")
        print("3. Gerenciar Fichas Técnicas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cardapio()

        elif opcao == "2":
            menu_pedidos()

        elif opcao == "3":
            menu_fichas()

        elif opcao == "0":
            print("Saindo do sistema.")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()