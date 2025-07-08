from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int ]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('============================')
    print('======= Bem vindo(a) =======')
    print('========= CL SHOP ==========')
    print('============================')

    print('Selecione uma opção abaixo:')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Vizualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - sair')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produtos()
    elif opcao == 4:
        vizualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opçao Invalida!')
        sleep(2)
        menu()

def cadastrar_produto() -> None:
    print('Cadastrar Produto')
    print('=================')

    nome: str = input('informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('--------------------')
            sleep(1)

    else:
        print('Ainda não existe produtos cadastrados no sistema.')
    sleep(2)
    menu()

def comprar_produtos() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print('===================PRODUTOS DISPONIVEIS=======================')
        for produto in produtos:
            print(produto)
            print('---------------------')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quantidade: int = item.get(produto)
                    if quantidade:
                        item[produto] = quantidade + 1
                        print(f'O produto {produto.nome} agora possui {quantidade + 1} quantidade no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com codigo {codigo} não foi encontrado.')
            sleep(2)
            menu()

    else:
        print('Ainda não existe produtos para vender!')
    sleep(2)
    menu()

def vizualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)

    else:
        print('Ainda não existe produto no carrinho.')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        
        valor_total: float = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('--------------------')
                sleep(2)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existe produtos no carrinho')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()
