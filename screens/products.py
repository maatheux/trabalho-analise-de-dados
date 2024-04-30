import os

import pandas as pd
from repositories.repository import Repository
import matplotlib.pyplot as plt


def display() -> None:
    print("\n")
    action_list = [
        'Produtos mais vendidos',
        'Produtos que renderam um maior faturamento'
    ]

    for i, v in enumerate(action_list):
        print(f'{i + 1} - {v}')
    action_value = int(input("Insira o valor da ação que deseja realizar: "))

    match action_value:
        case 1:
            get_best_sellers()
        case 2:
            highest_revenue()
        case _:
            return


def get_best_sellers() -> None:
    repo = Repository('ItensVendas')
    df = repo.get_table_data()

    grouped_df = df.groupby('ProdutoID').sum()

    best_sellers_series = list(grouped_df.items())[1][1].sort_values(ascending=False)

    product_names_dict = get_products()
    product_names_dict_values = []

    product_data = {}
    for product_id, value in best_sellers_series.items():
        product_data[product_names_dict[product_id]] = value
        product_names_dict_values.append(product_names_dict[product_id])

    fig, ax = plt.subplots()
    best_sellers_df = pd.DataFrame(product_data, index=['Valores'])
    best_sellers_df.plot(kind='barh', ax=ax, figsize=(22, 10))

    for container in ax.containers:
        ax.bar_label(container)

    ax.set_title("Quantidade vendidas p/ produto")
    ax.legend(product_names_dict_values)

    plt.show()


def highest_revenue() -> None:
    repo = Repository('ItensVendas')
    df = repo.get_table_data()

    grouped_df = df.groupby('ProdutoID').sum()

    highest_revenue_series = list(grouped_df.items())[-1][1].sort_values(ascending=False)
    print(highest_revenue_series)

    product_names_dict = get_products()
    product_names_dict_values = []

    product_data = {}
    for product_id, value in highest_revenue_series.items():
        product_data[product_names_dict[product_id]] = value
        product_names_dict_values.append(product_names_dict[product_id])

    fig, ax = plt.subplots()
    best_sellers_df = pd.DataFrame(product_data, index=['Faturamento'])
    best_sellers_df.plot(kind='barh', ax=ax, figsize=(18, 10))

    for container in ax.containers:
        ax.bar_label(container)

    ax.set_title("Faturamento p/ produto")
    ax.legend(product_names_dict_values)

    plt.show()


def get_products() -> dict:
    repo = Repository('Produtos')
    df = repo.get_table_data()

    df = df.set_index(df.columns[0])

    data_dict = df.squeeze().to_dict()

    return data_dict['Produto']


if __name__ == '__main__':
    display()
