import pandas as pd


class DataTransformer():
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def clean_column_names(self) -> None:
        """Cleans the column names of the dataframe.
        """
        cleaned_columns = [col.replace(" ", "_").lower() for col in self.df.columns]
        self.df.columns = cleaned_columns
        
    def time_to_dispatch(self) -> None:
        """Number of days taken to dispatch order from order date.
        """
        self.df["days_to_dispatch"] = (self.df["date_posted"] - self.df["date_paid"]).dt.days
    
    @staticmethod
    def save_csv(df: pd.DataFrame, filename: str) -> None:
        """Saves the cleaned dataframe to a CSV.

        Args:
            df (pd.DataFrame): Dataframe to save to a CSV file.
            filename (str): Filename to save the df as.
        """
        df.to_csv(f"src/data/{filename}.csv", index=False)


if __name__ == "__main__":
    # change to the file name of the dirty CSV file
    FILE_NAME = "EtsySoldOrderItems2022.csv"
    df = pd.read_csv(f"src/data/{FILE_NAME}", parse_dates=["Date Paid", "Date Posted"])

    transformer = DataTransformer(df)
    transformer.clean_column_names()
    transformer.time_to_dispatch()
    transformer.save_csv(transformer.df, "cleaned-data")
