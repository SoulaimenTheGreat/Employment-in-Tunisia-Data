# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
from data_viz.Project_Employement.code.raw_code.data_plotting.plots.Population_Active_Visualisation import population_active_occupée,population_active_occupée_sex,population_active,population_active_sex,indicators,population_active_sex
from data_viz.Project_Employement.code.raw_code.data_plotting.plots.Bureau_demploi_tt import Evolution_demandes_emploi,demande_emploi_hvf,demande_emploi,Demandes_emploi_Vs_Offres_reçues,evolution_offre_emploi,offre_emploi,indicatorsBureauEmploi
from data_viz.Project_Employement.code.raw_code.data_plotting.plots.chomage_visualisation import population_active_chômage,Taux_chômage,Taux_chômage_sexe,Taux_chômage_diplome,chomage_map,indicatorsChomage
from data_viz.Project_Employement.code.raw_code.data_plotting.plots.Own_account_workers import Travailleurs_independants,Travailleurs_independants_sex,indicatorsOwnAccount
from data_viz.Project_Employement.code.raw_code.data_plotting.plots.Population_occupée_Visualisation import Evolution_population_âge_activité,Evolution_population_âge_activité_sex,Evolution_créations_emploi,secteur_activité,indicatorsOccupée

import plotly
import json




