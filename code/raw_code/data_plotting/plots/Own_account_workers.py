#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import plotly.graph_objects as go


# In[2]:


df_Own_Account_workers=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/Own-account workers/Own-account Workers.csv",index_col=0)
df_Own_Account_workers.head()


# In[3]:

def Travailleurs_independants():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_Own_Account_workers['date'], y=df_Own_Account_workers["value"], name='Total',
                             line = dict(color='lightseagreen')))
    
    fig.update_layout(title="Travailleurs indépendants entre 1991 et 2019",template="plotly_white",font=dict(
                     family=" Gravitas One, cursive",
                     size=13))
    
    return fig


# In[4]:


df_Own_Account_Female=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/Own-account workers/Own-account Workers, Female.csv",index_col=0)
df_Own_Account_Female.head()


# In[5]:


df_Own_Account_male=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/Own-account workers/Own-account Workers, Male.csv",index_col=0)
df_Own_Account_male.head()


# In[7]:

def Travailleurs_independants_sex():
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=df_Own_Account_Female["date"],
                    y=df_Own_Account_Female['value'],
                    name='Femme',
                    marker_color='tomato'
                    ))
    fig1.add_trace(go.Bar(x=df_Own_Account_male["date"],
                    y=df_Own_Account_male['value'],
                    name='Homme',
                    marker_color='royalblue'
                    ))
    
    fig1.update_layout(
        title='Travailleurs indépendants des hommes Vs les femmes entre 1991 et 2019',template="plotly_white",font=dict(
                     family=" Gravitas One, cursive",
                     size=13))

    return fig1



