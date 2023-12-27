import sys

sys.path.append("./")

from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

from src import data_extraction


load_figure_template("cerulean")

app = Dash(external_stylesheets=[dbc.themes.LUX])

START, END = data_extraction.date_range()

app.layout = html.Div(children=[
    dbc.Col(className="header_div", children=[
        dbc.Row(html.H1("E-commerce Dashboard")),
        dbc.Row(html.P(f"{START} to {END}")),
        dbc.Row(id="info_div", children=[
            dbc.Col(f"Orders: {data_extraction.total_orders()}",
                    className="info_text"),
            dbc.Col(f"Items Ordered: {data_extraction.total_items()}",
                    className="info_text"),
            dbc.Col(f"Revenue: £{data_extraction.total_revenue()}",
                    className="info_text"),
            dbc.Col(
                f"Average Revenue: £{data_extraction.average_revenue()}", className="info_text")
        ]),
    ]),

    dbc.Card(
        dbc.CardBody([
            dbc.Row(id="top_plot_div", children=[
                dbc.Col(className="graph_div", children=[
                    dbc.Row(html.Div(id="day_plot_title")),
                    dbc.Row(dcc.Graph(id="day_plot_fig")),
                    dbc.Row(html.Div(className="small", children=[
                        dbc.RadioItems(className="selector", id="day_callback",
                            options=[
                                {"label": " Orders",
                                 "value": "orders"},
                                {"label": " Revenue",
                                 "value": "revenue"},
                            ],
                            value="orders", inline=True)]
                    ))
                ])
            ], justify="center"),

            dbc.Row(id="bottom_plot_div", children=[
                dbc.Col(className="graph_div", children=[
                    html.Div(id="country_plot_title"),
                    dcc.Graph(id="country_plot_fig"),
                    dbc.Select(className="selector", id="country_callback",
                               options=[
                                   {"label": "Orders", "value": "orders"},
                                   {"label": "Total Revenue", "value": "total"},
                                   {"label": "Average Revenue", "value": "average"}
                               ], value="orders")
                ]),

                dbc.Col(className="graph_div", children=[
                    html.Div(id="delivery_title"),
                    dcc.Graph(id="delivery_plot"),
                    html.Div(className="small", children=[
                        dbc.RadioItems(className="selector", id="delivery_callback",
                                       options=[
                                           {"label": " Orders", "value": "orders"},
                                           {"label": " Revenue", "value": "revenue"}],
                                       value="orders", inline=True)])]),

                dbc.Col(className="graph_div", children=[
                    html.H2("Days to Dispatch"),
                    dcc.Graph(figure=data_extraction.days_to_dispatch())])
            ])
        ])
    )
])


@app.callback(
    Output(component_id="day_plot_title", component_property="children"),
    Output(component_id="day_plot_fig", component_property="figure"),
    Input(component_id="day_callback", component_property="value")
)
def update_day_fig(input: str) -> tuple:
    """Callback function to update the 'days' title and figure.

    Args:
        input (str): Input from RadioItems where the input is 'orders' or 'revenue'.

    Returns:
        tuple: Header element to update the title and a bar plot figure.
    """
    output_title = "per Day"

    if input == "orders":
        return html.H2(f"Orders {output_title}"), data_extraction.orders_per_day()
    elif input == "revenue":
        return html.H2(f"Revenue {output_title}"), data_extraction.revenue_per_day()


@app.callback(
    Output(component_id="country_plot_title", component_property="children"),
    Output(component_id="country_plot_fig", component_property="figure"),
    Input(component_id="country_callback", component_property="value")
)
def update_country_fig(input: str) -> tuple:
    """Callback function to update the 'country' title and figure.

    Args:
        input (str): Input from a Select widget where the inputs can be 'orders', 'total' or 'average'.

    Returns:
        tuple: Header element to update the title and a bar plot figure.
    """
    output_title = "per Country"

    if input == "orders":
        return html.H2(f"Orders {output_title}"), data_extraction.orders_by_country()
    elif input == "total":
        return html.H2(f"Total Revenue {output_title}"), data_extraction.total_revenue_per_country()
    elif input == "average":
        return html.H2(f"Average Revenue {output_title}"), data_extraction.average_revenue_per_country()


@app.callback(
    Output(component_id="delivery_title", component_property="children"),
    Output(component_id="delivery_plot", component_property="figure"),
    Input(component_id="delivery_callback", component_property="value")
)
def update_delivery_fig(input: str) -> tuple:
    """Callback function to update the 'delivery' title and figure.

    Args:
        input (str): Input from a RadioItems widget where the inputs can be 'orders' or 'revenue'.

    Returns:
        tuple: Header element to update the title and a bar plot figure.
    """
    output_title = "per Delivery Type"

    if input == "orders":
        return html.H2(f"Orders {output_title}"), data_extraction.order_delivery_charge()
    else:
        return html.H2(f"Revenue {output_title}"), data_extraction.revenue_delivery_charge()


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
