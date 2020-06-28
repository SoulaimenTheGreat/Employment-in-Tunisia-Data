#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



# In[2]:


df_Population_Ch_1=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/chomage/Evolution de la population active en chômage selon le sexe.csv",
                                header=1)
df_Population_Ch_1.head()


# population active en chomage
max_df_Population_C_1=max(df_Population_Ch_1["Evolution de la population active en chômage"])
y_max_df_Population_C_1=df_Population_Ch_1[" "].loc[df_Population_Ch_1["Evolution de la population active en chômage"] == max_df_Population_C_1]

max_df_Population_C1_M=max(df_Population_Ch_1["Population active en chômage Masculine"])
y_max_df_Population_C_1_M=df_Population_Ch_1[" "].loc[df_Population_Ch_1["Population active en chômage Masculine"] == max_df_Population_C1_M]

max_df_Population_C_1_F=max(df_Population_Ch_1["Population active en chômage Féminine"])
y_max_df_Population_C_1_F=df_Population_Ch_1[" "].loc[df_Population_Ch_1["Population active en chômage Féminine"] == max_df_Population_C_1_F]

min_df_Population_C_1=min(df_Population_Ch_1["Evolution de la population active en chômage"])
y_min_df_Population_C_1=df_Population_Ch_1[" "].loc[df_Population_Ch_1["Evolution de la population active en chômage"] == min_df_Population_C_1]

min_df_Population_C1_M=min(df_Population_Ch_1["Population active en chômage Masculine"])
y_min_df_Population_C_1_M=df_Population_Ch_1[" "].loc[df_Population_Ch_1["Population active en chômage Masculine"] == min_df_Population_C1_M]

min_df_Population_C_1_F=min(df_Population_Ch_1["Population active en chômage Féminine"])
y_min_df_Population_C_1_F=df_Population_Ch_1[" "].loc[df_Population_Ch_1["Population active en chômage Féminine"] == min_df_Population_C_1_F]





# In[3]:


fig2 = go.Figure()

fig2.add_trace(go.Scatter(x=df_Population_Ch_1[' '], 
                         y=df_Population_Ch_1['Evolution de la population active en chômage'] ,
                    mode='markers',
                    name='Total',
                    marker=dict(
        size=16,
        color='lightseagreen')))
fig2.add_trace(go.Scatter(x=df_Population_Ch_1[' '], 
                         y=df_Population_Ch_1['Population active en chômage Masculine'] ,
                    mode='markers',
                    name='Masculin',
                    marker=dict(
        size=16,
        color='royalblue'))) 
fig2.add_trace(go.Scatter(x=df_Population_Ch_1[' '], 
                         y=df_Population_Ch_1['Population active en chômage Féminine'] ,
                    mode='markers',
                    name='Féminin',
                    marker=dict(
        size=16,
        color='tomato')))
fig2.update_layout(title='Evolution of the unemployed working population ',
                 template='plotly_white',
                 font=dict(
                 family=" Gravitas One, cursive",
                 size=13))

def population_active_chômage():
  return fig2


# In[4]:


df_Population_Ch_3=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/chomage/Taux de chômage selon le sexe.csv",
                                header=1)
df_Population_Ch_3.head()


# In[5]:
# taux de chomage
max_df_Population_TC_1=max(df_Population_Ch_3["Emploi\Chômage\Taux de chômage\Par sexe"])
y_max_df_Population_TC_1=df_Population_Ch_3[" "].loc[df_Population_Ch_3["Emploi\Chômage\Taux de chômage\Par sexe"] == max_df_Population_TC_1]

max_df_Population_TC1_M=max(df_Population_Ch_3["Taux de chômage Masculin"])
y_max_df_Population_TC_1_M=df_Population_Ch_3[" "].loc[df_Population_Ch_3["Taux de chômage Masculin"] == max_df_Population_TC1_M]

max_df_Population_TC_1_F=max(df_Population_Ch_3["Taux de chômage Féminin"])
y_max_df_Population_TC_1_F=df_Population_Ch_3[" "].loc[df_Population_Ch_3["Taux de chômage Féminin"] == max_df_Population_TC_1_F]

