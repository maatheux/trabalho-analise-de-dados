from matplotlib import pyplot as plt
import pandas as pd

from repositories.repository import Repository

def display() -> None:
    print("\n")
    action_list = [
        'Clientes que mais gastaram - Top 10',
        'De onde os clientes mais compraram - Top 10'
    ]

    for i, v in enumerate(action_list):
        print(f'{i + 1} - {v}')
    action_value = int(input("Insira o valor da ação que deseja realizar: "))

    match action_value:
        case 1:
            get_top10_costumers()
        case 2:
            pass
        case _:
            return
        

def get_top10_costumers() -> None:
    repo = Repository('Vendas')
    df = repo.get_table_data()

    columns_to_sum = [col for col in df.columns if col != 'Data']

    grouped_df = df.groupby('ClienteID')[columns_to_sum].sum()

    revenue_series = list(grouped_df.items())[-1][1].sort_values(ascending=False).head(10)
    
    customers = get_costumers()['Cliente']

    clients_names_dict_values = []

    costumer_data = {}
    for costumer_id, value in revenue_series.items():
        costumer_data[customers[costumer_id]] = value
        clients_names_dict_values.append(customers[costumer_id])
    
    print(costumer_data)
    print(clients_names_dict_values)

    fig, ax = plt.subplots()
    best_sellers_df = pd.DataFrame(costumer_data, index=['Clientes'])
    best_sellers_df.plot(kind='barh', ax=ax, figsize=(10, 8))

    for container in ax.containers:
        ax.bar_label(container)

    ax.set_title("Clientes que mais gastaram - Top 10")
    ax.legend(clients_names_dict_values)

    plt.show()


def get_state_costumer_top10():
    repo = Repository('Vendas')
    df = repo.get_table_data()


def get_costumers():
    repo = Repository('Clientes')
    df = repo.get_table_data()

    df = df.set_index(df.columns[0])

    data_dict = df.squeeze().to_dict()
    
    return data_dict


if __name__ == '__main__':
    get_top10_costumers()