@blueprint.route('/<template>')
def route_template(template):
   
    try:
        #Affichage des plots de Population occupée
        if(template=="Populationoccupée"):
            
            name="Population occupée"
            fig_PO1=Evolution_population_âge_activité()
            graphJSON1 = json.dumps(fig_PO1, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig_PO2=Evolution_population_âge_activité_sex()
            graphJSON2 = json.dumps(fig_PO2, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig_PO3=Evolution_créations_emploi()
            graphJSON3 = json.dumps(fig_PO3, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig_PO4=secteur_activité()
            graphJSON4= json.dumps(fig_PO4, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig1_max_t,fig1_max_t_m,fig1_max_f,fig1_min_t,fig1_min_t_m,fig1_min_f,fig1_max_t_oce,fig1_min_t_oce=indicatorsOccupée()
            graphJSON_fig1_max_t= json.dumps(fig1_max_t, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_t_m= json.dumps(fig1_max_t_m, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_f= json.dumps(fig1_max_f, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_t= json.dumps(fig1_min_t, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_t_m= json.dumps(fig1_min_t_m, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_f= json.dumps(fig1_min_f, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_t_oce= json.dumps(fig1_max_t_oce, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_min_t_oce= json.dumps(fig1_min_t_oce, cls=plotly.utils.PlotlyJSONEncoder)

            return render_template(template + '.html',template=name,plot1=graphJSON1,
                                    plot2=graphJSON2,
                                    plot3=graphJSON3,
                                    plot4=graphJSON4,
                                    plot5=graphJSON_fig1_max_t,
                                    plot6=graphJSON_fig1_max_t_m,
                                    plot7=graphJSON_fig1_max_f,
                                    plot8=graphJSON_fig_min_t,
                                    plot9=graphJSON_fig_min_t_m,
                                    plot10=graphJSON_fig_min_f,
                                    plot11=graphJSON_fig1_max_t_oce,
                                    plot12=graphJSON_fig1_min_t_oce)
        #Affichage des plots de Bureau d'emploi
        if(template=="Bureauemploi"):
            
            
             name="Bureau d'emploi"          
             fig_BE1=offre_emploi()
             graphJSON1 = json.dumps(fig_BE1, cls=plotly.utils.PlotlyJSONEncoder)
             
             fig_BE2=evolution_offre_emploi()
             graphJSON2 = json.dumps(fig_BE2, cls=plotly.utils.PlotlyJSONEncoder)
             
             fig_BE3=Demandes_emploi_Vs_Offres_reçues()
             graphJSON3 = json.dumps(fig_BE3, cls=plotly.utils.PlotlyJSONEncoder)
             
             fig_BE4= Evolution_demandes_emploi()
             graphJSON4 = json.dumps(fig_BE4, cls=plotly.utils.PlotlyJSONEncoder)
             
             fig_BE5=demande_emploi_hvf()
             graphJSON5 = json.dumps(fig_BE5, cls=plotly.utils.PlotlyJSONEncoder)
             
             fig_BE6=demande_emploi()
             graphJSON6 = json.dumps(fig_BE6, cls=plotly.utils.PlotlyJSONEncoder)
             
             fig1_max_be,fig1_max_be_oe,fig_min_be,fig_min_be_oe=indicatorsBureauEmploi()
             
             graphJSON_fig1_max_be= json.dumps(fig1_max_be, cls=plotly.utils.PlotlyJSONEncoder)
             graphJSON_fig1_max_be_oe= json.dumps(fig1_max_be_oe, cls=plotly.utils.PlotlyJSONEncoder)
             graphJSON_fig_min_be= json.dumps(fig_min_be, cls=plotly.utils.PlotlyJSONEncoder)
             graphJSON_fig_min_be_oe= json.dumps(fig_min_be_oe, cls=plotly.utils.PlotlyJSONEncoder)


             return render_template(template + '.html',template=name,plot1=graphJSON1,
                                    plot2=graphJSON2,
                                    plot3=graphJSON3,
                                    plot4=graphJSON4,
                                    plot5=graphJSON5,
                                    plot6=graphJSON6,
                                    plot7=graphJSON_fig1_max_be,
                                    plot8=graphJSON_fig1_max_be_oe,
                                    plot9=graphJSON_fig_min_be,
                                    plot10=graphJSON_fig_min_be_oe
                                    )
             
            
            #Carte Tunisienne 
        if(template=="Cartetunisienne"):
            name="Carte tunisienne" 
            figtun,fig1_max_tcr,fig1_min_tcr=chomage_map()
            graphJSON_figtun = json.dumps(figtun, cls=plotly.utils.PlotlyJSONEncoder) 
            graphJSON_fig1_max_tcr = json.dumps(fig1_max_tcr, cls=plotly.utils.PlotlyJSONEncoder) 
            graphJSON_fig1_min_tcr = json.dumps(fig1_min_tcr, cls=plotly.utils.PlotlyJSONEncoder) 
            return render_template(template + '.html',template=name,
                                   plot1=graphJSON_figtun,
                                   plot2=graphJSON_fig1_max_tcr,
                                   plot3=graphJSON_fig1_min_tcr)
        
        #Chomage visualisation
        if(template=="Chômeurs"):
              
            name="Chômeurs"
            fig_chomage1=population_active_chômage()

            graphJSON1 = json.dumps(fig_chomage1, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig_chomage2=Taux_chômage()
            graphJSON2 = json.dumps(fig_chomage2, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig_chomage3=Taux_chômage_sexe()
            graphJSON3 = json.dumps(fig_chomage3, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig_chomage4=Taux_chômage_diplome()
            graphJSON4= json.dumps(fig_chomage4, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig1_max_t_c,fig1_max_t_m_c,fig1_max_f_c,fig1_min_t_c,fig1_min_t_m_c,fig1_min_f_c,fig1_max_t_tc,fig1_max_t_m_tc,fig1_max_f_tc,fig1_min_t_tc,fig1_min_t_m_tc,fig1_min_f_tc,fig1_max_t_ces,fig1_max_t_m_ces,fig1_max_f_ces,fig1_min_t_ces,fig1_min_t_m_ces,fig1_min_f_ces=indicatorsChomage()
            graphJSON_fig1_max_t_c= json.dumps(fig1_max_t_c, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_t_m_c= json.dumps(fig1_max_t_m_c, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_f_c= json.dumps(fig1_max_f_c, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_min_t_c= json.dumps(fig1_min_t_c, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_min_t_m_c= json.dumps(fig1_min_t_m_c, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_min_f_c= json.dumps(fig1_min_f_c, cls=plotly.utils.PlotlyJSONEncoder)
            
            graphJSON_fig1_max_t_tc= json.dumps(fig1_max_t_tc, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_t_m_tc= json.dumps(fig1_max_t_m_tc, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_f_tc= json.dumps(fig1_max_f_tc, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_min_t_tc= json.dumps(fig1_min_t_tc, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_min_t_m_tc= json.dumps(fig1_min_t_m_tc, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_min_f_tc= json.dumps(fig1_min_f_tc, cls=plotly.utils.PlotlyJSONEncoder)
            
            
            graphJSON_fig1_max_t_m_ces= json.dumps(fig1_max_t_m_ces, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_f_ces= json.dumps(fig1_max_f_ces, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_min_t_m_ces= json.dumps(fig1_min_t_m_ces, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_min_f_ces= json.dumps(fig1_min_f_ces, cls=plotly.utils.PlotlyJSONEncoder)
            
            return render_template(template + '.html',template=name,
                                    plot1=graphJSON1,
                                    plot2=graphJSON2,
                                    plot3=graphJSON3,
                                    plot4=graphJSON4,
                                    plot5=graphJSON_fig1_max_t_c,
                                    plot6=graphJSON_fig1_max_t_m_c,
                                    plot7=graphJSON_fig1_max_f_c,  
                                    plot8=graphJSON_fig1_min_t_c,
                                    plot9=graphJSON_fig1_min_t_m_c,
                                    plot10=graphJSON_fig1_min_f_c,
                                    plot11=graphJSON_fig1_max_t_tc,
                                    plot12=graphJSON_fig1_max_t_m_tc,
                                    plot13=graphJSON_fig1_max_f_tc,  
                                    plot14=graphJSON_fig1_min_t_tc,
                                    plot15=graphJSON_fig1_min_t_m_tc,
                                    plot16=graphJSON_fig1_min_f_tc,
                                    plot17=graphJSON_fig1_max_t_m_ces,
                                    plot18=graphJSON_fig1_max_f_ces, 
                                    plot19=graphJSON_fig1_min_t_m_ces,
                                    plot20=graphJSON_fig1_min_f_ces,)
            
        
            #Population active
        if(template=="PopulationActive"):
            
            name="PopulationActive"   
            fig_PO1=population_active_occupée()
            graphJSON1 = json.dumps(fig_PO1, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig_PO2=population_active_occupée_sex()
            graphJSON2 = json.dumps(fig_PO2, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig_PO3=population_active()
            graphJSON3 = json.dumps(fig_PO3, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig_PO4=indicators()
            graphJSON4= json.dumps(fig_PO4, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig_PO5=population_active_sex()
            graphJSON5= json.dumps(fig_PO5, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig1_max_t,fig1_max_t_m,fig1_max_f,fig_min_t,fig_min_t_m,fig_min_f,fig1_max_t_pa,fig1_max_t_m_pa,fig1_max_f_pa,fig_min_t_pa,fig_min_t_m_pa,fig_min_f_pa=indicators()
            graphJSON_fig1_max_t= json.dumps(fig1_max_t, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_t_m= json.dumps(fig1_max_t_m, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_f= json.dumps(fig1_max_f, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_t= json.dumps(fig_min_t, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_t_m= json.dumps(fig_min_t_m, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_f= json.dumps(fig_min_f, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_t_pa= json.dumps(fig1_max_t_pa, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_t_m_pa= json.dumps(fig1_max_t_m_pa, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_f_pa= json.dumps(fig1_max_f_pa, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_t_pa= json.dumps(fig_min_t_pa, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_t_m_pa= json.dumps(fig_min_t_m_pa, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_f_pa= json.dumps(fig_min_f_pa, cls=plotly.utils.PlotlyJSONEncoder)



            return render_template(template + '.html',template=name,plot1=graphJSON1,
                                    plot2=graphJSON2,
                                    plot3=graphJSON3,
                                    plot4=graphJSON4,
                                    plot5=graphJSON_fig1_max_t,
                                    plot6=graphJSON_fig1_max_t_m,
                                    plot7=graphJSON_fig1_max_f,
                                    plot8=graphJSON_fig_min_t,
                                    plot9=graphJSON_fig_min_t_m,
                                    plot10=graphJSON_fig_min_f,
                                    plot11=graphJSON5,
                                    plot12=graphJSON_fig1_max_t_pa,
                                    plot13=graphJSON_fig1_max_t_m_pa,
                                    plot14=graphJSON_fig1_max_f_pa,
                                    plot15=graphJSON_fig_min_t_pa,
                                    plot16=graphJSON_fig_min_t_m_pa,
                                    plot17=graphJSON_fig_min_f_pa
                                    )
            
            #NonSalariés
        if(template=="Nonsalariés"):
            
            name="Non salariés"
            fig1_max_t,fig1_max_t_m,fig1_max_f,fig_min_t,fig_min_t_m,fig_min_f=indicatorsOwnAccount()
            graphJSON_fig1_max_t= json.dumps(fig1_max_t, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_t_m= json.dumps(fig1_max_t_m, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig1_max_f= json.dumps(fig1_max_f, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_t= json.dumps(fig_min_t, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_t_m= json.dumps(fig_min_t_m, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON_fig_min_f= json.dumps(fig_min_f, cls=plotly.utils.PlotlyJSONEncoder)  
            fig_NS1=Travailleurs_independants()
            graphJSON1 = json.dumps(fig_NS1, cls=plotly.utils.PlotlyJSONEncoder)
            
            fig_NS2=Travailleurs_independants_sex()
            graphJSON2 = json.dumps(fig_NS2, cls=plotly.utils.PlotlyJSONEncoder)
            return render_template(template + '.html',template=name,plot1=graphJSON1,
                                    plot2=graphJSON2,
                                    plot3=graphJSON_fig1_max_t,
                                    plot4=graphJSON_fig1_max_t_m,
                                    plot5=graphJSON_fig1_max_f,
                                    plot6=graphJSON_fig_min_t,
                                    plot7=graphJSON_fig_min_t_m,
                                    plot8=graphJSON_fig_min_f)
        if(template=="Story"):
            
            
            fig_NS2=Travailleurs_independants_sex()
            graphJSON2 = json.dumps(fig_NS2, cls=plotly.utils.PlotlyJSONEncoder)
            return render_template(template + '.html',template=template)
        if(template=="Population"):
            
            
            fig_NS2=Travailleurs_independants_sex()
            graphJSON2 = json.dumps(fig_NS2, cls=plotly.utils.PlotlyJSONEncoder)
            return render_template(template + '.html',template=template)

        
    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

