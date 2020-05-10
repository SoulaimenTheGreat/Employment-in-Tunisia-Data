# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:12:46 2020

@author: Soulaimen
"""
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from plots.Population_occupée_Visualisation import Evolution_population_âge_activité,Evolution_population_âge_activité_sex,Evolution_créations_emploi,secteur_activité


epaa=Evolution_population_âge_activité()
epaas=Evolution_population_âge_activité_sex()
ece=Evolution_créations_emploi()
sa=secteur_activité()

page2=dbc.Col([
    dcc.Graph(figure=epaa),
    dcc.Graph(figure=epaas),
    dcc.Graph(figure=ece),
    dcc.Graph(figure=sa)
    ],id="page_2")

def Page2():
    return page2