# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:23:42 2020

@author: Soulaimen
"""

import dash_bootstrap_components as dbc

def Nav_Side():
    nav = dbc.Navbar(
        dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink("population active", href="#")),
            dbc.NavItem(dbc.NavLink("population occupée", href="#")),
            dbc.NavItem(dbc.NavLink("population en chômage",href="#" )),
            dbc.NavItem(dbc.NavLink("secteur privé", href="#")),
            dbc.NavItem(dbc.NavLink("bureau d'emploi", href="#"))
        
        ],
        vertical="md"
    ))
    return nav