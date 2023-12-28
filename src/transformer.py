import pandas as pd

# TODO:
# have several ways of loading the data initially
# None - loads most recent excel/csv file from src/data/
# str - load the file of the specific filename

class DataTransformer():
    def __init__(self, filename: str) -> None:
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
    def load_file(filename: str) -> pd.DataFrame:
        pass

    @staticmethod
    def save_csv(df: pd.DataFrame, filename: str) -> None:
        """Saves the cleaned dataframe to a CSV.

        Args:
            df (pd.DataFrame): Dataframe to save to a CSV file.
            filename (str): Filename to save the df as.
        """
        df.to_csv(f"src/data/{filename}.csv", index=False)