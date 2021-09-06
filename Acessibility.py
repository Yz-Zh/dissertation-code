# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 16:14:32 2021

@author: Yz Zh
"""

import aceso
import numpy as np
import pandas as pd

#########
select_area="Shanghai" ##London  Shanghai
select_ps="school" ##park  hospital  school
select_model="gbm" ##gbm  2sfca
select_decay="parabolic" ##gaussian  raised_cosine  parabolic
#########
if select_area=="Shanghai":
    if select_ps=="park":
        distance=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\park\\shanghai_park_distance.csv")
        pop=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\pop.csv")
        supply=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\park\\shanghai_park_size.csv")
        if select_model=="2sfca":
            radius=1800.0
            model1 = aceso.TwoStepFCA(radius=radius)
            score = model1.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_1=pd.DataFrame(np.hstack(score))
            score_dataframe_1.to_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\park\\result\\2sfca_"
                                     +str(int(radius/60))+"min.csv")
        if select_model=="gbm":
            para=3600.0
            model0 = aceso.GravityModel(decay_function=select_decay,
                                        decay_params={'sigma':para})
            score = model0.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_0=pd.DataFrame(np.hstack(score))
            score_dataframe_0.to_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\park\\result\\gbm_"+
                                     str(select_decay)+"_"+
                                     str(int(para))+".csv")



    if select_ps=="school":
        distance=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\school\\shanghai_school_distance.csv")
        pop=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\pop.csv")
        supply=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\school\\shanghai_school_enrolment.csv")
        if select_model=="2sfca":
            radius=3600.0
            model1 = aceso.TwoStepFCA(radius=radius)
            score = model1.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_1=pd.DataFrame(np.hstack(score))
            score_dataframe_1.to_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\school\\result\\2sfca_"
                                     +str(int(radius/60))+"min.csv")
        if select_model=="gbm":
            para=3600.0
            model0 = aceso.GravityModel(decay_function=select_decay,
                                        decay_params={'scale':para})
            score = model0.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_0=pd.DataFrame(np.hstack(score))
            score_dataframe_0.to_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\school\\result\\gbm_"
                                     +str(select_decay)+"_"
                                     +str(int(para))+".csv")
    
    if select_ps=="hospital":
        distance=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\hospital\\shanghai_hospital_distance.csv")
        pop=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\pop.csv")
        supply=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\hospital\\shanghai_hospital_beds.csv")
        if select_model=="2sfca":
            radius=1800.0
            model1 = aceso.TwoStepFCA(radius=radius)
            score = model1.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_1=pd.DataFrame(np.hstack(score))
            score_dataframe_1.to_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\hospital\\result\\2sfca_"+str(int(radius/60))+"min.csv")
        if select_model=="gbm":
            para=900.0
            model0 = aceso.GravityModel(decay_function=select_decay,
                                        decay_params={'sigma':para})
            score = model0.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_0=pd.DataFrame(np.hstack(score))
            score_dataframe_0.to_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\hospital\\result\\gbm_"
                                     +str(select_decay)+"_"
                                     +str(int(para))+".csv")

    
if select_area=="London":

    if select_ps=="park":
        distance=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\demo-last.csv")
        pop=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\school\\matrix\\population.csv")
        supply=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\size.csv")
        if select_model=="2sfca":
            radius=7200.0
            model1 = aceso.TwoStepFCA(radius=radius)
            score = model1.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_1=pd.DataFrame(np.hstack(score))
            score_dataframe_1.to_csv("C:\\Users\\Yz Zh\\Desktop\\park\\2sfca_"
                                     +str(int(radius/60))+"min.csv")
        if select_model=="gbm":
            para=2700.0
            model0 = aceso.GravityModel(decay_function=select_decay,
                                        decay_params={'sigma':para})
            score = model0.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_0=pd.DataFrame(np.hstack(score))
            score_dataframe_0.to_csv("C:\\Users\\Yz Zh\\Desktop\\park\\gbm_"
                                     +str(select_decay)+"_"
                                     +str(int(para))+".csv")
    
    
    
    if select_ps=="school":
        supply=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\school\\matrix\\supply.csv")
        pop=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\school\\matrix\\population.csv")
        distance=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\school\\matrix\\school ward travel time car.csv")
        if select_model=="2sfca":
            radius=2000.0
            model1 = aceso.TwoStepFCA(radius=radius)
            score = model1.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_1=pd.DataFrame(np.hstack(score))
            score_dataframe_1.to_csv("C:\\Users\\Yz Zh\\Desktop\\school\\2sfca_"
                                     +str(int(radius/60))+"min.csv")
        if select_model=="gbm":
            para=3600.0
            model0 = aceso.GravityModel(decay_function=select_decay,
                                        decay_params={'scale':para})
            score = model0.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_0=pd.DataFrame(np.hstack(score))
            score_dataframe_0.to_csv("C:\\Users\\Yz Zh\\Desktop\\school\\gbm_"
                                     +str(select_decay)+"_"
                                     +str(int(para))+".csv")
    
    if select_ps=="hospital":
        distance=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\hospital\\hospital ward travel time car.csv")
        pop=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\school\\matrix\\population.csv")
        supply=pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\hospital\\beds.csv")
        if select_model=="2sfca":
            radius=3600.0
            model1 = aceso.TwoStepFCA(radius=radius)
            score = model1.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_1=pd.DataFrame(np.hstack(score))
            score_dataframe_1.to_csv("C:\\Users\\Yz Zh\\Desktop\\hospital\\2sfca_"
                                     +str(int(radius/60))+"min.csv")
        if select_model=="gbm":
            para=3600.0
            model0 = aceso.GravityModel(decay_function=select_decay,
                                        decay_params={'sigma':para})
            score = model0.calculate_accessibility_scores(
                distance_matrix=distance.values,
                demand_array=pop.values,
                supply_array=supply.values.T
            )
            score_dataframe_0=pd.DataFrame(np.hstack(score))
            score_dataframe_0.to_csv("C:\\Users\\Yz Zh\\Desktop\\hospital\\gbm_"
                                     +str(select_decay)+"_"
                                     +str(int(para))+".csv")






