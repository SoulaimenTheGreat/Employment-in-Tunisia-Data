# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:55:33 2020

@author: Soulaimen
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css',dbc.themes.COSMO]
app=dash.Dash(external_stylesheets=external_stylesheets)

app = JupyterDash('SimpleExample')

buttons = html.Div(
    [
      dbc.Button("Analyse", color="success", className="mr-1"), 
      dbc.Button("Prédiction", color="primary", className="mr-1"),
    ])

app.layout = html.Div([
    dbc.Alert("This is a primary alert", color="primary",className="alert-link"),
    html.H1(children='Hello Ya ali'),
    buttons
#     html.Div([
#       dcc.Graph(figure=fig1),
#       dcc.Graph(figure=fig2)]),
#       dcc.Graph(figure=fig3),
#       dcc.Graph(figure=fig4)
])

app