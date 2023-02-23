import pandas as pd
import datetime
from typing import NoReturn

COLUMNS_TO_KEEP = ["item_name", "quantity", "price", "discount_amount", "order_delivery", "item_total", "date_paid", "date_posted", "delivery_zipcode", "delivery_country"]
FILE_NAME = "sold-order-items.csv"

df = pd.read_csv(FILE_NAME)


def clean_column_names(df: pd.DataFrame) -> NoReturn:
    """Cleans the column names of the dataframe"""
    cleaned_columns = [col.replace(" ", "_").lower() for col in df.columns]
    df.columns = cleaned_columns


def drop_unused_columns(columns_to_keep: list, df: pd.DataFrame) -> NoReturn:
    """Drops columns that will not be needed in the dashboard - need to specify the columns to keep"""
    to_drop = [col for col in df.columns if col not in columns_to_keep]
    df.drop(to_drop, axis=1, inplace=True)


def convert_to_date(df: pd.DataFrame) -> NoReturn:
    """Converts dates to datetime objects"""
    date_cols = [col for col in df.columns if "date" in col]

    for col in date_cols:
        df[col] = pd.to_datetime(df[col])


def time_to_dispatch(df: pd.DataFrame) -> NoReturn:
    """Number of days taken to dispatch order from order date"""
    df["days_to_dispatch"] = (df["date_posted"] - df["date_paid"]).dt.days


def save_csv(df: pd.DataFrame) -> NoReturn:
    """Saves the cleaned dataframe to a CSV"""
    df.to_csv("cleaned_data.csv")


if __name__ == "__main__":
    clean_column_names(df)
    drop_unused_columns(COLUMNS_TO_KEEP, df)
    convert_to_date(df)
    time_to_dispatch(df)
    save_csv(df)