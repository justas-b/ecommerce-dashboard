import random
import datetime


class DataGenerator():
    def __init__(self, start: str, end: str):
        self.start = start
        self.end = end
        self.countries = open("src/data/countries.txt").read().split("\n")

    def get_random_num(self, start: int, end: int) -> int:
        """Generates a random integer between a start and end number (inclusive).

        Args:
            start (int): Starting number (inclusive).
            end (int): Ending number (inclusive).

        Returns:
            int: Random integer between start and end (inclusive).
        """
        num = random.randint(start, end)

        return num

    def generate_date(self, start: str, end: str, max_days: int|None=None) -> datetime.datetime:
        """Generates a random date between a start and end date. A max_days can be specified to restrict the range of the number of days, however, this range cannot be larger than the difference in days between the start and end dates.

        Args:
            start (str): Start date in the format of 'YYYY-MM-DD'.
            end (str): End date in the format of 'YYYY-MM-DD'
            max_days (int | None, optional): The maximum number of days to consider in the range; will use the difference between start and end if None. Defaults to None.

        Returns:
            datetime.datetime: The random date as a datetime object.
        """
        start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
        days_diff = (end_date - start_date).days
        days = days_diff if ((max_days is None) or (max_days > days_diff)) else max_days

        random_days = self.get_random_num(start=0, end=days)
        random_date = start_date + datetime.timedelta(days=random_days)

        return random_date

    def generate_country(self) -> str:
        """Selects a random country from the list of countries.

        Returns:
            str: Random country.
        """
        index = self.get_random_num(0, len(self.countries)-1)
        country = self.countries[index]
        
        return country
    
    def generate_row(self) -> list:
        """Generates a row of random data in order of sale date, quantity, price, post date, country and delivery cost.

        Returns:
            list: Row of random data in order of sale date, quantity, price, post date, country and delivery cost
        """
        sale_date = self.generate_date(start=self.start, end=self.end)
        quantity = self.get_random_num(start=1, end=5)
        price = round(self.get_random_num(1, 100) + random.random(), 2)
        post_date = self.generate_date(start=datetime.datetime.strftime(sale_date, "%Y-%m-%d"), end=self.end, max_days=7)
        country = self.generate_country()
        delivery_cost = 0 if self.get_random_num(start=0, end=1) == 0 else round(price*0.2, 2)

        row = [sale_date, quantity, price, post_date, country, delivery_cost]

        return row


if __name__ == "__main__":
    generator = DataGenerator(start="2023-01-01", end="2023-12-31")
    print(generator.generate_row())