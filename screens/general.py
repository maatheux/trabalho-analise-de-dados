import os
from repositories.repository import Repository


def display():
    action_option = int(input("\nInforme a tabela para análise (1 - Clientes / 2 - Vendedores / 3 - Produtos): "))

    match action_option:
        case 1:
            get_data("Clientes")
        case 2:
            get_data("Vendedores")
        case 3:
            get_data("Produtos")
        case _:
            return


def get_data(sheet_name: str) -> None:
    repo = Repository(sheet_name)
    df = repo.get_table_data()

    print(df.to_string(index=False))


if __name__ == '__main__':
    display()
