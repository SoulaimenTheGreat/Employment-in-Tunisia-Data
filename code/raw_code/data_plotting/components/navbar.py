# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:34:37 2020

@author: Soulaimen
"""
import dash_bootstrap_components as dbc
import dash_html_components as html


def Navbar():
    PLOTLY_LOGO = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Tunisia_logo.svg/1200px-Tunisia_logo.svg.png"
    
    search_bar = dbc.Row(
        [
            dbc.Col(dbc.Input(type="search", placeholder="Search")),
            dbc.Col(
                dbc.Button("Search", color="success", className="ml-2"),
                width="auto",
            ),
        ],
        no_gutters=True,
        className="ml-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )
    
    navbar = dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Dashboard de la Tunisie", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                )
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
        ],
        color="primary",
        dark=True,
    )
    return navbar


