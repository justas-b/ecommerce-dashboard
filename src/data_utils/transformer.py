import sys
import json
import logging

import pandas as pd

sys.path.append("./")
from src.data_utils.generator import DataGenerator


class DataTransformer:
    """Class that loads a data file from src/data/, based on the filename in config.json, that can apply various methods to standardise the data. If there is no filename specified, data will be randomly generated. 
    """
    def __init__(self) -> None:
        self.random = False

        self.config = json.load(open("config.json"))
        self.df = self.load_file()

    def limit_columns(self) -> None:
        """Limits the columns only to columns that are used.
        """
        if not self.random:
            columns = list(self.config.values())[1:]
            self.df = self.df[columns]
        
    def time_to_dispatch(self) -> None:
        """Number of days taken to dispatch order from order date.
        """
        posted_date = self.config["POSTED_DATE"] if not self.random else "post_date"
        sale_date = self.config["SALE_DATE"] if not self.random else "sale_date"

        self.df["days_to_dispatch"] = (self.df[posted_date] - self.df[sale_date]).dt.days
    
    def apply_transformations(self) -> None:
        """Applies all transformation methods to the instantiated dataframe.
        """
        self.limit_columns()
        self.time_to_dispatch()

    def load_file(self) -> pd.DataFrame:
        """Loads the data using the filename from the config.json file (.csv or .xlsx format), or randomly generates data using a generator and saves it as 'sample_data' in src/data/.

        Returns:
            pd.DataFrame: Data in the form of a pandas dataframe.
        """
        filename = self.config["FILENAME"]
        # User data
        if filename is not None:
            try:
                df = pd.read_csv(f"src/data/{filename}.csv")
            except:
                try:
                    df = pd.read_excel(f"src/data/{filename}.xlsx")
                except Exception as e:
                    logging.error(f"File {filename} is not .csv or .xlsx format, or does not exist. Error: {e}")
        # Randomly generated data
        else:
            generator = DataGenerator(start="2023-01-01", end="2023-12-31")
            df = generator.generate_n_rows(rows=1000)
            generator.save_csv(df, filename="sample_data")

            self.random = True
            

        date_columns = list(filter(lambda x: "date" in x.lower(), df.columns))
        df[date_columns] = df[date_columns].apply(pd.to_datetime)

        return df