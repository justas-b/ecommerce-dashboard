from dash import Dash, dcc, html
import dash_bootstrap_components as dbc


def init_layout() -> html.Div:
    pass


# if __name__ == '__main__':
#     app.layout = html.Div(className="page_div", children=[
#         dbc.Row(children=[
#             html.H1("E-commerce Dashboard"),

#             html.P(f"{appdata.START} to {appdata.END}", className="info_text")
#         ], className="header_div"),

#         dbc.Row(children=[
#             dbc.Col(children=[
#                 html.H3("Overview"),

#                 html.Hr(),
            
#                 html.P(f"Revenue: {appdata.TOT_REVENUE}", className="info_text"),

#                 html.P(f"Orders: {appdata.TOT_ORDERS}", className="info_text"),

#                 html.P(f"Items Ordered: {appdata.TOT_ITEMS}", className="info_text"),
            
#                 html.P(f"Daily Revenue: {appdata.DAILY_REVENUE}", className="info_text"),

#                 html.P(f"Revenue per Order: {appdata.REVENUE_PER_ORDER}", className="info_text"),

#                 html.P(f"Daily Orders: {appdata.DAILY_ORDERS}", className="info_text"),

#                 html.H4("Winners"),

#                 html.Hr(),
#                 # needs to be fixed to correctly extract the wanted data
#                 html.P(f"Day: Orders - {appdata.TOP_ORDERS_DATE} {appdata.TOP_ORDERS_DATE_CT}, Revenue - {appdata.TOP_REVENUE_DATE} {appdata.TOP_REVENUE_DATE_CT}", className="info_text"),

#                 html.P(f"Weekday: Orders - {appdata.TOP_ORDERS_DAY} {appdata.TOP_ORDERS_DAY_CT}, Revenue - {appdata.TOP_REVENUE_DAY} {appdata.TOP_REVENUE_DAY_CT}", className="info_text"),

#                 html.P(f"Month: Orders - {appdata.TOP_ORDERS_MONTH} {appdata.TOP_ORDERS_DAY_MONTH}, Revenue - {appdata.TOP_REVENUE_MONTH} {appdata.TOP_REVENUE_MONTH_CT}", className="info_text"),

#                 html.P(f"Country: Orders - {appdata.TOP_ORDERS_COUNTRY} {appdata.TOP_ORDERS_COUNTRY_CT}, Revenue -  {appdata.TOP_REVENUE_COUNTRY} {appdata.TOP_REVENUE_COUNTRY_CT}", className="info_text"),

#             ], class_name="sidebar_div", width=2),

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