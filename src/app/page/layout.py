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
    revenue = html.P(f"Revenue: {appdata.TOT_REVENUE}")
    orders = html.P(f"Orders: {appdata.TOT_ORDERS}")
    items = html.P(f"Items Ordered: {appdata.TOT_ITEMS}")
    daily_revenue = html.P(f"Daily Revenue: {appdata.DAILY_REVENUE}")
    revenue_order = html.P(f"Revenue per Order: {appdata.REVENUE_PER_ORDER}")
    daily_order = html.P(f"Daily Orders: {appdata.DAILY_ORDERS}")

    day = html.P(f"Best Day: Orders - {appdata.TOP_ORDERS_DATE} {appdata.TOP_ORDERS_DATE_CT}")
    weekday = html.P(f"Best Weekday: Orders - {appdata.TOP_ORDERS_DAY} {appdata.TOP_ORDERS_DAY_CT}")
    month = html.P(f"Best Month: Orders - {appdata.TOP_ORDERS_MONTH} {appdata.TOP_ORDERS_DAY_MONTH}")
    country = html.P(f"Top Country: Orders - {appdata.TOP_ORDERS_COUNTRY} {appdata.TOP_ORDERS_COUNTRY_CT}")

    overview_tab = dcc.Tab(
        dbc.Row([
            dbc.Col(revenue),
            dbc.Col(orders),
            dbc.Col(items),
            dbc.Col(daily_revenue),
            dbc.Col(revenue_order),
            dbc.Col(daily_order),
        ]), label="Overview"
    )

    winners_tab = dcc.Tab(
        dbc.Row([
            dbc.Col(day),
            dbc.Col(weekday),
            dbc.Col(month),
            dbc.Col(country),
        ]), label="Winners"
    )

    info = html.Div([
        dcc.Tabs([
            overview_tab,
            winners_tab
        ])
    ], className="info_div")

    return info


def init_layout() -> html.Div:
    layout = html.Div([
        init_header(),
        init_info()
    ], className="main_div")

    return layout


# if __name__ == '__main__':
#     app.layout = html.Div(className="page_div", children=[
#         dbc.Row(children=[

#         dbc.Row(children=[
#             dbc.Col(children=[

#             dbc.Col(children=[
#                 dbc.Row(children=[
#                     dbc.Col(children=[
#                         html.Div(children=[
#                             html.Div(id="day_plot_title"),

#                             dbc.Select(
#                                 id="day_callback",
#                                 options=[
#                                     {"label": " Orders",
#                                     "value": "orders"},
#                                     {"label": " Revenue",
#                                     "value": "revenue"}
#                                 ], 
#                                 value="orders", 
#                                 class_name="selector"
#                             ),

#                             dcc.Graph(id="day_plot_fig", style={"height": "70%"}),

#                             dcc.Slider(
#                                 id="granularity_slider", 
#                                 min=1, max=3, value=1, step=1, 
#                                 marks={
#                                     1: "Daily", 2: "Weekly",  3: "Monthly"
#                                 }, 
#                                 className="slider_selector"
#                             ),
#                         ], className="inner_div"),
#                     ], class_name="top_left_div", width=9),

#                     dbc.Col(children=[
#                         html.Div(children=[
#                             html.Div(id="delivery_title"),

#                             dbc.Select(
#                                 id="delivery_callback",
#                                 options=[
#                                     {"label": " Orders", "value": "orders"},
#                                     {"label": " Revenue", "value": "revenue"}
#                                 ],
#                                 value="orders", 
#                                 class_name="selector"
#                             ),

#                             dcc.Graph(id="delivery_plot", style={"height": "70%"})
#                         ], className="inner_div")
#                     ], class_name="top_right_div"),
#                 ], className="top_body_div"),

#                 dbc.Row(children=[
#                     dbc.Col(children=[
#                         html.Div(children=[
#                             html.Div(id="country_plot_title"),
                            
#                             dbc.Select(
#                                 id="country_analytic_callback",
#                                 options=[
#                                     {"label": "Orders", "value": "orders"},
#                                     {"label": "Total Revenue", "value": "revenue"},
#                                     {"label": "Average Revenue", "value": "mean_revenue"}
#                                 ], 
#                                 value="orders", 
#                                 class_name="selector",
#                             ),

#                             dcc.Graph(id="country_plot_fig", style={"height": "70%"}),

#                             dbc.RadioItems(
#                                 id="head_tail_country_callback",
#                                 options=[
#                                     {"label": " Top", "value": "head"},
#                                     {"label": " Bottom", "value": "tail"}
#                                 ], value="head", 
#                                 inline=True, 
#                                 class_name="radio_selector"
#                             )
#                         ], className="inner_div")
#                     ], class_name="bottom_left_div", width=6),

#                     dbc.Col(children=[
#                         html.Div(children=[
#                             html.H4("Days to Dispatch"),
                            
#                             dcc.Graph(figure=appdata.extractor.days_to_dispatch(), style={"height": "75%"}),
#                         ], className="inner_div")                
#                     ], class_name="bottom_right_div"), 
#                 ], className="bottom_body_div")
#             ], class_name="body_div")
#         ], className="main_div"),
#     ])