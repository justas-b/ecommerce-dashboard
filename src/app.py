import sys

from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

sys.path.append("./")
from src.data_utils.transformer import DataTransformer
from src.data_utils.extractor import DataExtractor

transformer = DataTransformer()
transformer.apply_transformations()
extractor = DataExtractor(transformer.df)

load_figure_template("cerulean")
app = Dash(external_stylesheets=[dbc.themes.FLATLY])

START, END = extractor.date_range()

app.layout = html.Div(className="page_div", children=[
    dbc.Row(className="header_div", children=[
        dbc.Row(html.H1("E-commerce Dashboard")),

        dbc.Row(html.P(f"{START} to {END}"))
    ]),

    dbc.Row(className="main_div", children=[
        dbc.Col(class_name="sidebar_div", children=[
            html.H3("Overview"),
        
            dbc.Col(f"Revenue: {extractor.total_revenue()}", className="info_text"),

            dbc.Col(f"Orders: {extractor.total_orders()}", className="info_text"),

            dbc.Col(f"Items Ordered: {extractor.total_items()}", className="info_text"),
        
            dbc.Col(f"Daily Revenue: {round(extractor.total_revenue() / extractor.number_of_days(), 2)}", className="info_text"),

            dbc.Col(f"Revenue per Order: {round(extractor.total_revenue() / extractor.total_orders(), 2)}", className="info_text"),

            dbc.Col(f"Daily Orders: {round(extractor.total_orders() / extractor.number_of_days(), 2)}", className="info_text")
        ], width=2),

        dbc.Col(class_name="body_div", children=[
            dbc.Row(className="top_body_div", children=[
                dbc.Col(class_name="top_left_div", children=[
                    html.Div(children=[
                        html.Div(id="day_plot_title"),

                        dcc.Graph(id="day_plot_fig", style={"height": "70%"}),

                        dcc.Slider(id="granularity_slider", min=1, max=3, value=1, step=1, marks={1: "Daily", 2: "Weekly",  3: "Monthly"}),

                        dbc.RadioItems(
                            class_name="selector",               id="day_callback",
                            options=[
                                {"label": " Orders",
                                "value": "orders"},
                                {"label": " Revenue",
                                "value": "revenue"},
                            ], value="orders", inline=True
                        ),
                    ], className="inner_div"),
                ], width=9),

                dbc.Col(class_name="top_right_div", children=[
                    html.Div(children=[
                        html.Div(id="delivery_title"),

                        dcc.Graph(id="delivery_plot", style={"height": "70%"}),

                        html.Div(className="small", children=[
                            dbc.RadioItems(
                                class_name="selector", id="delivery_callback", options=[
                                    {"label": " Orders", "value": "orders"},
                                    {"label": " Revenue", "value": "revenue"}
                                ], value="orders", inline=True
                            )
                        ])
                    ], className="inner_div")
                ]),
            ]),

            dbc.Row(className="bottom_body_div", children=[
                dbc.Col(class_name="bottom_left_div", children=[
                    html.Div(children=[
                        html.Div(id="country_plot_title"),

                        dcc.Graph(id="country_plot_fig", style={"height": "70%"}),

                        dbc.Row(children=[
                            dbc.Col(children=[
                                dbc.Select(
                                    class_name="selector",   id="country_analytic_callback",
                                    options=[
                                        {"label": "Orders", "value": "orders"},
                                        {"label": "Total Revenue", "value": "total"},
                                        {"label": "Average Revenue", "value": "average"}
                                    ], value="orders"
                                )
                            ]),
                        ]),

                        dbc.Col(children=[
                            dbc.RadioItems(
                                class_name="selector", id="head_tail_country_callback",
                                options=[
                                    {"label": " Top", "value": "head"},
                                    {"label": " Bottom", "value": "tail"}
                                ], value="head", inline=True
                            )
                        ]),
                    ], className="inner_div")
                ], width=6),

                dbc.Col(class_name="bottom_right_div", children=[
                    html.Div(children=[
                        html.H3("Days to Dispatch"),
                        
                        dcc.Graph(figure=extractor.days_to_dispatch(), style={"height": "75%"}),
                    ], className="inner_div")                
                ]), 
            ])
        ])
    ]),
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
        nbins = extractor.number_of_days()
        output_title = "Daily"
    elif granularity == 2:
        nbins = extractor.number_of_weeks()
        output_title = "Weekly"
    else:
        nbins = extractor.number_of_months()
        output_title = "Monthly"

    if analytic == "orders":
        return html.H3(f"{output_title} Orders "), extractor.orders_per_day(bins=nbins)
    elif analytic == "revenue":
        return html.H3(f"{output_title} Revenue"), extractor.revenue_per_day(bins=nbins)


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
    output_title = "per Country"
    # head_tail input will be passed to the figure functions
    if analytic == "orders":
        return html.H3(f"Orders {output_title}"), extractor.orders_by_country(head_tail)
    elif analytic == "total":
        return html.H3(f"Total Revenue {output_title}"), extractor.total_revenue_per_country(head_tail)
    elif analytic == "average":
        return html.H3(f"Average Revenue {output_title}"), extractor.average_revenue_per_country(head_tail)


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
        return html.H3(f"Orders {output_title}"), extractor.order_delivery_charge()
    else:
        return html.H3(f"Revenue {output_title}"), extractor.revenue_delivery_charge()


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)