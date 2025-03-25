# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class PreclampsiaBase(BaseModel):
	Age: int
	Pre_pregnancy_Weight: float
	Parity: int
	Annual_Income: int
	Socioeconomic_Status: int
	History_of_Hypertension: int
	History_of_Diabetes: int
	History_of_Preeclampsia: int
	Proteinuria_Levels: float
	Month: int
	Systolic_BP: int
	Diastolic_BP: int
