import pandas as pd

# change to columns you would like to keep
COLUMNS_TO_KEEP = ["item_name", "quantity", "price", "discount_amount", "order_delivery",
                   "item_total", "date_paid", "date_posted", "delivery_zipcode", "delivery_country"]
# change to the file name of the dirty CSV file
FILE_NAME = "EtsySoldOrderItems2022.csv"

df = pd.read_csv(f"src/data/{FILE_NAME}", parse_dates=["Date Paid", "Date Posted"])


def clean_column_names(df: pd.DataFrame) -> None:
    """Cleans the column names of the dataframe.

    Args:
        df (pd.DataFrame): Dataframe where the column names are to be normalised. 
    """
    cleaned_columns = [col.replace(" ", "_").lower() for col in df.columns]
    df.columns = cleaned_columns


def time_to_dispatch(df: pd.DataFrame) -> None:
    """Number of days taken to dispatch order from order date.

    Args:
        df (pd.DataFrame): Dataframe with 'date_posted' and 'date_paid' columns.
    """
    df["days_to_dispatch"] = (df["date_posted"] - df["date_paid"]).dt.days


def save_csv(df: pd.DataFrame, filename: str) -> None:
    """Saves the cleaned dataframe to a CSV.

    Args:
        df (pd.DataFrame): Dataframe to save to a CSV file.
        filename (str): Filename to save the df as.
    """
    df.to_csv(f"src/data/{filename}.csv", index=False)


if __name__ == "__main__":
    clean_column_names(df)
    time_to_dispatch(df)
    save_csv(df, "cleaned-data")
