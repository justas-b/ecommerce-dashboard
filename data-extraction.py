# TODO:
# total quantity of items ordered
# orders per delivery country
# total and average revenue per country
# distribution of days taken to dispatch orders
# order distribution across free and paid deliveries
# total revenue across free and paid deliveries
# avg and sum of total order revenue
# orders and item revenue per item
# map of orders
# avg quantity per order

import pandas as pd
import plotly.express as px

df = pd.read_csv("cleaned-data.csv", parse_dates=["date_paid", "date_posted"])


def total_orders(df: pd.DataFrame) -> int:
    """Extracts the total number of orders"""
    return df.shape[0]