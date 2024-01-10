import json

import pandas as pd
import plotly.express as px


class DataExtractor():
    """Class that is able to extract various types of data from the input dataframe.

    Args:
        df (pd.DataFrame): Dataframe to extract data from.
    """
    def __init__(self, df: pd.DataFrame) -> None:
        self.config = json.load(open("config.json"))
        self.df = df

    def total_orders(self) -> int:
        """Extracts the total number of orders.

        Returns:
            int: Number of orders.
        """
        return self.df.shape[0]

    def total_items(self) -> int:
        """Extracts the total number of items ordered.

        Returns:
            int: Number of items ordered.
        """
        return self.df[self.config["QUANTITY"]].sum()

    def total_revenue(self) -> float:
        """Total revenue of all orders.

        Returns:
            float: Total revenue.
        """
        return round(self.df[self.config["PRICE"]].sum(), 2)

    def average_revenue(self) -> float:
        """Average revenue across all orders.

        Returns:
            float: Average revenue across orders.
        """
        return round(self.df[self.config["PRICE"]].mean(), 2)

    def orders_by_country(self) -> px.bar:
        """Bar plot of the distribution of orders per country.

        Returns:
            px.bar: Bar plot of orders per country.
        """
        country_count = self.df[self.config["COUNTRY"]].value_counts()
        data = {
            "Country": reversed(country_count.keys()),
            "Orders": reversed(country_count.values)
        }

        fig = px.bar(data, x="Orders", y="Country", text="Orders")

        return fig

    def total_revenue_per_country(self) -> px.bar:
        """Bar plot of the total revenue per country.

        Returns:
            px.bar: Bar plot of revenue per country.
        """
        country_revenue = self.df[["delivery_country", "item_total"]]
        country_revenue = country_revenue.groupby("delivery_country")[
            "item_total"].sum().sort_values()
        data = {
            "Country": country_revenue.keys(),
            "Total Revenue (£)": country_revenue.values
        }

        fig = px.bar(data, x="Total Revenue (£)",
                    y="Country", text="Total Revenue (£)")

        return fig

    def average_revenue_per_country(self) -> px.bar:
        """Bar plot of the average revenue per country.

        Returns:
            px.bar: Bar plot of average revenue per country.
        """
        avg_country_revenue = self.df[[self.config["COUNTRY"], self.config["PRICE"]]]
        avg_country_revenue = avg_country_revenue.groupby(
            self.config["COUNTRY"])[self.config["PRICE"]].mean().sort_values()
        data = {
            "Country": avg_country_revenue.keys(),
            "Average Revenue (£)": [round(val, 2) for val in avg_country_revenue.values]
        }

        fig = px.bar(data, x="Average Revenue (£)",
                    y="Country", text="Average Revenue (£)")

        return fig

    def days_to_dispatch(self) -> px.bar:
        """Bar plot of the distribution of the days taken to dispatch orders.

        Returns:
            px.bar: Distribution of days taken to dispatch.
        """
        time_to_dispatch = self.df["days_to_dispatch"].value_counts().sort_index()
        data = {
            "Days to Dispatch": time_to_dispatch.keys(),
            "Orders": time_to_dispatch.values
        }

        fig = px.bar(data, x="Days to Dispatch", y="Orders", text="Orders")
        fig.update_traces(textposition="outside")

        return fig

    def order_delivery_charge(self) -> px.pie:
        """Pie chart of the total number of orders across free and paid deliveries.

        Returns:
            px.pie: Orders across paid and free deliveries.
        """
        orders_per_delivery = self.df[self.config["DELIVERY_COST"]].apply(
            lambda x: "Paid" if x else "Free").value_counts()
        data = {
            "Delivery Type": orders_per_delivery.keys(),
            "Orders": orders_per_delivery.values
        }

        fig = px.pie(data, values="Orders", names="Delivery Type")

        return fig

    def revenue_delivery_charge(self) -> px.pie:
        """Pie chart of the total revenue across free and paid deliveries.

        Returns:
            px.pie: Revenue across paid and free deliveries.
        """
        revenue_per_delivery = self.df[[self.config["DELIVERY_COST"], self.config["PRICE"]]]
        revenue_per_delivery[self.config["DELIVERY_COST"]] = revenue_per_delivery[self.config["DELIVERY_COST"]].apply(
            lambda x: "Paid" if x else "Free")
        revenue_per_delivery = revenue_per_delivery.groupby(self.config["DELIVERY_COST"])[self.config["PRICE"]].sum()
        data = {
            "Delivery Type": revenue_per_delivery.keys(),
            "Revenue": revenue_per_delivery.values
        }

        fig = px.pie(data, values="Revenue", names="Delivery Type")

        return fig

    def orders_per_day(self) -> px.bar:
        """Bar plot of the number of orders per day.

        Returns:
            px.bar: Bar plot of the number of orders per day.
        """
        num_per_day = self.df[self.config["PAID_DATE"]].value_counts().sort_index()
        data = {
            "Date": num_per_day.keys(),
            "Orders": num_per_day.values
        }
        fig = px.bar(data, x="Date", y="Orders", text="Orders")
        fig.update_traces(textposition="outside")

        return fig

    def revenue_per_day(self) -> px.bar:
        """Bar plot of the revenue per day.

        Returns:
            px.bar: Bar plot of the revenue per day.
        """
        rev_per_day = self.df[[self.config["PAID_DATE"], self.config["PRICE"]]].groupby(self.config["PAID_DATE"])[self.config["PRICE"]].sum()
        data = {
            "Date": rev_per_day.keys(),
            "Revenue (£)": rev_per_day.values
        }

        fig = px.bar(data, x="Date", y="Revenue (£)", text="Revenue (£)")
        fig.update_traces(textposition="outside")

        return fig

    def date_range(self) -> tuple:
        """Extracts the date range from the data.

        Returns:
            tuple: Start and end dates of the data, in the format of dd/mm/yyyy.
        """
        start = self.df[self.config["PAID_DATE"]].min().date()
        end = self.df[self.config["PAID_DATE"]].max().date()

        return start.strftime("%d/%m/%Y"), end.strftime("%d/%m/%Y")