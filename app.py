from dash import Dash, dcc, html
import dash_bootstrap_components  as dbc
from data_extraction import total_orders, total_items, total_revenue, average_revenue

app = Dash(external_stylesheets=[
           dbc.themes.ZEPHYR])

app.layout = html.Div(
    id="parent_div", children=[
        html.Div(id="header_div", children=[
            html.H1("E-commerce Dashboard"),
            html.P("Dashboard Info")
        ], style={"text-align": "center", "font-size": "20px"}),
        html.Div(id="info_div", children=[
            html.P(f"Orders: {total_orders()}", style={"text-align": "center","width": "24%", "display": "inline-block"}),
            html.P(f"Items Ordered: {total_items()}", style={"text-align": "center", "width": "24%", "display": "inline-block"}),
            html.P(f"Revenue: £{total_revenue()}", style={"text-align": "center", "width": "24%", "display": "inline-block"}),
            html.P(f"Average Revenue: £{average_revenue()}", style={"text-align": "center", "width": "24%", "display": "inline-block"})
        ]),
        html.Div(id="top_plot_div", children=[
            html.H1("Top Plot Div")
        ]),
        html.Div(id="bottom_plot_div", children=[
            html.H1("Bottom Plot Div")
        ])
    ])

if __name__ == "__main__":
    app.run_server(debug=True, port=8080)