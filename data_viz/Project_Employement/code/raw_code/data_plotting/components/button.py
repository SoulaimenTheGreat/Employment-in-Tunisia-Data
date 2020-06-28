# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:05:15 2020

@author: Soulaimen
"""
import dash_html_components as html
import dash_bootstrap_components as dbc

def Buttons():
    buttons = html.Div(
        [
          dbc.Button("Analyse", color="primary", className="mr-1"), 
          dbc.Button("Prédiction", color="secondary", className="mr-1"),
        ],style={'padding-left':'40%',
                 'padding-top':'0.5%'})
    return buttons             