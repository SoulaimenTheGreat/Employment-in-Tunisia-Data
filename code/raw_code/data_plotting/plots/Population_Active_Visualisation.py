#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import plotly.graph_objects as go


# In[2]:


df_Population_A_1=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/Population active/Evolution de la population active occupée selon le sexe.csv",
                                header=1)
df_Population_A_1.head()


# In[3]:


max_df_Population_A_1=max(df_Population_A_1["Evolution de la population active occupée"])
y_max_df_Population_A_1=df_Population_A_1[" "].loc[df_Population_A_1["Evolution de la population active occupée"] == max_df_Population_A_1]

max_df_Population_A_1_M=max(df_Population_A_1["Population active occupée Masculine"])
y_max_df_Population_A_1_M=df_Population_A_1[" "].loc[df_Population_A_1["Population active occupée Masculine"] == max_df_Population_A_1_M]

max_df_Population_A_1_F=max(df_Population_A_1["Population active occupée Féminine"])
y_max_df_Population_A_1_F=df_Population_A_1[" "].loc[df_Population_A_1["Population active occupée Féminine"] == max_df_Population_A_1_F]

min_df_Population_A_1=min(df_Population_A_1["Evolution de la population active occupée"])
y_min_df_Population_A_1=df_Population_A_1[" "].loc[df_Population_A_1["Evolution de la population active occupée"] == min_df_Population_A_1]

min_df_Population_A_1_M=min(df_Population_A_1["Population active occupée Masculine"])
y_min_df_Population_A_1_M=df_Population_A_1[" "].loc[df_Population_A_1["Population active occupée Masculine"] == min_df_Population_A_1_M]

min_df_Population_A_1_F=min(df_Population_A_1["Population active occupée Féminine"])
y_min_df_Population_A_1_F=df_Population_A_1[" "].loc[df_Population_A_1["Population active occupée Féminine"] == min_df_Population_A_1_F]


# In[4]:

def population_active_occupée():
    fig1=go.Figure(go.Scatter(x=df_Population_A_1[' '], 
                              y=df_Population_A_1['Evolution de la population active occupée'],
                              name='Total',
                              mode='lines+markers',
                              line = dict(color='lightseagreen')))
    
    # Edit the layout
    fig1.update_layout(title='Evolution de la population active occupée selon le sexe',template='plotly_white',font=dict(
                     family=" Gravitas One, cursive",
                     size=13))
    fig1.update_xaxes(showticklabels=False)
    fig1.update_yaxes(showticklabels=False)
    return fig1


# In[5]:


df_Population_A_1_2011=df_Population_A_1.loc[df_Population_A_1[" "].str.contains("2011"),:]
df_Population_A_1_2012=df_Population_A_1.loc[df_Population_A_1[" "].str.contains("2012"),:]
df_Population_A_1_2013=df_Population_A_1.loc[df_Population_A_1[" "].str.contains("2013"),:]
df_Population_A_1_2014=df_Population_A_1.loc[df_Population_A_1[" "].str.contains("2014"),:]
df_Population_A_1_2015=df_Population_A_1.loc[df_Population_A_1[" "].str.contains("2015"),:]
df_Population_A_1_2016=df_Population_A_1.loc[df_Population_A_1[" "].str.contains("2016"),:]
df_Population_A_1_2017=df_Population_A_1.loc[df_Population_A_1[" "].str.contains("2017"),:]
df_Population_A_1_2018=df_Population_A_1.loc[df_Population_A_1[" "].str.contains("2018"),:]
df_Population_A_1_2019=df_Population_A_1.loc[df_Population_A_1[" "].str.contains("2019"),:]


# In[6]:


