# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:55:33 2020

@author: Soulaimen
"""


def show_dash():
 import dash
 import dash_core_components as dcc
 import dash_html_components as html

 external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']   
 app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

 app.layout = html.Div(children=[
     html.H1(children='Hello Ya ali'),

     html.Div(children='''
        Dash: A web application framework for Python.
    '''),


])

 if __name__ == '__main__':
    return app.run_server(debug=True)

print(fig1)