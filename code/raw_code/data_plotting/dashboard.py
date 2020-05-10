# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:55:33 2020

@author: Soulaimen
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output,State
from components.navbar import Navbar
# from components.nav import Nav_Side
from components.button import Buttons
from components.page1 import Page1
from components.page2 import Page2
from plots.chomage_visualisation import population_active_chômage,Taux_chômage,Taux_chômage_sexe,Taux_chômage_diplome,chomage_map
from plots.Own_account_workers import Travailleurs_independants,Travailleurs_independants_sex
from plots.Bureau_demploi_tt import Evolution_demandes_emploi,demande_emploi_hvf,demande_emploi,Demandes_emploi_Vs_Offres_reçues,evolution_offre_emploi,offre_emploi

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css',dbc.themes.BOOTSTRAP]
app=dash.Dash(__name__,external_stylesheets=external_stylesheets)

# components
nav=Navbar()
# nav_side=Nav_Side()
buttons =Buttons()

# # plots p1
page1=Page1()

# plots p2
page2=Page2()

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



#app layout
app.layout = html.Div([
    dbc.Row(dbc.Col(nav)),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
    # dbc.Row(
    #         [
                
    #             dbc.Container(id="page_1",children=page1),
    #             dbc.Container(id="page_2",children=page2)

                
    #         ]
    #     ),
    ],style={'background-color':'#f1f1f1'})


    
# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page1
    elif pathname == '/page-2':
        return page2
    else:
        return "URL not found"

if __name__ == '__main__':
    app.run_server(debug=False,use_reloader=False)