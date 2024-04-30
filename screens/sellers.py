from matplotlib import pyplot as plt
import pandas as pd

from repositories.repository import Repository


def display() -> None:
    print("\n")
    action_list = [
        'Faturamento por vendedor',
        'Quantidade vendida em cada mes por vendedor'
    ]

    for i, v in enumerate(action_list):
        print(f'{i + 1} - {v}')
    action_value = int(input("Insira o valor da ação que deseja realizar: "))

    match action_value:
        case 1:
            get_sells_by_seller()
        case 2:
            get_sells_by_month()
        case _:
            return


def get_sells_by_seller() -> None:
    repo = Repository('Vendas')
    df = repo.get_table_data()

    columns_to_sum = [col for col in df.columns if col != 'Data']

    grouped_df = df.groupby('VendedorID')[columns_to_sum].sum()

    revenue_series = list(grouped_df.items())[-1][1].sort_values(ascending=False)

    sellers_dict = get_sellers()
    sellers_dict_values = []
    seller_data = {'Vendedor': [], 'Faturamento': []}

    for seller_id, value in revenue_series.items():
        seller_data['Vendedor'].append(sellers_dict[seller_id])
        seller_data['Faturamento'].append(value)
        sellers_dict_values.append(sellers_dict[seller_id])

    print(seller_data)

    fig, ax = plt.subplots()
    best_sellers_df = pd.DataFrame.from_dict(seller_data)
    print(best_sellers_df['Vendedor'])

    best_sellers_df.plot(kind='barh', ax=ax, figsize=(11, 10), x=best_sellers_df.columns[0],
                         y=best_sellers_df.columns[1])

    for container in ax.containers:
        ax.bar_label(container)

    ax.set_title("Faturamento p/ vendedor")

    plt.show()


def get_sells_by_month():
    repo = Repository('Vendas')
    df = repo.get_table_data()

    df['Data'] = df['Data'].apply(lambda x: x.strftime('%m'))

    # for i in range(len(df)):
    #     df.loc[i, 'Data'] = df.loc[i, 'Data'].strftime('%m')

    sellers = get_sellers()
    print("\n Vendedores")
    print(sellers)
    seller_id = int(input("Selecione o ID do vendedor a ser analisado: "))
    seller_name = sellers[seller_id]

    seller_df = df.loc[df['VendedorID'] == seller_id]

    seller_grouped_df = seller_df.groupby('Data').sum()

    revenue_series = list(seller_grouped_df.items())[-1][1]

    fig, ax = plt.subplots()
    revenue_series.plot(kind='bar', ax=ax)

    for container in ax.containers:
        ax.bar_label(container)

    ax.set_title(f"Vendas mês a mês - {seller_name} ")

    plt.xlabel("Meses")
    plt.show()


def get_sellers() -> dict:
    repo = Repository('Vendedores')
    df = repo.get_table_data()

    df = df.set_index(df.columns[0])

    data_dict = df.squeeze().to_dict()

    return data_dict


if __name__ == '__main__':
    get_sells_by_month()
