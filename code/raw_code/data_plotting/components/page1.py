# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:49:22 2020

@author: Soulaimen
"""
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from plots.Population_Active_Visualisation import indicators,population_active_occupée,population_active_occupée_sex,population_active,population_active_sex


# plots p1
fig1_max_t,fig1_max_t_m,fig1_max_f,fig_min_t,fig_min_t_m,fig_min_f=indicators()
pa=population_active()
pas=population_active_sex()
pao=population_active_occupée()
paos=population_active_occupée_sex()

indicators_max_1=dbc.Row([
                  dbc.Col(dcc.Graph(figure=fig1_max_t)),
                  dbc.Col(dcc.Graph(figure=fig1_max_t_m)),
                  dbc.Col(dcc.Graph(figure=fig1_max_f))
                         ],style={'padding-top':'0.5%'})

indicators_min_1=dbc.Row([
                  dbc.Col(dcc.Graph(figure=fig_min_t)),
                  dbc.Col(dcc.Graph(figure=fig_min_t_m)),
                  dbc.Col(dcc.Graph(figure=fig_min_f)),
    ],style={'padding-top':'0.5%'})    

                      
first=dbc.Row(
             [dbc.Col(dcc.Graph(figure=pa)),
              dbc.Col(dcc.Graph(figure=pas))],style={'padding-top':'0.5%'})
second=dbc.Row(
             [dbc.Col(dcc.Graph(figure=pao)),
              dbc.Col(dcc.Graph(figure=paos),style={'padding-top':'0.5%'})
    ])

page1=dbc.Col([
                               indicators_max_1,
                               indicators_min_1,
                               first,
                               second
                               ],id="page_1")
def Page1():
    return page1