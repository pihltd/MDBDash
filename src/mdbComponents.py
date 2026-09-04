from dash import html, dcc
import src.mdbStyles as ds


modeltable = html.Div([
    html.Hr(),
    html.H2("Latest Versions of models in MDB", id='modeltabletitle'),
    html.Div(id='modeltable'),
    html.Hr()
    ]
)

loadbutton = html.Div([
    dcc.Button("Click to load MDB data",id='loadbutton', n_clicks=0)
])



edptable = html.Div([
    html.Hr(),
    html.H2("EDPs in MDB", id='edptabletitle'),
    html.Div(id='edptable'),
    html.Hr()
    ]
)
