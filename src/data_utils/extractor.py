import math

import pandas as pd
import plotly.express as px


class DataExtractor:
    """Class that is able to extract various types of data from the input dataframe.

    Args:
        df (pd.DataFrame): Dataframe to extract data from.
    """
    def __init__(self, df: pd.DataFrame) -> None:
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
        return self.df["quantity"].sum()

    def total_revenue(self) -> float:
        """Total revenue of all orders.

        Returns:
            float: Total revenue.
        """
        return round(self.df["price"].sum(), 2)

    def average_revenue(self) -> float:
        """Average revenue across all orders.

        Returns:
            float: Average revenue across orders.
        """
        return round(self.df["price"].mean(), 2)

    def country_grouping(self, analytic: str) -> pd.Series:
        """Groups the countries based on an aggregate. Accepted aggregates are "orders", "revenue" and "mean_revenue".

        Args:
            analytic (str): Aggregate to group the countries by. Accepted aggregates are "orders", "revenue" and "mean_revenue".

        Returns:
            pd.Series: Countries and their respective aggregates grouped.
        """
        if analytic not in ["orders", "revenue", "mean_revenue"]:
            raise ValueError("Invalid aggregate - must be 'orders', 'revenue' or 'mean_revenue'.")
        
        if analytic == "orders":
            return self.df["country"].value_counts()
        else:
            grouped_data = self.df[["country", "price"]].groupby("country")["price"]
            if analytic == "revenue":
                return grouped_data.sum()
            return grouped_data.mean()

    def country_plots(self, analytic: str, order: str) -> px.bar:
        """Country plots that are used for the dashboard.

        Args:
            analytic (str): Aggregate to group the countries by. Accepted aggregates are "orders", "revenue" and "mean_revenue".
            order (str): Used to order the data - only "head" or "tail" are accepted.

        Returns:
            px.bar: Bar plot of the country data based on the analytic.
        """
        ascending = True if order == "head" else False
        axis_map = {
            "orders": "Orders", "revenue": "Revenue", "mean_revenue": "Average revenue"
        }

        grouped_country_series = self.country_grouping(analytic)
        sorted_grouping =grouped_country_series.sort_values(ascending=ascending).tail(10)

        fig = px.bar(sorted_grouping, x=sorted_grouping.values, y=sorted_grouping.index)
        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0), 
            xaxis_title=axis_map[analytic], 
            yaxis_title="Country"
        )

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

        fig = px.bar(data, x="Days to Dispatch", y="Orders")
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        
        return fig

    def order_delivery_charge(self) -> px.pie:
        """Pie chart of the total number of orders across free and paid deliveries.

        Returns:
            px.pie: Orders across paid and free deliveries.
        """
        orders_per_delivery = self.df["delivery_cost"].apply(
            lambda x: "Paid" if x else "Free").value_counts()
        data = {
            "Delivery Type": orders_per_delivery.keys(),
            "Orders": orders_per_delivery.values
        }

        fig = px.pie(data, values="Orders", names="Delivery Type")
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

        return fig

    def revenue_delivery_charge(self) -> px.pie:
        """Pie chart of the total revenue across free and paid deliveries.

        Returns:
            px.pie: Revenue across paid and free deliveries.
        """
        revenue_per_delivery = self.df[["delivery_cost", "price"]]
        revenue_per_delivery["delivery_cost"] = revenue_per_delivery["delivery_cost"].apply(
            lambda x: "Paid" if x else "Free")
        revenue_per_delivery = revenue_per_delivery.groupby("delivery_cost")["price"].sum()
        data = {
            "Delivery Type": revenue_per_delivery.keys(),
            "Revenue": revenue_per_delivery.values
        }

        fig = px.pie(data, values="Revenue", names="Delivery Type")
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

        return fig

    def orders_per_day(self, bins: int) -> px.histogram:
        """Histogram plot of the count of orders over the time range of the data.
        
        Args:
            bins (int): Number of bins in the histogram - acts like the granularity.

        Returns:
            px.histogram: Histogram plot of the count of orders over the time range of the data.
        """
        fig = px.histogram(self.df, x="date", nbins=bins)
        fig.update_layout(
            xaxis_title_text = "Date", 
            yaxis_title_text = "Orders",
            bargap=0.25,
            margin=dict(l=0, r=0, t=0, b=0)
        )

        return fig

    def revenue_per_day(self, bins: int) -> px.histogram:
        """Histogram plot of the sum of prices over the time range of the data.

        Args:
            bins (int): Number of bins in the histogram - acts like the granularity.

        Returns:
            px.histogram: Histogram plot of the sum of prices over the time range of the data.
        """
        fig = px.histogram(self.df, x="date", y="price", nbins=bins)
        fig.update_layout(
            xaxis_title_text = "Date", 
            yaxis_title_text = "Revenue",
            bargap=0.25,
            margin=dict(l=0, r=0, t=0, b=0)
        )

        return fig

    def date_range(self) -> tuple:
        """Extracts the date range from the data.

        Returns:
            tuple: Start and end dates of the data, in the format of yyyy-mm-dd.
        """
        start = self.df["date"].min().date()
        end = self.df["date"].max().date()

        return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")
    
    def number_of_days(self) -> int:
        """Gets the number of days that the data covers.

        Returns:
            int: The number of days that the data covers.
        """
        start = self.df["date"].min().date()
        end = self.df["date"].max().date()
        days = math.ceil((end - start).days)

        return days
    
    def number_of_weeks(self) -> int:
        """Gets the number of weeks that the data covers.

        Returns:
            int: The number of weeks that the data covers.
        """
        days = self.number_of_days()
        weeks = math.ceil(days / 7)

        return weeks

    def number_of_months(self) -> int:
        """Gets the number of months that the data covers.

        Returns:
            int: The number of months that the data covers.
        """
        days = self.number_of_days()
        months = math.ceil(days / (365/12))

        return months
    
    def best_datetime_performance(self, aggregate: str, decomposer: str) -> str:
        """Extracts information about the best performing date object - works for "dates", "weekday" and "months".

        Args:
            aggregate (str): Aggregate used to extract the relevant information - must be "orders" or "revenue".
            decomposer (str): Date decomposer to use - must be "date", "weekday" or "month".

        Returns:
            str: _description_
        """
        allowed_decomposers = ["date", "weekday", "month"]
        if decomposer not in ["date", "weekday", "month"]:
            raise ValueError(f"Invalid decomposer used - must be in {allowed_decomposers}.")
        
        if aggregate == "orders":
            return self.df[decomposer].value_counts().idxmax()
        elif aggregate == "revenue":
            return self.df.groupby(decomposer)["price"].sum().idxmax()
        else:
            raise ValueError("Invalid aggregate used.")