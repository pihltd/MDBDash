import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from dash import dash_table


def stsRequest(url):
    headers =  {'accept': 'application/json'}
    try:
        retry = Retry(total=5, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        session = requests.Session()
        session.mount('https://', adapter)
        result = session.get(url=url, headers=headers, timeout=160)
        
        if result.status_code == 200:
            return(result.json())
        else:
            return None
    except requests.exceptions.HTTPError as e:
        print ("HTTP Error: {e}")
        return None



def buildBasicTable(df, diffstyle = None, dedup = True):
    if dedup:
        #Get rid of empty columns and rows
        df.dropna(how='all', axis=1, inplace=True)
        df.dropna(how='all', axis=0, inplace=True)
    if diffstyle is None:
        styles = [{'if':{'row_index':'odd'}, 'backgroundColor': 'rgb(220,220,220)'}]
    else:
        styles = diffstyle

    return dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{"name": e, "id": e} for e in (df.columns)],
            style_table={'overflowX':'auto'},
            style_cell={'overflow':'hidden', 'textOverflow':'ellipsis', 'maxWidth':10, 'textAlign':'center'},
            style_data={'color':'black', 'backgroundColor':'white'},
            style_data_conditional=styles,
            style_header={'backgroundColor': 'rgb(210,210,210)', 'color':'black', 'fontWeight':'bold', 'textAlign':'center'},
            tooltip_data=[
                {
                    column:{'value': str(value), 'type':'markdown'}
                    for column, value in row.items()
                } for row in df.to_dict('records')
            ],
            tooltip_duration=None,
            export_format="csv"
        )