min_df_Population_TC_1=min(df_Population_Ch_3["Emploi\Chômage\Taux de chômage\Par sexe"])
y_min_df_Population_TC_1=df_Population_Ch_3[" "].loc[df_Population_Ch_3["Emploi\Chômage\Taux de chômage\Par sexe"] == min_df_Population_TC_1]

min_df_Population_TC1_M=min(df_Population_Ch_3["Taux de chômage Masculin"])
y_min_df_Population_TC_1_M=df_Population_Ch_3[" "].loc[df_Population_Ch_3["Taux de chômage Masculin"] == min_df_Population_TC1_M]

min_df_Population_TC_1_F=min(df_Population_Ch_3["Taux de chômage Féminin"])
y_min_df_Population_TC_1_F=df_Population_Ch_3[" "].loc[df_Population_Ch_3["Taux de chômage Féminin"] == min_df_Population_TC_1_F]




fig_C=go.Figure(data=[go.Scatter(x=df_Population_Ch_3[' '], 
                                  y=df_Population_Ch_3["Emploi\Chômage\Taux de chômage\Par sexe"], 
                                  name='Total',
                                  mode='lines+markers',
                                  line = dict(color='lightseagreen'))
                     ])
# Edit the layout
fig_C.update_layout(title="",template='plotly_white',
                 font=dict(
                 family=" Gravitas One, cursive",
                 size=13))
fig_C.update_xaxes(showticklabels=False)
fig_C.update_yaxes(showticklabels=False)
def Taux_chômage():
  return fig_C


# In[6]:


df_Population_Ch_3_2011=df_Population_Ch_3.loc[df_Population_Ch_3[" "].str.contains("2011"),:]
df_Population_Ch_3_2012=df_Population_Ch_3.loc[df_Population_Ch_3[" "].str.contains("2012"),:]
df_Population_Ch_3_2013=df_Population_Ch_3.loc[df_Population_Ch_3[" "].str.contains("2013"),:]
df_Population_Ch_3_2014=df_Population_Ch_3.loc[df_Population_Ch_3[" "].str.contains("2014"),:]
df_Population_Ch_3_2015=df_Population_Ch_3.loc[df_Population_Ch_3[" "].str.contains("2015"),:]
df_Population_Ch_3_2016=df_Population_Ch_3.loc[df_Population_Ch_3[" "].str.contains("2016"),:]
df_Population_Ch_3_2017=df_Population_Ch_3.loc[df_Population_Ch_3[" "].str.contains("2017"),:]
df_Population_Ch_3_2018=df_Population_Ch_3.loc[df_Population_Ch_3[" "].str.contains("2018"),:]
df_Population_Ch_3_2019=df_Population_Ch_3.loc[df_Population_Ch_3[" "].str.contains("2019"),:]


# In[7]:


