# TODO:
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


def total_items(df: pd.DataFrame) -> int:
    """Extracts the total number of items ordered"""
    return df["quantity"].sum()


def orders_by_country(df: pd.DataFrame) -> px.bar:
    """Bar plot of the distribution of orders per country"""
    country_count = df["delivery_country"].value_counts()
    data = {
        "Country": reversed(country_count.keys()), 
        "Orders": reversed(country_count.values)
    }

    fig = px.bar(data, x="Orders", y="Country", text="Orders")
    fig.update_traces(textposition="outside")

    return fig


def total_revenue_per_country(df: pd.DataFrame) -> px.bar:
    """Bar plot of the total revenue per country"""
    country_revenue = df[["delivery_country", "item_total"]]
    country_revenue = country_revenue.groupby("delivery_country")["item_total"].sum().sort_values()
    data ={
        "Country": country_revenue.keys(),
        "Total Revenue (£)": country_revenue.values
    }

    fig = px.bar(data, x="Total Revenue (£)", y="Country", text="Total Revenue (£)")
    fig.update_traces(textposition="outside")

    return fig


def average_revenue_per_country(df: pd.DataFrame) -> px.bar:
    """Bar plot of the average revenue per country"""
    avg_country_revenue = df[["delivery_country", "item_total"]]
    avg_country_revenue = avg_country_revenue.groupby("delivery_country")["item_total"].mean().sort_values()
    data = {
        "Country": avg_country_revenue.keys(),
        "Average Revenue (£)": [round(val, 2) for val in avg_country_revenue.values]
    }

    fig = px.bar(data, x="Average Revenue (£)", y="Country", text="Average Revenue (£)")
    fig.update_traces(textposition="outside")

    return fig