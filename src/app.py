import sys

from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

sys.path.append("./")
from src.assets import appdata

load_figure_template("cerulean")
app = Dash(external_stylesheets=[dbc.themes.FLATLY])

app.layout = html.Div(className="page_div", children=[
    dbc.Row(children=[
        html.H1("E-commerce Dashboard"),

        html.P(f"{appdata.START} to {appdata.END}", className="info_text")
    ], className="header_div"),

    dbc.Row(children=[
        dbc.Col(children=[
            html.H3("Overview"),

            html.Hr(),
        
            html.P(f"Revenue: {appdata.TOT_REVENUE}", className="info_text"),

            html.P(f"Orders: {appdata.TOT_ORDERS}", className="info_text"),

            html.P(f"Items Ordered: {appdata.TOT_ITEMS}", className="info_text"),
        
            html.P(f"Daily Revenue: {appdata.DAILY_REVENUE}", className="info_text"),

            html.P(f"Revenue per Order: {appdata.REVENUE_PER_ORDER}", className="info_text"),

            html.P(f"Daily Orders: {appdata.DAILY_ORDERS}", className="info_text"),

            html.H4("Winners"),

            html.Hr(),
            # needs to be fixed to correctly extract the wanted data
            html.P(f"Day: Orders - {appdata.TOP_ORDERS_DATE} {appdata.TOP_ORDERS_DATE_CT}, Revenue - {appdata.TOP_REVENUE_DATE} {appdata.TOP_REVENUE_DATE_CT}", className="info_text"),

            html.P(f"Weekday: Orders - {appdata.TOP_ORDERS_DAY} {appdata.TOP_ORDERS_DAY_CT}, Revenue - {appdata.TOP_REVENUE_DAY} {appdata.TOP_REVENUE_DAY_CT}", className="info_text"),

            html.P(f"Month: Orders - {appdata.TOP_ORDERS_MONTH} {appdata.TOP_ORDERS_DAY_MONTH}, Revenue - {appdata.TOP_REVENUE_MONTH} {appdata.TOP_REVENUE_MONTH_CT}", className="info_text"),

            html.P(f"Country: Orders - {appdata.TOP_ORDERS_COUNTRY} {appdata.TOP_ORDERS_COUNTRY_CT}, Revenue -  {appdata.TOP_REVENUE_COUNTRY} {appdata.TOP_REVENUE_COUNTRY_CT}", className="info_text"),

        ], class_name="sidebar_div", width=2),

        dbc.Col(children=[
            dbc.Row(children=[
                dbc.Col(children=[
                    html.Div(children=[
                        html.Div(id="day_plot_title"),

                        dbc.Select(
                            id="day_callback",
                            options=[
                                {"label": " Orders",
                                "value": "orders"},
                                {"label": " Revenue",
                                "value": "revenue"}
                            ], 
                            value="orders", 
                            class_name="selector"
                        ),

                        dcc.Graph(id="day_plot_fig", style={"height": "70%"}),

                        dcc.Slider(
                            id="granularity_slider", 
                            min=1, max=3, value=1, step=1, 
                            marks={
                                1: "Daily", 2: "Weekly",  3: "Monthly"
                            }, 
                            className="slider_selector"
                        ),
                    ], className="inner_div"),
                ], class_name="top_left_div", width=9),

                dbc.Col(children=[
                    html.Div(children=[
                        html.Div(id="delivery_title"),

                        dbc.Select(
                            id="delivery_callback",
                            options=[
                                {"label": " Orders", "value": "orders"},
                                {"label": " Revenue", "value": "revenue"}
                            ],
                            value="orders", 
                            class_name="selector"
                        ),

                        dcc.Graph(id="delivery_plot", style={"height": "70%"})
                    ], className="inner_div")
                ], class_name="top_right_div"),
            ], className="top_body_div"),

            dbc.Row(children=[
                dbc.Col(children=[
                    html.Div(children=[
                        html.Div(id="country_plot_title"),
                        
                        dbc.Select(
                            id="country_analytic_callback",
                            options=[
                                {"label": "Orders", "value": "orders"},
                                {"label": "Total Revenue", "value": "revenue"},
                                {"label": "Average Revenue", "value": "mean_revenue"}
                            ], 
                            value="orders", 
                            class_name="selector",
                        ),

                        dcc.Graph(id="country_plot_fig", style={"height": "70%"}),

                        dbc.RadioItems(
                             id="head_tail_country_callback",
                            options=[
                                {"label": " Top", "value": "head"},
                                {"label": " Bottom", "value": "tail"}
                            ], value="head", 
                            inline=True, 
                            class_name="radio_selector"
                        )
                    ], className="inner_div")
                ], class_name="bottom_left_div", width=6),

                dbc.Col(children=[
                    html.Div(children=[
                        html.H4("Days to Dispatch"),
                        
                        dcc.Graph(figure=appdata.extractor.days_to_dispatch(), style={"height": "75%"}),
                    ], className="inner_div")                
                ], class_name="bottom_right_div"), 
            ], className="bottom_body_div")
        ], class_name="body_div")
    ], className="main_div"),
])


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
    Output(component_id="delivery_title", component_property="children"),
    Output(component_id="delivery_plot", component_property="figure"),
    Input(component_id="delivery_callback", component_property="value")
)
def update_delivery_fig(analytic: str) -> tuple:
    """Callback function to update the 'delivery' title and figure.

    Args:
        analytic (str): Input from a RadioItems widget where the inputs can be 'orders' or 'revenue'.

    Returns:
        tuple: Header element to update the title and a bar plot figure.
    """
    output_title = "per Delivery Type"

    if analytic == "orders":
        return html.H4(f"Orders {output_title}"), appdata.extractor.order_delivery_charge()
    else:
        return html.H4(f"Revenue {output_title}"), appdata.extractor.revenue_delivery_charge()


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)