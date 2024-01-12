import math
import datetime


class DataGenerator():
    def __init__(self):
        self.countries = open("src/data/countries.txt").read().split("\n")
        pass

    def get_random_num(self, start: int, end: int) -> int:
        pass

    def generate_date(self, start: int, end: int, max_days=int|None) -> datetime.datetime:
        pass

    def generate_country(self) -> str:
        pass
    
    def generate_row(self):
        pass

    
    # generate random sale date
    # generate random quantity
    # generate random price
    # generate random paid date
    # generate random posted date
    # generate random country
    # generate random delivery cost


if __name__ == "__main__":
    generator = DataGenerator()
    print(generator.generate_country())