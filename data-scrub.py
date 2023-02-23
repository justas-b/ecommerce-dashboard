import pandas as pd
from typing import NoReturn

df = pd.read_csv("sold-order-items.csv")


def clean_column_names(df: pd.DataFrame) -> NoReturn:
    """Cleans the column names of the dataframe"""
    columns = df.columns
    cleaned_columns = [column.replace(" ", "_").lower() for column in columns]
    df.columns = cleaned_columns


def drop_unused_columns(columns_to_keep: list, df: pd.DataFrame) -> NoReturn:
    """Drops columns that will not be needed in the dashboard - need to specify the columns to keep"""
    to_drop = [col for col in df.columns if col not in columns_to_keep]
    df.drop(to_drop, axis=1, inplace=True)


if __name__ == "__main__":
    columns_to_keep = ["sale_date", "item_name", "quantity", "price"  "discount_amount", "order_delivery", "item_total", "date_posted", "delivery_zipcode", "delivery_country"]
    clean_column_names(df)
    drop_unused_columns(columns_to_keep, df)
    print(df.info())

#TODO:
#Convert dates to datetime