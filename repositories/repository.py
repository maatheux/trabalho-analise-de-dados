import pandas as pd
from dotenv import load_dotenv
import os


class Repository:
    def __init__(self, sheet: str):
        load_dotenv()
        self.sheet = sheet
        self.file_path = os.getenv("FILE_PATH")

    def get_table_data(self) -> pd.DataFrame:
        df = pd.read_excel(self.file_path, sheet_name=self.sheet)
        return df


if __name__ == '__main__':
    #load_dotenv()

    repo = Repository('Vendedores')
    print(repo.get_table_data())
