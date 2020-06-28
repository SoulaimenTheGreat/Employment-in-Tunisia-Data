import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
from plotly.subplots import make_subplots


# In[2]:
df_Population_O_1=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/Population occupée/Evolution de la population en âge d'activité (15 ans et plus) selon le sexe.csv",
                                header=1)
df_Population_O_1.head()


max_df_Population_O_1=max(df_Population_O_1["Evolution de la population en âge d'activité (15 ans et plus)"])
y_max_df_Population_O_1=df_Population_O_1[" "].loc[df_Population_O_1["Evolution de la population en âge d'activité (15 ans et plus)"] == max_df_Population_O_1]

max_df_Population_O_1_M=max(df_Population_O_1["Evolution de la population Masculine (15 ans et plus)"])
y_max_df_Population_O_1_M=df_Population_O_1[" "].loc[df_Population_O_1["Evolution de la population Masculine (15 ans et plus)"] == max_df_Population_O_1_M]

max_df_Population_O_1_F=max(df_Population_O_1["Evolution de la population Féminine (15 ans et plus)"])
y_max_df_Population_O_1_F=df_Population_O_1[" "].loc[df_Population_O_1["Evolution de la population Féminine (15 ans et plus)"] == max_df_Population_O_1_F]

min_df_Population_O_1=min(df_Population_O_1["Evolution de la population en âge d'activité (15 ans et plus)"])
y_min_df_Population_O_1=df_Population_O_1[" "].loc[df_Population_O_1["Evolution de la population en âge d'activité (15 ans et plus)"] == min_df_Population_O_1]

min_df_Population_O_1_M=min(df_Population_O_1["Evolution de la population Masculine (15 ans et plus)"])
y_min_df_Population_O_1_M=df_Population_O_1[" "].loc[df_Population_O_1["Evolution de la population Masculine (15 ans et plus)"] == min_df_Population_O_1_M]

min_df_Population_O_1_F=min(df_Population_O_1["Evolution de la population Féminine (15 ans et plus)"])
y_min_df_Population_O_1_F=df_Population_O_1[" "].loc[df_Population_O_1["Evolution de la population Féminine (15 ans et plus)"] == min_df_Population_O_1_F]

# In[14]:
def Evolution_population_âge_activité():    
    fig_E_P_A_15=go.Figure(data=[go.Scatter(x=df_Population_O_1[' '], 
                                      y=df_Population_O_1["Evolution de la population en âge d'activité (15 ans et plus)"], 
                                      name='Total',
                                      mode='lines+markers',
                                      line = dict(color='lightseagreen'))
        
    ])
    # Edit the layout
    fig_E_P_A_15.update_layout(title="",template='plotly_white',font=dict(
                     family=" Gravitas One, cursive",
                     size=13))
    fig_E_P_A_15.update_xaxes(showticklabels=False)
    fig_E_P_A_15.update_yaxes(showticklabels=False)
    return fig_E_P_A_15


# In[4]:


df_Population_O_1_2011=df_Population_O_1.loc[df_Population_O_1[" "].str.contains("2011"),:]
df_Population_O_1_2012=df_Population_O_1.loc[df_Population_O_1[" "].str.contains("2012"),:]
df_Population_O_1_2013=df_Population_O_1.loc[df_Population_O_1[" "].str.contains("2013"),:]
df_Population_O_1_2014=df_Population_O_1.loc[df_Population_O_1[" "].str.contains("2014"),:]
df_Population_O_1_2015=df_Population_O_1.loc[df_Population_O_1[" "].str.contains("2015"),:]
df_Population_O_1_2016=df_Population_O_1.loc[df_Population_O_1[" "].str.contains("2016"),:]
df_Population_O_1_2017=df_Population_O_1.loc[df_Population_O_1[" "].str.contains("2017"),:]
df_Population_O_1_2018=df_Population_O_1.loc[df_Population_O_1[" "].str.contains("2018"),:]
df_Population_O_1_2019=df_Population_O_1.loc[df_Population_O_1[" "].str.contains("2019"),:]


# In[5]:


