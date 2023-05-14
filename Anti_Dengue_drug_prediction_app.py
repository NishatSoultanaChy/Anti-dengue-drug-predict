# -*- coding: utf-8 -*-
"""
Created on Mon May  1 11:54:18 2023

@author: User
"""

#install libraries
######################
# Import libraries
######################
import numpy as np
import pandas as pd
import streamlit as st

import pickle
#from PIL import Image
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
install('padelpy')

from padelpy import from_smiles

######################
# Custom function
######################

#def generate(smiles, verbose=False):

 #  descriptors = pd.DataFrame(from_smiles(smiles, threads = 1))
 #  return descriptors

######################
# Page Title
######################

#image = Image.open('solubility_logo.jpg')

#st.image(image, use_column_width=True)

st.write("""
# Anti-dengue Drug Prediction Web App

This app predicts the **Bioactivity (pIC50)** values of molecules!

""")


######################
# Input molecules (Side Panel)
######################

st.header('User Input Features')

## Read SMILES input
SMILES_input = "ccc"

SMILES = st.text_area("SMILES input",  SMILES_input)

#st.header('Input SMILES')
S= SMILES.upper()

S

## Calculate molecular descriptors
#st.header('Computed molecular descriptors')
desc = from_smiles('CCC')

#st.header('Descriptors')

desc
#X = pd.DataFrame(from_smiles([SMILES], threads = 1))

#X = X[["SpMax7_Bhi", "IC5", "nRotB", "SpMin8_Bhs", "SpAD_Dzv", "AATSC2e", "ATSC1v", "Kier2", "McGowan_Volume", "GATS1m", 
#              "SHBint3", "SpMAD_Dze", "AATS2v", "CIC5", "VE2_Dzp", "VP-1", "BCUTc-1l", "SpMax_Dzp", "SHBint10", "minHBint7",
#          "AATSC2c", "AATS1i", "maxwHBa", "minHBd", "GATS2i", "ETA_Shape_Y", "SHBint7", "VR2_D", "VR1_Dt", "VR3_Dzp", 
#            "XLogP", "GATS5i", "BCUTp-1l", "ETA_BetaP_s", "AATS8i", "C1SP2", "GATS8s", "ATSC2c", "AATS4i", "AATS2i", 
#            "VR1_Dzp", "minHBint9"]]

#X.replace([np.inf, -np.inf], np.nan, inplace=True)
#X = X.astype("float64")
#X = pd.DataFrame(X).fillna(0)


######################
# Pre-built model
######################

# Reads in saved model
#load_model = pickle.load(open('finalized_model_ET_42.pkl', 'rb'))

# Apply model to make predictions
#prediction = load_model.predict(X)

#st.header('Predicted pIC50(nM) value')
#prediction
