from dash import Input, Output, State, dash_table
from dash.exceptions import PreventUpdate
from mdbDashboard import app
import src.mdbSubroutines as ms
import pandas as pd
import io


#
#  Populate Datastores
#

@app.callback(
    Output(component_id='modelstore', component_property='data'),
    Input(component_id='loadbutton', component_property='n_clicks')
)
def populateModelStore(n_clicks):
    url = 'https://sts.cancer.gov/v2/models/?skip=0&limit=0'
    modeljson = ms.stsRequest(url=url)
    df = pd.DataFrame(modeljson)
    return df.to_json(orient='split')



@app.callback(
    Output(component_id='edpstore', component_property='data'),
    Input(component_id='loadbutton', component_property='n_clicks')
)
def populateEDPStore(n_clicks):
    edpowner = 'CRDC'
    url = f"https://sts.cancer.gov/v2/edps/{edpowner}?skip=0&limit=0"
    modeljson = ms.stsRequest(url=url)
    df = pd.DataFrame(modeljson)
    return df.to_json(orient='split')

#
# Table Callbacks
#


@app.callback(
    Output(component_id='modeltable', component_property='children'),
    Input(component_id='modelstore', component_property='data')
)
def populateModelTable(modelstore):
    df = pd.read_json(io.StringIO(modelstore), orient='split')
    current_df = df.loc[df['is_latest_version'] == True]

    
    return ms.buildBasicTable(df=current_df)




@app.callback(
    Output(component_id='edptable', component_property='children'),
    Input(component_id='edpstore', component_property='data')
)
def populateEDPTable(edpstore):
    df = pd.read_json(io.StringIO(edpstore), orient='split')

    
    return ms.buildBasicTable(df=df)