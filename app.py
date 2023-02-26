from dash import Dash, dcc, html
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
            html.H2("Orders per Day"),
            dcc.Graph(figure=orders_per_day())
        ]),
        html.Div(id="bottom_plot_div", children=[
            html.Div(className="indiv_bottom_graph", children=[
                html.H2("Orders per Country"),
                dcc.Graph(figure=orders_by_country())
                ]),
            html.Div(className="indiv_bottom_graph", children=[
                html.H2("Orders per Delivery Type"),
                dcc.Graph(figure=order_delivery_charge())]),
            html.Div(className="indiv_bottom_graph", children=[
                html.H2("Days to Dispatch"),
                dcc.Graph(figure=days_to_dispatch())])
        ])
    ])

if __name__ == "__main__":
    app.run_server(debug=True, port=8080)