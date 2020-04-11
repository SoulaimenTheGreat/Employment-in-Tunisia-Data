# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:55:33 2020

@author: Soulaimen
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from navbar import Navbar
from nav import Nav_Side
from button import Buttons


external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css',dbc.themes.BOOTSTRAP]
app=dash.Dash(__name__,external_stylesheets=external_stylesheets)



nav=Navbar()
nav_side=Nav_Side()

buttons =Buttons() 


app.layout = html.Div([
    dbc.Row(dbc.Col(nav)),
    dbc.Row(
            [
                dbc.Col(nav_side, width=2),
                dbc.Col(buttons),
                
            ]
        )
    ],style={'background-color':'#f1f1f1'})

if __name__ == '__main__':
    app.run_server(debug=False,use_reloader=False)