data=[
    go.Scatter(
              x=df_Population_Ch_3[' '], 
              y=df_Population_Ch_3["Taux de chômage Masculin"], 
              name='Homme',
              mode='lines+markers',
              line=dict(
              color='royalblue')),
    go.Scatter(
              x=df_Population_Ch_3[' '], 
              y=df_Population_Ch_3["Taux de chômage Féminin"], 
              name='Femme',
              mode='lines+markers',
              line=dict(
              color='tomato')),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_3_2011[' '], 
           y=df_Population_Ch_3_2011["Taux de chômage Masculin"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_3_2011[' '], 
           y=df_Population_Ch_3_2011["Taux de chômage Féminin"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_3_2012[' '], 
           y=df_Population_Ch_3_2012["Taux de chômage Masculin"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_3_2012[' '], 
           y=df_Population_Ch_3_2012["Taux de chômage Féminin"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_3_2013[' '], 
           y=df_Population_Ch_3_2013["Taux de chômage Masculin"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_3_2013[' '], 
           y=df_Population_Ch_3_2013["Taux de chômage Féminin"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_3_2014[' '], 
           y=df_Population_Ch_3_2014["Taux de chômage Masculin"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_3_2014[' '], 
           y=df_Population_Ch_3_2014["Taux de chômage Féminin"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_3_2015[' '], 
           y=df_Population_Ch_3_2015["Taux de chômage Masculin"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_3_2015[' '], 
           y=df_Population_Ch_3_2015["Taux de chômage Féminin"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_3_2016[' '], 
           y=df_Population_Ch_3_2016["Taux de chômage Masculin"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_3_2016[' '], 
           y=df_Population_Ch_3_2016["Taux de chômage Féminin"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_3_2017[' '], 
           y=df_Population_Ch_3_2017["Taux de chômage Masculin"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_3_2017[' '], 
           y=df_Population_Ch_3_2017["Taux de chômage Féminin"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_3_2018[' '], 
           y=df_Population_Ch_3_2018["Taux de chômage Masculin"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_3_2018[' '], 
           y=df_Population_Ch_3_2018["Taux de chômage Féminin"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_3_2019[' '], 
           y=df_Population_Ch_3_2019["Taux de chômage Masculin"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_3_2019[' '], 
           y=df_Population_Ch_3_2019["Taux de chômage Féminin"],
          marker_color='tomato'),
    
]


# In[8]:


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
layout=go.Layout(updatemenus=list([dict(buttons= list_updatemenus)]),title_text="",template='plotly_white',font=dict(
                 family=" Gravitas One, cursive",
                 size=13))

#defining figure and plotting
fig1 = go.Figure(data,layout)
def Taux_chômage_sexe():
  return fig1


# In[9]:


df_Population_Ch_2_1=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/chomage/Taux de chômage des diplômés de l’enseignement supérieur selon le genre.csv",
                                header=1)
df_Population_Ch_2_1.head()



# population active en chomage
max_df_Population_CES_1=max(df_Population_Ch_2_1["Taux de chômage des diplômés de l’enseignement supérieur"])
y_max_df_Population_CES_1=df_Population_Ch_2_1[" "].loc[df_Population_Ch_2_1["Taux de chômage des diplômés de l’enseignement supérieur"] == max_df_Population_CES_1]

max_df_Population_C1ES_M=max(df_Population_Ch_2_1["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"])
y_max_df_Population_CES_1_M=df_Population_Ch_2_1[" "].loc[df_Population_Ch_2_1["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"] == max_df_Population_C1ES_M]

max_df_Population_CES_1_F=max(df_Population_Ch_2_1["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"])
y_max_df_Population_CES_1_F=df_Population_Ch_2_1[" "].loc[df_Population_Ch_2_1["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"] == max_df_Population_CES_1_F]

min_df_Population_CES_1=min(df_Population_Ch_2_1["Taux de chômage des diplômés de l’enseignement supérieur"])
y_min_df_Population_CES_1=df_Population_Ch_2_1[" "].loc[df_Population_Ch_2_1["Taux de chômage des diplômés de l’enseignement supérieur"] == min_df_Population_CES_1]

min_df_Population_C1ES_M=min(df_Population_Ch_2_1["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"])
y_min_df_Population_CES_1_M=df_Population_Ch_2_1[" "].loc[df_Population_Ch_2_1["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"] == min_df_Population_C1ES_M]

min_df_Population_CES_1_F=min(df_Population_Ch_2_1["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"])
y_min_df_Population_CES_1_F=df_Population_Ch_2_1[" "].loc[df_Population_Ch_2_1["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"] == min_df_Population_CES_1_F]

# In[10]:


df_Population_Ch_2_1_2011=df_Population_Ch_2_1.loc[df_Population_Ch_2_1[" "].str.contains("2011"),:]
df_Population_Ch_2_1_2012=df_Population_Ch_2_1.loc[df_Population_Ch_2_1[" "].str.contains("2012"),:]
df_Population_Ch_2_1_2013=df_Population_Ch_2_1.loc[df_Population_Ch_2_1[" "].str.contains("2013"),:]
df_Population_Ch_2_1_2014=df_Population_Ch_2_1.loc[df_Population_Ch_2_1[" "].str.contains("2014"),:]
df_Population_Ch_2_1_2015=df_Population_Ch_2_1.loc[df_Population_Ch_2_1[" "].str.contains("2015"),:]
df_Population_Ch_2_1_2016=df_Population_Ch_2_1.loc[df_Population_Ch_2_1[" "].str.contains("2016"),:]
df_Population_Ch_2_1_2017=df_Population_Ch_2_1.loc[df_Population_Ch_2_1[" "].str.contains("2017"),:]
df_Population_Ch_2_1_2018=df_Population_Ch_2_1.loc[df_Population_Ch_2_1[" "].str.contains("2018"),:]
df_Population_Ch_2_1_2019=df_Population_Ch_2_1.loc[df_Population_Ch_2_1[" "].str.contains("2019"),:]


# In[11]:


data1=[
    go.Scatter(
              x=df_Population_Ch_2_1[" "], 
              y=df_Population_Ch_2_1["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"], 
              name='Homme',
              mode='lines+markers',
              line=dict(
              color='royalblue')),
    go.Scatter(
              x=df_Population_Ch_2_1[" "], 
              y=df_Population_Ch_2_1["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"], 
              name='Femme',
              mode='lines+markers',
              line=dict(
              color='tomato')),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_2_1_2011[" "], 
           y=df_Population_Ch_2_1_2011["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_2_1_2011[" "], 
           y=df_Population_Ch_2_1_2011["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_2_1_2012[" "], 
           y=df_Population_Ch_2_1_2012["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_2_1_2012[" "], 
           y=df_Population_Ch_2_1_2012["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_2_1_2013[" "], 
           y=df_Population_Ch_2_1_2013["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_2_1_2013[" "], 
           y=df_Population_Ch_2_1_2013["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_2_1_2014[" "], 
           y=df_Population_Ch_2_1_2014["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_2_1_2014[" "], 
           y=df_Population_Ch_2_1_2014["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_2_1_2015[" "], 
           y=df_Population_Ch_2_1_2015["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_2_1_2015[" "], 
           y=df_Population_Ch_2_1_2015["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_2_1_2016[" "], 
           y=df_Population_Ch_2_1_2016["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_2_1_2016[" "], 
           y=df_Population_Ch_2_1_2016["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_2_1_2017[" "], 
           y=df_Population_Ch_2_1_2017["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_2_1_2017[" "], 
           y=df_Population_Ch_2_1_2017["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_2_1_2018[" "], 
           y=df_Population_Ch_2_1_2018["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_2_1_2018[" "], 
           y=df_Population_Ch_2_1_2018["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"],
          marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_Ch_2_1_2019[" "], 
           y=df_Population_Ch_2_1_2019["Taux de chômage des Masculins des diplômés de l’enseignement supérieur"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_Ch_2_1_2019[" "], 
           y=df_Population_Ch_2_1_2019["Taux de chômage des Féminins des diplômés de l’enseignement supérieur"],
          marker_color='tomato'),
    
]


# In[12]:


# Add dropdown
list_updatemenus1=[
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
layout_bar1=go.Layout(updatemenus=list([dict(buttons= list_updatemenus1)]),title_text="",yaxis_zeroline=False, xaxis_zeroline=False,template='plotly_white',font=dict(
                 family=" Gravitas One, cursive",
                 size=13))

#defining figure and plotting
fig = go.Figure(data1,layout_bar1)
def Taux_chômage_diplome(): 
    return fig


# In[2]:
#***********************Map Tunisian*****************************

df_region=pd.read_excel("~/data_viz/Project_Employement/data/raw_data/region.xlsx")
df_region.head()


max_df_Population_TCR_1=max(df_region["taux de chomâge"])
y_max_df_Population_TCR_1=df_region["gouvernorat"].loc[df_region["taux de chomâge"] == max_df_Population_TCR_1]

min_df_Population_TCR_1=min(df_region["taux de chomâge"])
y_min_df_Population_TCR_1=df_region["gouvernorat"].loc[df_region["taux de chomâge"] == min_df_Population_TCR_1]





# In[6]:


px.set_mapbox_access_token("pk.eyJ1Ijoic291bGFpbWVudGhlZ3JlYXQiLCJhIjoiY2s4dTZrenloMDFvODNlcDg2NGMzcjVtZCJ9.XvW1_RTHyRjR3TkA9-vGsQ")
figtun = px.scatter_mapbox(df_region,
                           lon="longitude",lat="latitude",
                           size="taux de chomâge",
                           hover_name="gouvernorat",
                           color="taux de chomâge",
                           size_max=15,
                           zoom=4.8)




fig1_max_tcr = go.Figure()
fig1_max_tcr.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.8em;color:lightseagreen'> Max Taux de chômage </span><br><span style='font-size:0.8em;color:lightseared'>"+str(y_max_df_Population_TCR_1.values)+"</span><br><span style='font-size:0.8em;color:lightseared'>"+str(max_df_Population_TCR_1)+"</span>"}))

fig1_max_tcr.update_layout(paper_bgcolor = "white",
                         width=300,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=20))



fig1_min_tcr = go.Figure()
fig1_min_tcr.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.8em;color:lightseagreen'> Min Taux de chômage </span><br><span style='font-size:0.8em;color:lightseared'>"+str(y_min_df_Population_TCR_1.values)+"</span><br><span style='font-size:0.8em;color:lightseared'>"+str(min_df_Population_TCR_1)+"</span>"}))

fig1_min_tcr.update_layout(paper_bgcolor = "white",
                           width=300,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=7))
def chomage_map():
   return (figtun,fig1_max_tcr,fig1_min_tcr)
#************************Population Active en Chomage********************
fig1_max_t_c = go.Figure()
fig1_max_t_c.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'> Max Total</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_max_df_Population_C_1.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(max_df_Population_C_1)+"</span>"}))

fig1_max_t_c.update_layout(paper_bgcolor = "white",
                         width=100,
                         height=150,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=20))


# In[9]:


fig1_max_t_m_c = go.Figure()
fig1_max_t_m_c.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'> Max Homme</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_max_df_Population_C_1_M.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(max_df_Population_C1_M)+"</span>"}))

fig1_max_t_m_c.update_layout(paper_bgcolor = "white",
                           width=100,
                         height=150,font=dict(
                 family=" Gravitas One, cursive",
                 size=7))




# In[10]:


fig1_max_f_c = go.Figure()
fig1_max_f_c.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'>Max Femme</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_max_df_Population_C_1.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(max_df_Population_C_1_F)+"</span>"}))
fig1_max_f_c.update_layout(paper_bgcolor = "white",
                         width=100,
                         height=150,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))


fig1_min_t_c = go.Figure()
fig1_min_t_c.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'> Min Total</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_min_df_Population_C_1.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(min_df_Population_C_1)+"</span>"}))


fig1_min_t_c.update_layout(paper_bgcolor = "white",
                         width=100,
                         height=150,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))


# In[9]:


fig1_min_t_m_c = go.Figure()
fig1_min_t_m_c.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'> Min Homme</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_min_df_Population_C_1_M.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(min_df_Population_C1_M)+"</span>"}))

fig1_min_t_m_c.update_layout(paper_bgcolor = "white",
                           width=100,
                         height=150,font=dict(
                 family=" Gravitas One, cursive",
                 size=7))




# In[10]:


fig1_min_f_c = go.Figure()
fig1_min_f_c.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'> Min Femme</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_min_df_Population_C_1_F.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(min_df_Population_C_1_F)+"</span>"}))


fig1_min_f_c.update_layout(paper_bgcolor = "white",
                         width=100,
                         height=150,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))

#************************Taux de Chomage********************



fig1_max_t_tc = go.Figure()
fig1_max_t_tc.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Max<br><span style='font-size:0.8em;color:lightseagreen'>Total</span><br>"+str(y_max_df_Population_TC_1.values)},
    value = max_df_Population_TC_1,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_t_tc.update_layout(paper_bgcolor = "white",
                         width=300,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=20))


# In[9]:


fig1_max_t_m_tc = go.Figure()
fig1_max_t_m_tc.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Max<br><span style='font-size:0.8em;color:lightseagreen'>Homme</span><br>"+str(y_max_df_Population_TC_1_M.values)},
    value = max_df_Population_TC1_M,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_t_m_tc.update_layout(paper_bgcolor = "white",
                           width=200,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=7))




# In[10]:


fig1_max_f_tc = go.Figure()
fig1_max_f_tc.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Max<br><span style='font-size:0.8em;color:lightseagreen'>Femme</span><br>"+str(y_max_df_Population_TC_1.values)},
    value = max_df_Population_TC_1_F,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_f_tc.update_layout(paper_bgcolor = "white",
                         width=200,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))


fig1_min_t_tc = go.Figure()
fig1_min_t_tc.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Total</span><br>"+str(y_min_df_Population_TC_1.values)},
    value = min_df_Population_TC_1,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))
   

fig1_min_t_tc.update_layout(paper_bgcolor = "white",
                         width=300,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))


# In[9]:


fig1_min_t_m_tc = go.Figure()
fig1_min_t_m_tc.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Homme</span><br>"+str(y_min_df_Population_TC_1_M.values)},
    value = min_df_Population_TC1_M,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_min_t_m_tc.update_layout(paper_bgcolor = "white",
                           width=200,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=7))




# In[10]:


fig1_min_f_tc = go.Figure()
fig1_min_f_tc.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Femme</span><br>"+str(y_min_df_Population_TC_1_F.values)},
    value = min_df_Population_TC_1_F,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))


fig1_min_f_tc.update_layout(paper_bgcolor = "white",
                         width=200,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))
#************************Population Active en Chomage********************
fig1_max_t_ces = go.Figure()
fig1_max_t_ces.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'> Max Total</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_max_df_Population_CES_1.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(max_df_Population_CES_1)+"</span>"}))

fig1_max_t_ces.update_layout(paper_bgcolor = "white",
                         width=100,
                         height=150,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=20))


# In[9]:


fig1_max_t_m_ces = go.Figure()
fig1_max_t_m_ces.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'> Max Homme</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_max_df_Population_CES_1_M.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(max_df_Population_C1ES_M)+"</span>"}))

fig1_max_t_m_ces.update_layout(paper_bgcolor = "white",
                           width=100,
                         height=150,font=dict(
                 family=" Gravitas One, cursive",
                 size=7))




# In[10]:


fig1_max_f_ces = go.Figure()
fig1_max_f_ces.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'>Max Femme</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_max_df_Population_CES_1.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(max_df_Population_CES_1_F)+"</span>"}))
fig1_max_f_ces.update_layout(paper_bgcolor = "white",
                         width=100,
                         height=150,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))


fig1_min_t_ces = go.Figure()
fig1_min_t_ces.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'> Min Total</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_min_df_Population_CES_1.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(min_df_Population_CES_1)+"</span>"}))


fig1_min_t_ces.update_layout(paper_bgcolor = "white",
                         width=100,
                         height=150,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))


# In[9]:


fig1_min_t_m_ces = go.Figure()
fig1_min_t_m_ces.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'> Min Homme</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_min_df_Population_CES_1_M.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(min_df_Population_C1ES_M)+"</span>"}))

fig1_min_t_m_ces.update_layout(paper_bgcolor = "white",
                           width=100,
                         height=150,font=dict(
                 family=" Gravitas One, cursive",
                 size=7))




# In[10]:


fig1_min_f_ces = go.Figure()
fig1_min_f_ces.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "<br><span style='font-size:0.6em;color:lightseagreen'> Min Femme</span><br><span style='font-size:0.6em;color:lightseagreen'>"+str(y_min_df_Population_CES_1_F.values)+"</span><br><span style='font-size:0.7em;color:lightseared'>"+str(min_df_Population_CES_1_F)+"</span>"}))


fig1_min_f_ces.update_layout(paper_bgcolor = "white",
                         width=100,
                         height=150,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=7))

def indicatorsChomage():
    return(fig1_max_t_c,fig1_max_t_m_c,fig1_max_f_c,fig1_min_t_c,fig1_min_t_m_c,fig1_min_f_c,
           fig1_max_t_tc,fig1_max_t_m_tc,fig1_max_f_tc,fig1_min_t_tc,fig1_min_t_m_tc,fig1_min_f_tc,
           fig1_max_t_ces,fig1_max_t_m_ces,fig1_max_f_ces,fig1_min_t_ces,fig1_min_t_m_ces,fig1_min_f_ces)


