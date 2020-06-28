#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import plotly.graph_objects as go

# In[2]:


df_Population_Be_1=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/bureau d'emploi/Socio économique 02_22_2020 22_04_20.csv",
                                header=1)
df_Population_Be_1


# In[3]:


fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df_Population_Be_1[' '], y=df_Population_Be_1["Evolution des demandes d'emploi enregistrées"], name='Total',
                         line = dict(color='lightseagreen')))

fig1.update_layout(title="",template='plotly_white',font=dict(
                 family=" Gravitas One, cursive",
                 size=13))
def Evolution_demandes_emploi():
   return fig1


# In[4]:


fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=df_Population_Be_1[' '], 
    y=df_Population_Be_1["Demandes d'emploi enregistrées des Masculins"],
    name='Homme',
    marker_color='royalblue'
))
fig2.add_trace(go.Bar(
    x=df_Population_Be_1[' '],
    y=df_Population_Be_1["demandes d'emploi enregistrées des Feminins"],
    name='Femme',
    marker_color='tomato'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig2.update_layout(barmode='group', xaxis_tickangle=-45,title="",template="plotly_white",font=dict(
                 family=" Gravitas One, cursive",
                 size=13))
def demande_emploi_hvf():
   return fig2


# In[12]:


# Initialize figure
fig3 = go.Figure()

# Add Traces

fig3.add_trace(
    go.Scatter(x=df_Population_Be_1[' '],
               y=df_Population_Be_1["Evolution des demandes d'emploi enregistrées"],
               name="Total Demandes",
               line=dict(color="lightseagreen")))

fig3.add_trace(
    go.Scatter(x=df_Population_Be_1[' '],
               y=df_Population_Be_1["Demandes d'emploi enregistrées des Masculins"],
               name="Demandes masculines",
               visible=False,
               line=dict(color="royalblue")))

fig3.add_trace(
    go.Scatter(x=df_Population_Be_1[' '],
               y=df_Population_Be_1["demandes d'emploi enregistrées des Feminins"],
               name="Demandes Féminines",
               line=dict(color="tomato")))

fig3.add_trace(
    go.Scatter(x=df_Population_Be_1[' '],
               y=df_Population_Be_1['Dont première demande'],
               name="PrD",
               visible=False,
               line=dict(color="darkturquoise")))

# Add Annotations and Buttons

fig3.update_layout(
    updatemenus=[
        dict(
            #active=0,
            #bgcolor='#B8F7D4',
            #borderwidth =2,
            buttons=list([
                dict(label="Total Demandes",
                     method="update",
                     args=[{"visible": [True, False, False, False]},
                           {"title": "Demandes d'emploi"
                            }]),
                dict(label="Demandes masculines",
                     method="update",
                     args=[{"visible": [True, True, False, False]},
                           {"title": "Demandes d'emploi"
                           }]),
                dict(label="Demandes Féminines",
                     method="update",
                     args=[{"visible": [True, False, True, False]},
                           {"title": "Demandes d'emploi"
                            }]),
                dict(label="PrD",
                     method="update",
                     args=[{"visible": [True,False,False, True]},
                           {"title": "Demandes d'emploi"
                            }]),
            ])
        )
    ])

# Set title


fig3.update_layout(hovermode="x",
                   template="plotly_white",
        title="Demandes d'emploi",
        font=dict(
        family=" Gravitas One, cursive",
        size=13))
        #color="MidnightBlue" 
def demande_emploi():
   return fig3


# In[6]:


df_Population_Be_2=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/bureau d'emploi/Socio économique 02_22_2020 22_12_13.csv",
                                header=1)
df_Population_Be_2.head()


max_df_Population_Be_1=max(df_Population_Be_1["Evolution des demandes d'emploi enregistrées"])
y_max_df_Population_Be_1=df_Population_Be_1[" "].loc[df_Population_Be_1["Evolution des demandes d'emploi enregistrées"] == max_df_Population_Be_1]

max_df_Population_Be_1_OE=max(df_Population_Be_2["Evolution des offres d'emploi reçus"])
y_max_df_Population_Be_1_OE=df_Population_Be_2[" "].loc[df_Population_Be_2["Evolution des offres d'emploi reçus"] == max_df_Population_Be_1_OE]

min_df_Population_Be_1=min(df_Population_Be_1["Evolution des demandes d'emploi enregistrées"])
y_min_df_Population_Be_1=df_Population_Be_1[" "].loc[df_Population_Be_1["Evolution des demandes d'emploi enregistrées"] == min_df_Population_Be_1]

min_df_Population_Be_1_OE=min(df_Population_Be_2["Evolution des offres d'emploi reçus"])
y_min_df_Population_Be_1_OE=df_Population_Be_2[" "].loc[df_Population_Be_2["Evolution des offres d'emploi reçus"] == min_df_Population_Be_1_OE]

# In[7]:
fig1_max_be = go.Figure()
fig1_max_be.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Max<br><span style='font-size:0.8em;color:lightseagreen'>Demandes enregistrées</span><br>"+str(y_max_df_Population_Be_1.values)},
    value = max_df_Population_Be_1,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_be.update_layout(paper_bgcolor = "white",
                         width=200,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=13))


