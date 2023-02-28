import pandas as pd
from typing import NoReturn

# change to columns you would like to keep
COLUMNS_TO_KEEP = ["item_name", "quantity", "price", "discount_amount", "order_delivery",
                   "item_total", "date_paid", "date_posted", "delivery_zipcode", "delivery_country"]
# change to the file name of the dirty CSV file
FILE_NAME = "sold-order-items.csv"

df = pd.read_csv(FILE_NAME, parse_dates=["Date Paid", "Date Posted"])


def clean_column_names(df: pd.DataFrame) -> NoReturn:
    """Cleans the column names of the dataframe"""
    cleaned_columns = [col.replace(" ", "_").lower() for col in df.columns]
    df.columns = cleaned_columns


def drop_unused_columns(columns_to_keep: list, df: pd.DataFrame) -> NoReturn:
    """Drops columns that will not be needed in the dashboard - need to specify the columns to keep"""
    to_drop = [col for col in df.columns if col not in columns_to_keep]
    df.drop(to_drop, axis=1, inplace=True)


def time_to_dispatch(df: pd.DataFrame) -> NoReturn:
    """Number of days taken to dispatch order from order date"""
    df["days_to_dispatch"] = (df["date_posted"] - df["date_paid"]).dt.days


def save_csv(df: pd.DataFrame) -> NoReturn:
    """Saves the cleaned dataframe to a CSV"""
    df.to_csv("cleaned-data.csv", index=False)


if __name__ == "__main__":
    clean_column_names(df)
    drop_unused_columns(COLUMNS_TO_KEEP, df)
    time_to_dispatch(df)
    save_csv(df)
