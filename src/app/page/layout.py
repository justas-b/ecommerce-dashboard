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
    revenue_card = dbc.Card(dbc.CardBody([html.H5("Revenue"), revenue]))

    orders = appdata.TOT_ORDERS
    orders_card = dbc.Card(dbc.CardBody([html.H5("Orders"), orders]))

    items = appdata.TOT_ITEMS
    items_card = dbc.Card(dbc.CardBody([html.H5("Items Ordered"), items]))

    daily_revenue = appdata.DAILY_REVENUE
    daily_revenue_card = dbc.Card(dbc.CardBody([html.H5("Daily Revenue"), daily_revenue]))

    daily_order = appdata.DAILY_ORDERS
    daily_order_card = dbc.Card(dbc.CardBody([html.H5("Daily Orders"), daily_order]))

    date = f"{appdata.TOP_ORDERS_DATE.strftime('%Y-%m-%d')} [{appdata.TOP_ORDERS_DATE_CT} orders]"
    date_card = dbc.Card(dbc.CardBody([html.H5("Best Date"), date]))

    weekday = f"{appdata.TOP_ORDERS_DAY} [{appdata.TOP_ORDERS_DAY_CT} orders]"
    weekday_card = dbc.Card(dbc.CardBody([html.H5("Best Weekday"), weekday]))

    month = f"{appdata.TOP_ORDERS_MONTH} [{appdata.TOP_ORDERS_DAY_MONTH} orders]"
    month_card = dbc.Card(dbc.CardBody([html.H5("Best Month"), month]))

    country = f"{appdata.TOP_ORDERS_COUNTRY} [{appdata.TOP_ORDERS_COUNTRY_CT} orders]"
    country_card = dbc.Card(dbc.CardBody([html.H5("Top Country"), country]))

    overview_tab = dbc.Tab([
        html.Br(),
        dbc.Row([
            dbc.Col(revenue_card),
            dbc.Col(orders_card),
            dbc.Col(items_card),
            dbc.Col(daily_revenue_card),
            dbc.Col(daily_order_card)
        ])
    ], label="Overview", label_class_name="tab_label")

    winners_tab = dbc.Tab([
        html.Br(),
        dbc.Row([
            dbc.Col(date_card),
            dbc.Col(weekday_card),
            dbc.Col(month_card),
            dbc.Col(country_card),
        ])
    ], label="Winners", label_class_name="tab_label")

    info = html.Div([
        dbc.Tabs([
            overview_tab,
            winners_tab
        ]),
        html.Br()
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
    country_title = html.Div(id="country_plot_title")
    analytic_select = dbc.Select(
        id="country_analytic_callback",
        options=[
            {"label": "Orders", "value": "orders"},
            {"label": "Total Revenue", "value": "revenue"},
            {"label": "Average Revenue", "value": "mean_revenue"}
        ], 
        value="orders", 
        class_name="selector"
    )
    country_graph = dcc.Graph(id="country_plot_fig", style={"height": "70%"})
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
            dbc.Row([
                dbc.Col(init_country_plot()),
                dbc.Col(init_dispatch())
            ])
        ], className="main_div")
    ], className="page_div")

    return layout