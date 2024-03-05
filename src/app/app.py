import sys

from dash import Dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

sys.path.append("./")
from src.app.page.layout import init_layout
from src.app.page.callbacks import init_callbacks


load_figure_template("cerulean")
app = Dash(external_stylesheets=[dbc.themes.FLATLY])

app.layout = init_layout
init_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True, port=8080)