data_bar=[
    go.Scatter(
              x=df_Population_O_1[' '], 
              y=df_Population_O_1["Evolution de la population Masculine (15 ans et plus)"], 
              name='Homme',
              mode='lines+markers',
              line=dict(
              color='royalblue')),
    go.Scatter(
              x=df_Population_O_1[' '], 
              y=df_Population_O_1["Evolution de la population Féminine (15 ans et plus)"], 
              name='Femme',
              mode='lines+markers',
              line=dict(
              color='tomato')),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_O_1_2011[' '], 
           y=df_Population_O_1_2011["Evolution de la population Masculine (15 ans et plus)"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_O_1_2011[' '], 
           y=df_Population_O_1_2011["Evolution de la population Féminine (15 ans et plus)"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_O_1_2012[' '], 
           y=df_Population_O_1_2012["Evolution de la population Masculine (15 ans et plus)"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_O_1_2012[' '], 
           y=df_Population_O_1_2012["Evolution de la population Féminine (15 ans et plus)"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_O_1_2013[' '], 
           y=df_Population_O_1_2013["Evolution de la population Masculine (15 ans et plus)"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_O_1_2013[' '], 
           y=df_Population_O_1_2013["Evolution de la population Féminine (15 ans et plus)"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_O_1_2014[' '], 
           y=df_Population_O_1_2014["Evolution de la population Masculine (15 ans et plus)"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_O_1_2014[' '], 
           y=df_Population_O_1_2014["Evolution de la population Féminine (15 ans et plus)"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_O_1_2015[' '], 
           y=df_Population_O_1_2015["Evolution de la population Masculine (15 ans et plus)"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_O_1_2015[' '], 
           y=df_Population_O_1_2015["Evolution de la population Féminine (15 ans et plus)"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_O_1_2016[' '], 
           y=df_Population_O_1_2016["Evolution de la population Masculine (15 ans et plus)"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_O_1_2016[' '], 
           y=df_Population_O_1_2016["Evolution de la population Féminine (15 ans et plus)"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_O_1_2017[' '], 
           y=df_Population_O_1_2017["Evolution de la population Masculine (15 ans et plus)"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_O_1_2017[' '], 
           y=df_Population_O_1_2017["Evolution de la population Féminine (15 ans et plus)"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_O_1_2018[' '], 
           y=df_Population_O_1_2018["Evolution de la population Masculine (15 ans et plus)"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_O_1_2018[' '], 
           y=df_Population_O_1_2018["Evolution de la population Féminine (15 ans et plus)"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_O_1_2019[' '], 
           y=df_Population_O_1_2019["Evolution de la population Masculine (15 ans et plus)"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_O_1_2019[' '], 
           y=df_Population_O_1_2019["Evolution de la population Féminine (15 ans et plus)"],
          marker_color='tomato'),
    
]


# In[15]:


# Add dropdown
list_updatemenus=[
        {'args':[{"visible":[True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}],
         'label':"Tout",
         'method':"update"},
    
        {'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True]}],
         'label':"2019",
         'method':"update"},

         {'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False]}],
         'label':"2018",
         'method':"update"},

         {'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False]}],
         'label':"2017",
         'method':"update"
         },

         {'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False]}],
         'label':"2016",
         'method':"update"
         },

         {'args':[{"visible":[False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False]}],
         'label':"2015",
         'method':"update" 
         },

         {'args':[{"visible":[False,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False]}],
         'label':"2014",
         'method':"update"
         },

         {'args':[{"visible":[False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False]}],
         'label':"2013",
         'method':"update"
         },

         {'args':[{"visible":[False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}],
         'label':"2012",
         'method':"update"
         },

          {'args':[{"visible":[False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}],
           'label':"2011",
           'method':"update"},]

#defining layout   
layout_bar=go.Layout(updatemenus=list([dict(buttons= list_updatemenus)]),
                     title_text="",
                     template='plotly_white',
                     font=dict(
                    family=" Gravitas One, cursive",
                    size=13))

#defining figure and plotting
fig_bar_15 = go.Figure(data_bar,layout_bar)
def Evolution_population_âge_activité_sex():
    return fig_bar_15

# In[7]:


df_Population_O_2=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/Population occupée/Evolution des créations d'emploi selon le sexe.csv",
                                header=1)
df_Population_O_2.head()



max_df_Population_OCE_1=max(df_Population_O_2["Evolution des créations d'emploi"])
y_max_df_Population_OCE_1=df_Population_O_2[" "].loc[df_Population_O_2["Evolution des créations d'emploi"] == max_df_Population_OCE_1]

min_df_Population_OCE_1=min(df_Population_O_2["Evolution des créations d'emploi"])
y_min_df_Population_OCE_1=df_Population_O_2[" "].loc[df_Population_O_2["Evolution des créations d'emploi"] == min_df_Population_OCE_1]



fig1_max_t_oce = go.Figure()
fig1_max_t_oce.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Total</span><br>"+str(y_max_df_Population_OCE_1.values)},
    value = max_df_Population_OCE_1,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_t_oce.update_layout(paper_bgcolor = "white",
                         width=300,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=20))



fig1_min_t_oce = go.Figure()
fig1_min_t_oce.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Total</span><br>"+str(y_min_df_Population_OCE_1.values)},
    value = min_df_Population_OCE_1,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_min_t_oce.update_layout(paper_bgcolor = "white",
                         width=300,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))

# In[8]:


def Evolution_créations_emploi():
    fig=go.Figure(data=[go.Scatter(
        x=df_Population_O_2[' '],
        y=df_Population_O_2["Evolution des créations d'emploi"],
        mode='markers',
        marker=dict(
            showscale=True,
            color=df_Population_O_2["Evolution des créations d'emploi"],
             colorscale=['darkturquoise','lightseagreen','royalblue','tomato'],
            size=abs(df_Population_O_2["Evolution des créations d'emploi"],
                    )
            )
    )])
    fig.update_layout(title="",template='plotly_white',font=dict(
                     family=" Gravitas One, cursive",
                     size=13))
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    return fig


# In[2]:


df_Population_Secteur=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/Population occupée/Répartition de la population active occupée selon le secteur d'activité.csv",)
df_Population_Secteur_2019=df_Population_Secteur[[" ","IV trimestre 2019"]]
df_Population_Secteur_2018=df_Population_Secteur[[" ","IV trimestre 2018"]]
df_Population_Secteur_2017=df_Population_Secteur[[" ","IV trimestre 2017"]]
df_Population_Secteur_2016=df_Population_Secteur[[" ","IV trimestre 2016"]]
df_Population_Secteur_2015=df_Population_Secteur[[" ","IV trimestre 2015"]]
df_Population_Secteur_2014=df_Population_Secteur[[" ","IV trimestre 2014"]]
df_Population_Secteur_2013=df_Population_Secteur[[" ","IV trimestre 2013"]]
df_Population_Secteur_2012=df_Population_Secteur[[" ","IV trimestre 2012"]]
df_Population_Secteur_2011=df_Population_Secteur[[" ","IV trimestre 2011"]]
df_Population_Secteur.head()



#max_df_Population_OS_1=max(df_Population_Secteur["Evolution de la population en âge d'activité (15 ans et plus)"])
#y_max_df_Population_OS_1=df_Population_Secteur[" "].loc[df_Population_Secteur["Evolution de la population en âge d'activité (15 ans et plus)"] == max_df_Population_OS_1]

#min_df_Population_OS_1=min(df_Population_Secteur["Evolution de la population en âge d'activité (15 ans et plus)"])
#y_min_df_Population_OS_1=df_Population_Secteur[" "].loc[df_Population_Secteur["Evolution de la population en âge d'activité (15 ans et plus)"] == min_df_Population_OS_1]



# In[3]:


#defining data
data=[go.Pie(values=df_Population_Secteur_2019["IV trimestre 2019"],labels=df_Population_Secteur_2019[" "]),
      go.Pie(values=df_Population_Secteur_2018["IV trimestre 2018"],labels=df_Population_Secteur_2018[" "],visible=False),
      go.Pie(values=df_Population_Secteur_2017["IV trimestre 2017"],labels=df_Population_Secteur_2017[" "],visible=False),
      go.Pie(values=df_Population_Secteur_2016["IV trimestre 2016"],labels=df_Population_Secteur_2016[" "],visible=False),
      go.Pie(values=df_Population_Secteur_2015["IV trimestre 2015"],labels=df_Population_Secteur_2015[" "],visible=False),
      go.Pie(values=df_Population_Secteur_2014["IV trimestre 2014"],labels=df_Population_Secteur_2014[" "],visible=False),
      go.Pie(values=df_Population_Secteur_2013["IV trimestre 2013"],labels=df_Population_Secteur_2013[" "],visible=False),
      go.Pie(values=df_Population_Secteur_2012["IV trimestre 2012"],labels=df_Population_Secteur_2012[" "],visible=False),
      go.Pie(values=df_Population_Secteur_2011["IV trimestre 2011"],labels=df_Population_Secteur_2011[" "],visible=False)]


# In[4]:


list_updatemenus=[
        {'args':[{"visible":[True,False,False,False,False,False,False,False,False,]}],
         'label':"2019",
         'method':"update"},

         {'args':[{"visible":[False,True,False,False,False,False,False,False,False,]}],
         'label':"2018",
         'method':"update"},

         {'args':[{"visible":[False,False,True,False,False,False,False,False,False,]}],
         'label':"2017",
         'method':"update"
         },

         {'args':[{"visible":[False,False,False,True,False,False,False,False,False,]}],
         'label':"2016",
         'method':"update"
         },

         {'args':[{"visible":[False,False,False,False,True,False,False,False,False,]}],
         'label':"2015",
         'method':"update" 
         },

         {'args':[{"visible":[False,False,False,False,False,True,False,False,False,]}],
         'label':"2014",
         'method':"update"
         },

         {'args':[{"visible":[False,False,False,False,False,False,True,False,False,]}],
         'label':"2013",
         'method':"update"
         },

         {'args':[{"visible":[False,False,False,False,False,False,False,True,False,]}],
         'label':"2012",
         'method':"update"
         },

          {'args':[{"visible":[False,False,False,False,False,False,False,False,True]}],
           'label':"2011",
           'method':"update"},]
                
                
#defining layout   
layout=go.Layout(updatemenus=list([dict(buttons= list_updatemenus)]),title_text="",template="plotly_white",font=dict(
                 family=" Gravitas One, cursive",
                 size=13))
#defining figure and plotting
fig_pie_ser = go.Figure(data,layout)
def secteur_activité():
  return fig_pie_ser


fig1_max_t = go.Figure()
fig1_max_t.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Total</span><br>"+str(y_max_df_Population_O_1.values)},
    value = max_df_Population_O_1,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_t.update_layout(paper_bgcolor = "white",
                         width=300,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=20))


# In[9]:


fig1_max_t_m = go.Figure()
fig1_max_t_m.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Homme</span><br>"+str(y_max_df_Population_O_1_M.values)},
    value = max_df_Population_O_1_M,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_t_m.update_layout(paper_bgcolor = "white",
                           width=200,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=7))




# In[10]:


fig1_max_f = go.Figure()
fig1_max_f.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Femme</span><br>"+str(y_max_df_Population_O_1.values)},
    value = max_df_Population_O_1_F,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))
fig1_max_f.update_layout(paper_bgcolor = "white",
                         width=200,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))


fig1_min_t = go.Figure()
fig1_min_t.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Total</span><br>"+str(y_min_df_Population_O_1.values)},
    value = min_df_Population_O_1,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_min_t.update_layout(paper_bgcolor = "white",
                         width=300,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))


# In[9]:


fig1_min_t_m = go.Figure()
fig1_min_t_m.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Homme</span><br>"+str(y_min_df_Population_O_1_M.values)},
    value = min_df_Population_O_1_M,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_min_t_m.update_layout(paper_bgcolor = "white",
                           width=200,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=7))




# In[10]:


fig1_min_f = go.Figure()
fig1_min_f.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'> Femme</span><br>"+str(y_min_df_Population_O_1_F.values)},
    value = min_df_Population_O_1_F,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))
 

fig1_min_f.update_layout(paper_bgcolor = "white",
                         width=200,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))

def indicatorsOccupée():
    return(fig1_max_t,fig1_max_t_m,fig1_max_f,fig1_min_t,fig1_min_t_m,fig1_min_f,fig1_max_t_oce,fig1_min_t_oce)



