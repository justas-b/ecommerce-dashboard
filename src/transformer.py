import os
import json
import logging

import pandas as pd

# TODO:
# have several ways of loading the data initially
# None - loads most recent excel/csv file from src/data/
# str - load the file of the specific filename

class DataTransformer():
    """Class that loads a data file from src/data/, based on the filename in config.json, that can apply various methods to standardise the data. 
    """
    def __init__(self) -> None:
        self.df = self.load_file()

    def clean_column_names(self) -> None:
        """Cleans the column names of the dataframe.
        """
        cleaned_columns = [col.replace(" ", "_").lower() for col in self.df.columns]
        self.df.columns = cleaned_columns
        
    def time_to_dispatch(self) -> None:
        """Number of days taken to dispatch order from order date.
        """
        self.df["days_to_dispatch"] = (self.df["date_posted"] - self.df["date_paid"]).dt.days
    
    def apply_transformations(self) -> None:
        """Applies all transformation methods to the instantiated dataframe.
        """
        self.clean_column_names()
        self.time_to_dispatch()

    @staticmethod
    def load_file() -> pd.DataFrame:
        # can have a filename input and then load a csv or excel file
        # no input and load the most recent file eithe csv or excel
        filename = json.load(open("config.json"))["FILENAME"]
        if filename is not None:
            try:
                df = pd.read_csv(f"src/data/{filename}.csv")
            except:
                try:
                    df = pd.read_excel(f"src/data/{filename}.xlsx")
                except Exception as e:
                    logging.error(f"File {filename} is not .csv or .xlsx format, or does not exist. Error: {e}")

        # return df

    @staticmethod
    def save_csv(df: pd.DataFrame, filename: str) -> None:
        """Saves the cleaned dataframe to a CSV.

        Args:
            df (pd.DataFrame): Dataframe to save to a CSV file.
            filename (str): Filename to save the df as.
        """
        df.to_csv(f"src/data/{filename}.csv", index=False)


if __name__ == "__main__":
    transformer = DataTransformer()
    print(transformer.df)