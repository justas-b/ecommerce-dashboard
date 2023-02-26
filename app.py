from dash import Dash, dcc, html
import dash_bootstrap_components  as dbc

app = Dash(external_stylesheets=[
           dbc.themes.ZEPHYR])

app.layout = html.Div(
    id="parent_div", children=[
        html.Div(id="header_div", children=[
            html.H1("E-commerce Dashboard"),
            html.P("Dashboard Info")
        ], style={"text-align": "center", "font-size": "20px"}),
        html.Div(id="info_div", children=[
            html.P("Orders: 50", style={"text-align": "center","width": "24%", "display": "inline-block"}),
            html.P("Items Ordered: 55", style={"text-align": "center", "width": "24%", "display": "inline-block"}),
            html.P("Revenue: £1000", style={"text-align": "center", "width": "24%", "display": "inline-block"}),
            html.P("Average Revenue: £30", style={"text-align": "center", "width": "24%", "display": "inline-block"})
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