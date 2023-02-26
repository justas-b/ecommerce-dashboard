# TODO:
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


def total_revenue(df: pd.DataFrame) -> float:
    """Total revenue of all orders"""
    return round(df["item_total"].sum(), 2)


def average_revenue(df: pd.DataFrame) -> float:
    """Average revenue across all orders"""
    return round(df["item_total"].mean(), 2)


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


def days_to_dispatch(df: pd.DataFrame) -> px.bar:
    """Bar plot of the distribution of the days taken to dispatch orders"""
    time_to_dispatch = df["days_to_dispatch"].value_counts().sort_index()
    data = {
        "Days to Dispatch": time_to_dispatch.keys(),
        "Orders": time_to_dispatch.values
    }

    fig = px.bar(data, x="Days to Dispatch", y="Orders", text="Orders")
    fig.update_traces(textposition="outside")

    return fig


def order_delivery_charge(df: pd.DataFrame) -> px.pie:
    """Pie chart of the total number of orders across free and paid deliveries
    """
    orders_per_delivery = df["order_delivery"].apply(
        lambda x: "Paid" if x else "Free").value_counts()
    data = {
        "Delivery Type": orders_per_delivery.keys(),
        "Orders": orders_per_delivery.values
    }

    fig = px.pie(data, values="Orders", names="Delivery Type")

    return fig


def revenue_delivery_charge(df: pd.DataFrame) -> px.pie:
    """Pie chart of the total revenue across free and paid deliveries"""
    revenue_per_delivery = df[["order_delivery", "item_total"]]
    revenue_per_delivery["order_delivery"] = revenue_per_delivery["order_delivery"].apply(lambda x: "Paid" if x else "Free")
    revenue_per_delivery = revenue_per_delivery.groupby("order_delivery")["item_total"].sum()
    data = {
        "Delivery Type": revenue_per_delivery.keys(),
        "Revenue": revenue_per_delivery.values
    }

    fig = px.pie(data, values="Revenue", names="Delivery Type")

    return fig


def orders_per_day(df: pd.DataFrame) -> px.bar:
    """Bar plot of the number of orders per day"""
    num_per_day = df["date_paid"].value_counts().sort_index()
    data = {
        "Date": num_per_day.keys(),
        "Orders": num_per_day.values
    }
    fig = px.bar(data, x="Date", y="Orders")

    return fig