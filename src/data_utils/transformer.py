import os
import json
import glob
import logging

import pandas as pd


class DataTransformer():
    """Class that loads a data file from src/data/, based on the filename in config.json, that can apply various methods to standardise the data. 
    """
    def __init__(self) -> None:
        self.config = json.load(open("config.json"))
        self.df = self.load_file()

    def limit_columns(self) -> None:
        """Limits the columns only to columns that are used.
        """
        columns = list(self.config.values())[1:]
        self.df = self.df[columns]
        
    def time_to_dispatch(self) -> None:
        """Number of days taken to dispatch order from order date.
        """
        self.df["days_to_dispatch"] = (self.df[self.config["POSTED_DATE"]] - self.df[self.config["PAID_DATE"]]).dt.days
    
    def apply_transformations(self) -> None:
        """Applies all transformation methods to the instantiated dataframe.
        """
        self.limit_columns()
        self.time_to_dispatch()

    def load_file(self) -> pd.DataFrame:
        """Loads the data using the filename from the config.json file (.csv or .xlsx format), or loads the most recent data file from src/data/.

        Returns:
            pd.DataFrame: Data in the form of a pandas dataframe.
        """
        filename = self.config["FILENAME"]
        if filename is not None:
            try:
                df = pd.read_csv(f"src/data/{filename}.csv")
            except:
                try:
                    df = pd.read_excel(f"src/data/{filename}.xlsx")
                except Exception as e:
                    logging.error(f"File {filename} is not .csv or .xlsx format, or does not exist. Error: {e}")
        else:
            files = glob.glob("src/data/*.xlsx") + glob.glob("src/data/*.csv")

            if len(files) == 0:
                logging.error("File is not .csv or .xlsx format, or does not exist in src/data/.")
                exit()

            latest_file = max(files, key=os.path.getctime)
            file_type = latest_file.split(".")[-1]

            df = pd.read_excel(latest_file) if file_type == "xlsx" else pd.read_csv(latest_file)

        date_columns = list(filter(lambda x: "date" in x.lower(), df.columns))
        df[date_columns] = df[date_columns].apply(pd.to_datetime)

        return df

    @staticmethod
    def save_csv(df: pd.DataFrame, filename: str) -> None:
        """Saves the cleaned dataframe to a CSV.

        Args:
            df (pd.DataFrame): Dataframe to save to a CSV file.
            filename (str): Filename to save the df as.
        """
        df.to_csv(f"src/data/{filename}.csv", index=False)