# In[9]:


fig1_max_be_oe = go.Figure()
fig1_max_be_oe.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Max<br><span style='font-size:0.8em;color:royalblue'>Offres reçues</span><br>"+str(y_max_df_Population_Be_1_OE.values)},
    value = max_df_Population_Be_1_OE,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_be_oe.update_layout(paper_bgcolor = "white",
                           width=200,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=20))


# In[11]:

fig_min_be = go.Figure()
fig_min_be.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Demandes enregistrées</span><br>"+str(y_min_df_Population_Be_1.values)},
    value = min_df_Population_Be_1,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig_min_be.update_layout(paper_bgcolor = "white",
                        width=200,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=13))


fig_min_be_oe = go.Figure()
fig_min_be_oe.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:tomato'>Offres reçues</span><br>"+str(y_min_df_Population_Be_1_OE.values)},
    value = min_df_Population_Be_1_OE,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig_min_be_oe.update_layout(paper_bgcolor = "white",
                        width=200,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=13))




# In[8]:


fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=df_Population_Be_1[' '], y=df_Population_Be_1["Evolution des demandes d'emploi enregistrées"], fill='tonexty',name="Demandes enregistrées",line_color='firebrick')) # fill down to xaxis
fig4.add_trace(go.Scatter(x=df_Population_Be_1[' '], y=df_Population_Be_2["Evolution des offres d'emploi reçus"], fill='tozeroy',name="Offres reçues",line_color='darkturquoise')) # fill to trace0 y
fig4.update_layout(hovermode="x",title_text="",template="plotly_white",font=dict(
                 family=" Gravitas One, cursive",
                 size=13))
def Demandes_emploi_Vs_Offres_reçues():
   return fig4


# In[14]:


fig5 = go.Figure(data=[
    go.Bar(name="Evolution des offres d'emploi reçus", x=df_Population_Be_2[' '], y=df_Population_Be_2["Evolution des offres d'emploi reçus"],marker_color='darkturquoise'),
    go.Bar(name="Placements réalisées par Sexe", x=df_Population_Be_2[' '], y=df_Population_Be_2["Placements réalisées par Sexe"],marker_color='lightseagreen'),
    go.Bar(name="Placements réalisées  des Masculins", x=df_Population_Be_2[' '], y=df_Population_Be_2["Placements réalisées  des Masculins"],marker_color='royalblue'),
    go.Bar(name="Placements réalisées des Feminins", x=df_Population_Be_2[' '], y=df_Population_Be_2["Placements réalisées des Feminins"],marker_color='tomato'),
    go.Bar(name="Dont premier emploi", x=df_Population_Be_2[' '], y=df_Population_Be_2["Dont premier emploi"],marker_color='firebrick')
])
# Change the bar mode

fig5.update_layout(barmode='group',template="plotly_white",font=dict(
                 family=" Gravitas One, cursive",
                 size=13))
def evolution_offre_emploi():
    return fig5


# In[10]:
fig = go.Figure(data=[
    go.Bar(name="Evolution des offres d'emploi reçus", x=df_Population_Be_2[' '], y=df_Population_Be_2["Evolution des offres d'emploi reçus"],marker_color='darkturquoise'),
    go.Bar(name="Placements réalisées par Sexe", x=df_Population_Be_2[' '], y=df_Population_Be_2["Placements réalisées par Sexe"],marker_color='lightseagreen'),
    go.Bar(name="Placements réalisées  des Masculins", x=df_Population_Be_2[' '], y=df_Population_Be_2["Placements réalisées  des Masculins"],marker_color='royalblue'),
    go.Bar(name="Placements réalisées des Feminins", x=df_Population_Be_2[' '], y=df_Population_Be_2["Placements réalisées des Feminins"],marker_color='tomato'),
    go.Bar(name="Dont premier emploi", x=df_Population_Be_2[' '], y=df_Population_Be_2["Dont premier emploi"],marker_color='firebrick')
])
# Change the bar mode

fig.update_layout(barmode='stack',template="plotly_white",font=dict(
                 family=" Gravitas One, cursive",
                 size=13))
def offre_emploi():
  return fig


def indicatorsBureauEmploi():
    return(fig1_max_be,fig1_max_be_oe,fig_min_be,fig_min_be_oe)




