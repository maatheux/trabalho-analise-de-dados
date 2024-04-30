from screens import products, sellers, costumers
from dotenv import dotenv_values

def display():
    secrets = dotenv_values(".env")
    
    print("Menu de análise da base")
    print("-----------------------------------------------")
    print("Qual análise gostaria de realizar? (1 - Visão geral / 2 - Visão de produtos / 3 - Visão de vendedores / 4 - "
          "Visão de clientes)")
    screen_option = int(input("Digite o valor: "))

    match screen_option:
        case 1:
            costumers.display()
        case 2:
            products.display()
        case 3:
            sellers.display()
        case 4:
            pass
        case _:
            return


if __name__ == '__main__':
    display()
