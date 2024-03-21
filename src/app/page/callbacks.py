import sys

from dash import Dash, html, Input, Output, State

sys.path.append("./")
from src.app.appdata import appdata


def init_callbacks(app: Dash) -> None:
    @app.callback(
        Output(component_id="day_plot_title", component_property="children"),
        Output(component_id="day_plot_fig", component_property="figure"),
        Input(component_id="day_callback", component_property="value"),
        Input(component_id="granularity_slider", component_property="value"),
    )
    def update_day_fig(analytic: str, granularity: int) -> tuple:
        """Callback function to update the 'days' title and figure.

        Args:
            analytic (str): Input from RadioItems where the input is 'orders' or 'revenue'.
            granularity (int): Input from a Slider widget where the input is 1, 2 or 3. The lower the input the higher the granularity is: 1 - daily, 2 - weekly, or 3 - monthly.

        Returns:
            tuple: Header element to update the title and a bar plot figure.
        """
        if granularity == 1:
            nbins = appdata.extractor.number_of_days()
            output_title = "Daily"
        elif granularity == 2:
            nbins = appdata.extractor.number_of_weeks()
            output_title = "Weekly"
        else:
            nbins = appdata.extractor.number_of_months()
            output_title = "Monthly"

        if analytic == "orders":
            return html.H4(f"{output_title} Orders "), appdata.extractor.orders_per_day(bins=nbins)
        elif analytic == "revenue":
            return html.H4(f"{output_title} Revenue"), appdata.extractor.revenue_per_day(bins=nbins)


    @app.callback(
        Output(component_id="country_plot_title", component_property="children"),
        Output(component_id="country_plot_fig", component_property="figure"),
        Input(component_id="country_analytic_callback", component_property="value"),
        Input(component_id="head_tail_country_callback", component_property="value")
    )
    def update_country_fig(analytic: str, head_tail: str) -> tuple:
        """Callback function to update the 'country' title and figure.

        Args:
            analytic_input (str): Input from a Select widget where the inputs can be 'orders', 'total' or 'average'.
            top_bottom_input (str): Input from a Select widget where the inputs can be 'head' or 'tail'.

        Returns:
            tuple: Header element to update the title and a bar plot figure.
        """
        country_plot = appdata.extractor.country_plots(analytic, head_tail)
        label = country_plot["layout"]["xaxis"]["title"]["text"]

        return html.H4(f"{label} per Country"), country_plot
    
    @app.callback(
        Output("date_collapse", "is_open"),
        [Input("date_collapse_button", "n_clicks")],
        [State("date_collapse", "is_open")],
    )
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open