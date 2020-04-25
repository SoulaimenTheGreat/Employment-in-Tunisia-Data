#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



# In[2]:


df_Population_Ch_1=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/chomage/Evolution de la population active en chômage selon le sexe.csv",
                                header=1)
df_Population_Ch_1.head()


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
fig2.update_layout(title='Evolution de la population active en chômage ',
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



fig_C=go.Figure(data=[go.Scatter(x=df_Population_Ch_3[' '], 
                                  y=df_Population_Ch_3["Emploi\Chômage\Taux de chômage\Par sexe"], 
                                  name='Total',
                                  mode='lines+markers',
                                  line = dict(color='lightseagreen'))
                     ])
# Edit the layout
fig_C.update_layout(title="Taux de chômage selon le sexe",template='plotly_white',
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
layout=go.Layout(updatemenus=list([dict(buttons= list_updatemenus)]),title_text="Taux de chômage selon le sexe",template='plotly_white',font=dict(
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
layout_bar1=go.Layout(updatemenus=list([dict(buttons= list_updatemenus1)]),title_text="Taux de chômage des diplômés de l’enseignement supérieur",yaxis_zeroline=False, xaxis_zeroline=False,template='plotly_white',font=dict(
                 family=" Gravitas One, cursive",
                 size=13))

#defining figure and plotting
fig = go.Figure(data1,layout_bar1)
def Taux_chômage_diplome(): 
    return fig


# In[2]:


df_region=pd.read_excel("~/data_viz/Project_Employement/data/raw_data/region.xlsx")
df_region.head()


# In[6]:


px.set_mapbox_access_token("pk.eyJ1Ijoic291bGFpbWVudGhlZ3JlYXQiLCJhIjoiY2s4dTZrenloMDFvODNlcDg2NGMzcjVtZCJ9.XvW1_RTHyRjR3TkA9-vGsQ")
figtun = px.scatter_mapbox(df_region,
                           lon="longitude",lat="latitude",
                           size="taux de chomâge",
                           hover_name="gouvernorat",
                           color="taux de chomâge",
                           size_max=15,
                           zoom=4.8)
def chomage_map():
   return figtun






