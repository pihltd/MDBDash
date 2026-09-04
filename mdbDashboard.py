from dash import Dash, html, dcc

from src.mdbComponents import *
from src.mdbStyles import *
from src.mdbSubroutines import *


app = Dash(
    __name__,
    #external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=True,
    update_title="Updating..."
)
app.title ="CRDC Submission Dashboard"

app.layout = html.Div([
    dcc.Store(id='modelstore'),
    dcc.Store(id='edpstore'),
    loadbutton, modeltable, edptable
])


from src.mdbCallbackss import *


if __name__ == "__main__":
    app.run(port=8050, debug=True)