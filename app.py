from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components  as dbc
from data_extraction import *

app = Dash(external_stylesheets=[
           dbc.themes.ZEPHYR])

app.layout = html.Div(
    id="parent_div", children=[
        html.Div(className="header_div", id="header_div", children=[
            html.H1("E-commerce Dashboard"),
            html.P("Dashboard Info")
        ]),
        html.Div(id="info_div", children=[
            html.P(className="info_text", children=[
                f"Orders: {total_orders()}"]),
            html.P(className="info_text", children=[
                f"Items Ordered: {total_items()}"]),
            html.P(className="info_text", children=[
                f"Revenue: £{total_revenue()}"]),
            html.P(className="info_text", children=[
                f"Average Revenue: £{average_revenue()}"])
        ]),
        html.Div(className="top_plot_div", id="top_plot_div", children=[
            html.Div(id="day_plot_title"),
            dcc.Graph(id="day_plot_fig"),
            dcc.RadioItems(className="radio_item", id="day_callback", 
            options=[
                {"label": "Orders", "value": "orders"},
                {"label": "Revenue", "value": "revenue"},
            ], value="orders")
            ]),
        html.Div(id="bottom_plot_div", children=[
            html.Div(className="indiv_bottom_graph", children=[
                html.Div(id="country_plot_title"),
                dcc.Graph(id="country_plot_fig"),
                dcc.Dropdown(className="dropdown", id="country_callback",
                options=[
                    {"label": "Orders", "value": "orders"},
                    {"label": "Total Revenue", "value": "total"},
                    {"label": "Average Revenue", "value": "average"}
                ], value="orders", clearable=False)
                ]),
            html.Div(className="indiv_bottom_graph", children=[
                html.H2("Orders per Delivery Type"),
                dcc.Graph(figure=order_delivery_charge())]),
            html.Div(className="indiv_bottom_graph", children=[
                html.H2("Days to Dispatch"),
                dcc.Graph(figure=days_to_dispatch())])
        ])
    ])


@app.callback(
    Output(component_id="day_plot_title", component_property="children"),
    Output(component_id="day_plot_fig", component_property="figure"),
    Input(component_id="day_callback", component_property="value")
)
def update_day_fig(input: str) -> tuple:
    """Callback function to update the 'days' title and figure"""
    output_title = "per Day"

    if input == "orders":
        return html.H2(f"Orders {output_title}"), orders_per_day()
    else:
        return html.H2(f"Revenue {output_title}"), revenue_per_day()


@app.callback(
    Output(component_id="country_plot_title", component_property="children"),
    Output(component_id="country_plot_fig", component_property="figure"),
    Input(component_id="country_callback", component_property="value")
)
def update_country_fig(input: str) -> tuple:
    """Callback function to update the 'country' title and figure"""
    output_title = "per Country"

    if input == "orders":
        return html.H2(f"Orders {output_title}"), orders_by_country()
    elif input == "total":
        return html.H2(f"Total Revenue {output_title}"), total_revenue_per_country()
    else:
        return html.H2(f"Average Revenue {output_title}"), average_revenue_per_country()


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)