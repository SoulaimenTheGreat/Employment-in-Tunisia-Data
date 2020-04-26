# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:55:33 2020

@author: Soulaimen
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from components.navbar import Navbar
from components.nav import Nav_Side
from components.button import Buttons
from plots.Population_Active_Visualisation import indicators,population_active_occupée,population_active_occupée_sex,population_active,population_active_sex
from plots.Population_occupée_Visualisation import Evolution_population_âge_activité,Evolution_population_âge_activité_sex,Evolution_créations_emploi,secteur_activité
from plots.chomage_visualisation import population_active_chômage,Taux_chômage,Taux_chômage_sexe,Taux_chômage_diplome,chomage_map
from plots.Own_account_workers import Travailleurs_independants,Travailleurs_independants_sex
from plots.Bureau_demploi_tt import Evolution_demandes_emploi,demande_emploi_hvf,demande_emploi,Demandes_emploi_Vs_Offres_reçues,evolution_offre_emploi,offre_emploi

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css',dbc.themes.BOOTSTRAP]
app=dash.Dash(__name__,external_stylesheets=external_stylesheets)

# components
nav=Navbar()
nav_side=Nav_Side()
buttons =Buttons()

# plots p1
fig1_max_t,fig1_max_t_m,fig1_max_f,fig_min_t,fig_min_t_m,fig_min_f=indicators()
pa=population_active()
pas=population_active_sex()
pao=population_active_occupée()
paos=population_active_occupée_sex()

# plots p2
epaa=Evolution_population_âge_activité ()
epaas=Evolution_population_âge_activité_sex()
ece=Evolution_créations_emploi()
sa=secteur_activité()

# plots p3
pac=population_active_chômage()
tc=Taux_chômage()
tcs=Taux_chômage_sexe()
tcd=Taux_chômage_diplome()
cm=chomage_map()

# plots p4
ede=Evolution_demandes_emploi()
dehf=demande_emploi_hvf()
de=demande_emploi()
devor=Demandes_emploi_Vs_Offres_reçues()
eoe=evolution_offre_emploi()
oe=offre_emploi()

# plots p5
ti=Travailleurs_independants()
tis=Travailleurs_independants_sex()

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

#app layout
app.layout = html.Div([
    dbc.Row(dbc.Col(nav)),
    dbc.Row(
            [
                dbc.Col(nav_side, width=2),
                dbc.Container(dbc.Col([
                               indicators_max_1,
                               indicators_min_1,
                               first,
                               second
                               ]))
                
            ]
        ),
    ],style={'background-color':'#f1f1f1'})
    


if __name__ == '__main__':
    app.run_server(debug=False,use_reloader=False)