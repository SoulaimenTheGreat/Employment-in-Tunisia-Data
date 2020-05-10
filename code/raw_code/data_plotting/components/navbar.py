# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:34:37 2020

@author: Soulaimen
"""
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

# def Navbar():
#     PLOTLY_LOGO = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Tunisia_logo.svg/1200px-Tunisia_logo.svg.png"
    
#     # make a reuseable dropdown for the different examples
#     dropdown = dbc.DropdownMenu(
#         children=[
#             dbc.DropdownMenuItem("population active",id="population_1"),
#             dbc.DropdownMenuItem("population occupée",id="population_2"),
#             dbc.DropdownMenuItem("Entry 3"),
#         ],
#         label="Menu",
#         color="warning",
#         className="m-1"
#     )
    
#     search_bar = dbc.Row(
#         [
#             dbc.Col(dbc.Input(type="search", placeholder="Search")),
#             dbc.Col(
#                 dbc.Button("Search", color="success", className="ml-2"),
#                 width="auto",
#             ),
#         ],
#         no_gutters=True,
#         className="ml-auto flex-nowrap mt-3 mt-md-0",
#         align="center",
#     )
    
#     navbar = dbc.Navbar(
#         [
#             html.A(
#                 # Use row and col to control vertical alignment of logo / brand
#                 dbc.Row(
#                     [
#                         dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
#                         dbc.Col(dbc.NavbarBrand("Dashboard de la Tunisie", className="ml-2")),
#                     ],
#                     align="center",
#                     no_gutters=True,
#                 )
#             ),
#             dbc.Collapse(dbc.Col(dropdown)),
#             dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
#         ],
#         color="primary",
#         dark=True,
#     )
#     return navbar


# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[
        dcc.Link(dbc.DropdownMenuItem("population active",id="population_1"),href='/page-1'),
        dcc.Link(dbc.DropdownMenuItem("population occupée",id="population_2"),href='/page-2'),
        dbc.DropdownMenuItem("Entry 3"),
    ],
    label="Menu",
    color="warning",
    className="m-1"
)           
               
               
# here's how you can recreate the same thing using Navbar
# (see also required callback at the end of the file)
search_navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("Employement in Tunisia"),
            dbc.NavbarToggler(id="navbar-toggler3"),
            dropdown,
            dbc.Collapse(
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Input(type="search", placeholder="Search")
                        ),
                        dbc.Col(
                            dbc.Button(
                                "Search", color="primary", className="ml-2"
                            ),
                            # set width of button column to auto to allow
                            # search box to take up remaining space.
                            width="auto",
                        ),
                    ],
                    no_gutters=True,
                    # add a top margin to make things look nice when the navbar
                    # isn't expanded (mt-3) remove the margin on medium or
                    # larger screens (mt-md-0) when the navbar is expanded.
                    # keep button and search box on same row (flex-nowrap).
                    # align everything on the right with left margin (ml-auto).
                    className="ml-auto flex-nowrap mt-3 mt-md-0",
                    align="center",
                ),
                id="navbar-collapse3",
                navbar=True,
            ),
        ]
    ),
    color='white'
)
            
def Navbar():
   return  search_navbar            


