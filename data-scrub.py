import pandas as pd
from typing import NoReturn

df = pd.read_csv("sold-order-items.csv")


def clean_column_names(df: pd.DataFrame) -> NoReturn:
    """Cleans the column names of the dataframe"""
    columns = df.columns
    cleaned_columns = [column.replace(" ", "_").lower() for column in columns]
    df.columns = cleaned_columns


clean_column_names(df)