#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import plotly.graph_objects as go


# In[2]:


df_Own_Account_workers=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/Own-account workers/Own-account Workers.csv",index_col=0)
df_Own_Account_workers.head()




max_df_Population_A_1=max(df_Own_Account_workers["value"])
y_max_df_Population_A_1=df_Own_Account_workers["date"].loc[df_Own_Account_workers["value"] == max_df_Population_A_1]

min_df_Population_A_1=min(df_Own_Account_workers["value"])
y_min_df_Population_A_1=df_Own_Account_workers["date"].loc[df_Own_Account_workers["value"] == min_df_Population_A_1]


# In[3]:

def Travailleurs_independants():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_Own_Account_workers['date'], y=df_Own_Account_workers["value"], name='Total',
                             line = dict(color='lightseagreen')))
    
    fig.update_layout(title="",template="plotly_white",font=dict(
                     family=" Gravitas One, cursive",
                     size=13))
    
    return fig


# In[4]:


df_Own_Account_Female=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/Own-account workers/Own-account Workers, Female.csv",index_col=0)
df_Own_Account_Female.head()


max_df_Population_A_1_F=max(df_Own_Account_Female["value"])
y_max_df_Population_A_1_F=df_Own_Account_Female["date"].loc[df_Own_Account_Female["value"] == max_df_Population_A_1_F]


min_df_Population_A_1_F=min(df_Own_Account_Female["value"])
y_min_df_Population_A_1_F=df_Own_Account_Female["date"].loc[df_Own_Account_Female["value"] == min_df_Population_A_1_F]

# In[5]:


df_Own_Account_male=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/Own-account workers/Own-account Workers, Male.csv",index_col=0)
df_Own_Account_male.head()


max_df_Population_A_1_M=max(df_Own_Account_male["value"])
y_max_df_Population_A_1_M=df_Own_Account_male["date"].loc[df_Own_Account_male["value"] == max_df_Population_A_1_M]


min_df_Population_A_1_M=min(df_Own_Account_male["value"])
y_min_df_Population_A_1_M=df_Own_Account_male["date"].loc[df_Own_Account_male["value"] == min_df_Population_A_1_M]


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
        title='',template="plotly_white",font=dict(
                     family=" Gravitas One, cursive",
                     size=13))

    return fig1


fig1_max_t = go.Figure()
fig1_max_t.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Max<br><span style='font-size:0.8em;color:lightseagreen'>Total</span><br>"+str(y_max_df_Population_A_1.values)},
    value = max_df_Population_A_1,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_t.update_layout(paper_bgcolor = "white",
                         width=300,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=13))


# In[9]:


fig1_max_t_m = go.Figure()
fig1_max_t_m.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Max<br><span style='font-size:0.8em;color:royalblue'>Homme</span><br>"+str(y_max_df_Population_A_1_M.values)},
    value = max_df_Population_A_1_M,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_t_m.update_layout(paper_bgcolor = "white",
                           width=200,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=20))




# In[10]:


fig1_max_f = go.Figure()
fig1_max_f.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Max<br><span style='font-size:0.8em;color:tomato'>Femme</span><br>"+str(y_max_df_Population_A_1_F.values)},
    value = max_df_Population_A_1_F,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_f.update_layout(paper_bgcolor = "white",
                         width=200,
                         height=200,
                         font=dict(
                 family=" Gravitas One, cursive",
                 size=13))



# In[11]:


fig_min_t = go.Figure()
fig_min_t.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:lightseagreen'>Total</span><br>"+str(y_min_df_Population_A_1.values)},
    value = min_df_Population_A_1,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig_min_t.update_layout(paper_bgcolor = "white",
                        width=300,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=13))



# In[12]:


fig_min_t_m = go.Figure()
fig_min_t_m.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:royalblue'>Homme</span><br>"+str(y_min_df_Population_A_1_M.values)},
    value = min_df_Population_A_1_M,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig_min_t_m.update_layout(paper_bgcolor = "white",
                          width=200,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=13))



# In[13]:


fig_min_f = go.Figure()
fig_min_f.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:tomato'>Femme</span><br>"+str(y_min_df_Population_A_1_F.values)},
    value = min_df_Population_A_1_F,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig_min_f.update_layout(paper_bgcolor = "white",
                        width=200,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=13))

def indicatorsOwnAccount():
    return(fig1_max_t,fig1_max_t_m,fig1_max_f,fig_min_t,fig_min_t_m,fig_min_f)
