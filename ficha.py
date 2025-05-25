import json
import os

ARQUIVO_FICHAS = 'ficha.json'

def carregar_fichas():
    if not os.path.exists(ARQUIVO_FICHAS):
        with open(ARQUIVO_FICHAS, 'w') as f:
            json.dump([], f)
        return []
    
    with open(ARQUIVO_FICHAS, 'r') as f:
        return json.load(f)

def salvar_fichas(fichas):
    with open(ARQUIVO_FICHAS, 'w') as f:
        json.dump(fichas, f, indent=4)

def adicionar_ficha(fichas):
     while True:
        print("\n" + "=" * 40)
        print("ADICIONAR NOVA FICHA".center(40))
        print("=" * 40)

        while True:
            nome = input("Nome: ").strip().capitalize()
            if not nome:
                print("Nome não pode ser vazio!")
                continue
        
            nome_existe = any(f['nome'].lower() == nome.lower() for f in fichas)
            if nome_existe:
                print("Já existe uma ficha com este nome!")
            else:
                break
        
        while True:
            categoria = input("Categoria: ").strip().upper()
            if categoria:
                break
            print("Categoria não pode ser vazia!")

        ingredientes = []
        print("\nINGREDIENTES:")
        while True:
            ingred = input("Ingrediente (deixe em branco para parar): ").capitalize()
            if not ingred:
                if not ingredientes:
                    print("Adicione pelo menos 1 ingrediente!")
                    continue
                break

            quant = input("Quantidade: ").strip()
            while not quant:
                print("Quantidade não pode ser vazia!")
                quant = input("Quantidade: ").strip()
                
            ingredientes.append({'ingrediente': ingred, 'quantidade': quant})
        
        preparo = []
        print("\nMODO DE PREPARO:")
        passo_num = 1
        while True:
            descricao = input(f"Passo {passo_num} (deixe em branco para parar): ").strip().capitalize()
            if not descricao:
                if not preparo:
                    print("Adicione pelo menos 1 passo!")
                    continue
                break
            preparo.append({'passo': passo_num, 'descricao': descricao})
            passo_num += 1
    
        nova_ficha = {
            'categoria': categoria,
            'nome': nome,
            'ingredientes': ingredientes,
            'preparo': preparo
        }

        fichas.append(nova_ficha)
        salvar_fichas(fichas)
        print("\nFicha adicionada com sucesso!")

        op = input("\nAdicionar outra ficha? (s/n): ").lower()
        if op != 's':
            break


def visualizar_fichas(fichas):
    if not fichas:
        print("\nNenhuma ficha cadastrada ainda!")
        input("Pressione Enter para voltar...")
        return
    
    categorias = sorted(set(f['categoria'] for f in fichas))

    for categoria in categorias:
        print("\n" + "=" * 90)
        print(f"\n{categoria.upper():^90}")
        print("=" * 90)

        fichas_cat = [f for f in fichas if f['categoria'] == categoria]
        for ficha in  fichas_cat:
            
            print(f"Nome: {ficha['nome']}")
        
            print("\nIngredientes:")
            for ingred in ficha['ingredientes']:
                print(f"- {ingred['quantidade']} de {ingred['ingrediente']}")
        
            print("\nModo de Preparo:")
            for passo in ficha['preparo']:
                print(f"{passo['passo']}. {passo['descricao']}")
                print("-" * 90)
        
        input("\nPressione Enter para voltar...")

def editar_fichas(fichas):
    nome = input("Digite o nome da ficha que deseja editar: ").strip().lower()
    
    for ficha in fichas:
        if ficha['nome'].lower() == nome:
            print(f"\nEditando ficha: {ficha['nome']}")
            ficha['nome'] = input("Novo nome: ").capitalize()
            ficha['categoria'] = input("Nova categoria: ").upper()
            print("Ficha editada com sucesso!")
            salvar_fichas(fichas)
            return
    
    print("Ficha não encontrada.")

def excluir_fichas(fichas):
    nome = input("Digite o nome da ficha que deseja excluir: ").strip().lower()
    
    for ficha in fichas:
        if ficha['nome'].lower() == nome:
            print(f"\nFicha encontrada: {ficha['nome']}")
            if input("Tem certeza que deseja excluir? (s/n): ").lower() == 's':
                fichas.remove(ficha)
                print("Ficha excluída com sucesso.")
            salvar_fichas(fichas)
            return
    
    print("Ficha não encontrada.")