data_o=[
    go.Scatter(
              x=df_Population_A_1[' '], 
              y=df_Population_A_1["Population active occupée Masculine"], 
              name='Homme',
              mode='lines+markers',
              line=dict(
              color='royalblue')),
    go.Scatter(
              x=df_Population_A_1[' '], 
              y=df_Population_A_1["Population active occupée Féminine"], 
              name='Femme',
              mode='lines+markers',
              line=dict(
              color='tomato')),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_1_2011[' '], 
           y=df_Population_A_1_2011["Population active occupée Masculine"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_1_2011[' '], 
           y=df_Population_A_1_2011["Population active occupée Féminine"],
            marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_1_2012[' '], 
           y=df_Population_A_1_2012["Population active occupée Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_1_2012[' '], 
           y=df_Population_A_1_2012["Population active occupée Féminine"],
            marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_1_2013[' '], 
           y=df_Population_A_1_2013["Population active occupée Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_1_2013[' '], 
           y=df_Population_A_1_2013["Population active occupée Féminine"],
            marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_1_2014[' '], 
           y=df_Population_A_1_2014["Population active occupée Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_1_2014[' '], 
           y=df_Population_A_1_2014["Population active occupée Féminine"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_1_2015[' '], 
           y=df_Population_A_1_2015["Population active occupée Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_1_2015[' '], 
           y=df_Population_A_1_2015["Population active occupée Féminine"],
            marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_1_2016[' '], 
           y=df_Population_A_1_2016["Population active occupée Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_1_2016[' '], 
           y=df_Population_A_1_2016["Population active occupée Féminine"],
            marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_1_2017[' '], 
           y=df_Population_A_1_2017["Population active occupée Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_1_2017[' '], 
           y=df_Population_A_1_2017["Population active occupée Féminine"],
            marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_1_2018[' '], 
           y=df_Population_A_1_2018["Population active occupée Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_1_2018[' '], 
           y=df_Population_A_1_2018["Population active occupée Féminine"],
            marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_1_2019[' '], 
           y=df_Population_A_1_2019["Population active occupée Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_1_2019[' '], 
           y=df_Population_A_1_2019["Population active occupée Féminine"],
            marker_color='tomato'),
    
]


# In[7]:


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
layout_o=go.Layout(updatemenus=list([dict(buttons= list_updatemenus)]),title_text="Evolution de la population active occupée selon le sexe",template='plotly_white',font=dict(
                 family=" Gravitas One, cursive",
                 size=13))

#defining figure and plotting
fig_o = go.Figure(data_o,layout_o)
def population_active_occupée_sex():
   return fig_o


# In[8]:


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
                           width=300,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=20))




# In[10]:


fig1_max_f = go.Figure()
fig1_max_f.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Max<br><span style='font-size:0.8em;color:tomato'>Female</span><br>"+str(y_max_df_Population_A_1_F.values)},
    value = max_df_Population_A_1_F,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig1_max_f.update_layout(paper_bgcolor = "white",
                         width=300,
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
                          width=300,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=13))



# In[13]:


fig_min_f = go.Figure()
fig_min_f.add_trace(go.Indicator(
    mode = "number",
    title = {"text": "Min<br><span style='font-size:0.8em;color:tomato'>Female</span><br>"+str(y_min_df_Population_A_1_F.values)},
    value = min_df_Population_A_1_F,
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig_min_f.update_layout(paper_bgcolor = "white",
                        width=300,
                         height=200,font=dict(
                 family=" Gravitas One, cursive",
                 size=13))




# In[14]:


df_Population_A_2=pd.read_csv("~/data_viz/Project_Employement/data/tidy_data/Population active/Evolution de la population active selon le sexe.csv",
                                header=1)
df_Population_A_2.head()


# In[15]:

def population_active():
    fig3=go.Figure(data=[go.Scatter(x=df_Population_A_2[' '], 
                                      y=df_Population_A_2["Evolution de la population active"], 
                                      name='Total',
                                      mode='lines+markers',
                                      line = dict(color='lightseagreen'))
        
    ])
    # Edit the layout
    fig3.update_layout(title="Evolution de la population active",template='plotly_white',font=dict(
                     family=" Gravitas One, cursive",
                     size=13))
    fig3.update_xaxes(showticklabels=False)
    fig3.update_yaxes(showticklabels=False)
    return fig3


# In[16]:


df_Population_A_2_2011=df_Population_A_2.loc[df_Population_A_2[" "].str.contains("2011"),:]
df_Population_A_2_2012=df_Population_A_2.loc[df_Population_A_2[" "].str.contains("2012"),:]
df_Population_A_2_2013=df_Population_A_2.loc[df_Population_A_2[" "].str.contains("2013"),:]
df_Population_A_2_2014=df_Population_A_2.loc[df_Population_A_2[" "].str.contains("2014"),:]
df_Population_A_2_2015=df_Population_A_2.loc[df_Population_A_2[" "].str.contains("2015"),:]
df_Population_A_2_2016=df_Population_A_2.loc[df_Population_A_2[" "].str.contains("2016"),:]
df_Population_A_2_2017=df_Population_A_2.loc[df_Population_A_2[" "].str.contains("2017"),:]
df_Population_A_2_2018=df_Population_A_2.loc[df_Population_A_2[" "].str.contains("2018"),:]
df_Population_A_2_2019=df_Population_A_2.loc[df_Population_A_2[" "].str.contains("2019"),:]


# In[17]:


data_a=[
    go.Scatter(
              x=df_Population_A_2[' '], 
              y=df_Population_A_2["Evolution de la population active Masculine"], 
              name='Homme',
              mode='lines+markers',
              line=dict(
              color='royalblue')),
    go.Scatter(
              x=df_Population_A_2[' '], 
              y=df_Population_A_2["Evolution de la population active Féminine"], 
              name='Femme',
              mode='lines+markers',
              line=dict(
              color='tomato')),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_2_2011[' '], 
           y=df_Population_A_2_2011["Evolution de la population active Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_2_2011[' '], 
           y=df_Population_A_2_2011["Evolution de la population active Féminine"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_2_2012[' '], 
           y=df_Population_A_2_2012["Evolution de la population active Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_2_2012[' '], 
           y=df_Population_A_2_2012["Evolution de la population active Féminine"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_2_2013[' '], 
           y=df_Population_A_2_2013["Evolution de la population active Masculine"],
           marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_2_2013[' '], 
           y=df_Population_A_2_2013["Evolution de la population active Féminine"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_2_2014[' '], 
           y=df_Population_A_2_2014["Evolution de la population active Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_2_2014[' '], 
           y=df_Population_A_2_2014["Evolution de la population active Féminine"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_2_2015[' '], 
           y=df_Population_A_2_2015["Evolution de la population active Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_2_2015[' '], 
           y=df_Population_A_2_2015["Evolution de la population active Féminine"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_2_2016[' '], 
           y=df_Population_A_2_2016["Evolution de la population active Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_2_2016[' '], 
           y=df_Population_A_2_2016["Evolution de la population active Féminine"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_2_2017[' '], 
           y=df_Population_A_2_2017["Evolution de la population active Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_2_2017[' '], 
           y=df_Population_A_2_2017["Evolution de la population active Féminine"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_2_2018[' '], 
           y=df_Population_A_2_2018["Evolution de la population active Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_2_2018[' '], 
           y=df_Population_A_2_2018["Evolution de la population active Féminine"],
           marker_color='tomato'),
    go.Bar(name='Homme',
           visible=False,
           x=df_Population_A_2_2019[' '], 
           y=df_Population_A_2_2019["Evolution de la population active Masculine"],
          marker_color='royalblue'),
    go.Bar(name='Femme',
           visible=False,
           x=df_Population_A_2_2019[' '], 
           y=df_Population_A_2_2019["Evolution de la population active Féminine"],
         marker_color='tomato')
    

    
]


# In[18]:


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
layout_a=go.Layout(updatemenus=list([dict(buttons= list_updatemenus)]),title_text="Evolution de la population active selon le sex",template='plotly_white',font=dict(
                 family=" Gravitas One, cursive",
                 size=13))

#defining figure and plotting
fig_bar_15 = go.Figure(data_a,layout_a)
def population_active_sex():
    return fig_bar_15


def indicators():
    return(fig1_max_t,fig1_max_t_m,fig1_max_f,fig_min_t,fig_min_t_m,fig_min_f)

