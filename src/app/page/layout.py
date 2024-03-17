import sys

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

sys.path.append("./")
from src.app.appdata import appdata


def init_header() -> html.Div:
    """Header element for the dashboard.

    Returns:
        html.Div: Header Div component.
    """
    header_text = html.H1("E-commerce Dashboard")
    date_range = html.P(f"{appdata.START} to {appdata.END}")

    header = html.Div([
        header_text,
        date_range
    ], className="header_div")
    
    return header


def init_info() -> html.Div:
    """Information element for the dashboard.

    Returns:
        html.Div: Information Div component.
    """
    revenue = appdata.TOT_REVENUE
    revenue_div = dbc.Card(children=[dbc.CardHeader("Revenue"), dbc.CardBody(revenue)])

    orders = appdata.TOT_ORDERS
    orders_div = dbc.Card(children=[dbc.CardHeader("Orders"), dbc.CardBody(orders)])

    items = appdata.TOT_ITEMS
    items_div = dbc.Card(children=[dbc.CardHeader("Items Ordered"), dbc.CardBody(items)])

    daily_revenue = appdata.DAILY_REVENUE
    daily_revenue_div = dbc.Card(children=[dbc.CardHeader("Daily Revenue"), dbc.CardBody(daily_revenue)])

    revenue_order = appdata.REVENUE_PER_ORDER
    revenue_order_div = dbc.Card(children=[dbc.CardHeader("Revenue per Order"), dbc.CardBody(revenue_order)])

    daily_order = appdata.DAILY_ORDERS
    daily_order_div = dbc.Card(children=[dbc.CardHeader("Daily Orders"), dbc.CardBody(daily_order)])

    date = f"{appdata.TOP_ORDERS_DATE.strftime('%Y-%m-%d')} [{appdata.TOP_ORDERS_DATE_CT} orders]"
    date_div = dbc.Card(children=["Best Date", date])

    weekday = html.P(f"{appdata.TOP_ORDERS_DAY} [{appdata.TOP_ORDERS_DAY_CT} orders]")
    weekday_div = dbc.Card(children=["Best Weekday", weekday])

    month = html.P(f"{appdata.TOP_ORDERS_MONTH} [{appdata.TOP_ORDERS_DAY_MONTH} orders]")
    month_div = dbc.Card(children=["Best Month", month])

    country = html.P(f"{appdata.TOP_ORDERS_COUNTRY} [{appdata.TOP_ORDERS_COUNTRY_CT} orders]")
    country_div = dbc.Card(children=["Top Country", country])

    overview_tab = dbc.Tab(
        dbc.Row([
            dbc.Col(revenue_div),
            dbc.Col(orders_div),
            dbc.Col(items_div),
            dbc.Col(daily_revenue_div),
            dbc.Col(revenue_order_div),
            dbc.Col(daily_order_div)
        ]), label="Overview"
    )

    winners_tab = dbc.Tab(
        dbc.Row([
            dbc.Col(date_div),
            dbc.Col(weekday_div),
            dbc.Col(month_div),
            dbc.Col(country_div),
        ]), label="Winners"
    )

    info = html.Div([
        dbc.Tabs([
            overview_tab,
            winners_tab
        ])
    ], className="info_div")

    return info


def init_date_plot() -> html.Div:
    """Date plot element that displays the trend of orders and revenue across date. Daily, weekly and monthly granularities are available.

    Returns:
        html.Div: Date plot div element.
    """
    title = html.Div(id="day_plot_title")
    select = dbc.Select(
        id="day_callback",
        options=[
            {"label": " Orders",
            "value": "orders"},
            {"label": " Revenue",
            "value": "revenue"}
        ], 
        value="orders", 
        class_name="selector"
    )
    graph = dcc.Graph(id="day_plot_fig", style={"height": "70%"})
    slider = dcc.Slider(
        id="granularity_slider", 
        min=1, max=3, value=1, step=1, 
        marks={
            1: "Daily", 2: "Weekly",  3: "Monthly"
        }, 
        className="slider_selector"
    )

    day_div = html.Div([
        title,
        select,
        graph,
        slider
    ], className="day_div")

    return day_div
    

def init_country_plot() -> html.Div:
    """Country plot element that displays the trends across countries, along with the best and worst performing ones.

    Returns:
        html.Div: Country plot div element.
    """
    country_title = html.Div(id="country_plot_title"),
    analytic_select = dbc.Select(
        id="country_analytic_callback",
        options=[
            {"label": "Orders", "value": "orders"},
            {"label": "Total Revenue", "value": "revenue"},
            {"label": "Average Revenue", "value": "mean_revenue"}
        ], 
        value="orders", 
        class_name="selector",
    ),
    country_graph = dcc.Graph(id="country_plot_fig"),
    top_bottom_radio = dbc.RadioItems(
        id="head_tail_country_callback",
        options=[
            {"label": " Top", "value": "head"},
            {"label": " Bottom", "value": "tail"}
        ], value="head", 
        inline=True, 
        class_name="radio_selector"
    )

    country_div = html.Div([
        country_title,
        analytic_select,
        country_graph,
        top_bottom_radio
    ], className="country_div")

    return country_div


def init_dispatch() -> html.Div:
    """Dispatch plot element that displays the distribution of days taken to dispatch orders.

    Returns:
        html.Div: Dispatch plot div element.
    """
    dispatch_title = html.H4("Days to Dispatch")          
    dispatch_graph = dcc.Graph(figure=appdata.extractor.days_to_dispatch(), style={"height": "75%"})

    dispatch_div = html.Div([
        dispatch_title,
        dispatch_graph
    ], className="dispatch_div")

    return dispatch_div


def init_layout() -> html.Div:
    """Main application layout initialisation function. Used to initialise the layout and all elements contained within it.

    Returns:
        html.Div: Layout div element.
    """
    layout = html.Div([
        html.Div([
            init_header(),
            init_info(),
            init_date_plot(),
            # init_country_plot(),
            init_dispatch()
        ], className="main_div")
    ], className="page_div")

    return layout