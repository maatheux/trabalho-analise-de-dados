from screens import products, sellers, costumers, general
from dotenv import dotenv_values


def display():
    while True:
        print("\nMenu de análise da base")
        print("-----------------------------------------------")
        print(
            "Qual análise gostaria de realizar? (0 - Fechar sistema / 1 - Visão geral / 2 - Visão de produtos / 3 - "
            "Visão de vendedores / 4 -"
            "Visão de clientes)")
        screen_option = int(input("Digite o valor: "))

        match screen_option:
            case 0:
                return
            case 1:
                general.display()
            case 2:
                products.display()
            case 3:
                sellers.display()
            case 4:
                costumers.display()
            case _:
                return


if __name__ == '__main__':
    display()
