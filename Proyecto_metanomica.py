#!/usr/bin/env python
# coding: utf-8

# # Proyecto comparación de Outputs de clasificación taxonómica

# In[2]:


import pandas as pd 
import numpy as np


# In[3]:


# lectura de los datos por medio de pandas
# Se tomaron las 10 primeras lineas de el output de kraken
# datakraken10 = pd.read_csv('data/10lineas_kraken',sep='\t',header=None, names=["c-clasificado", "read","taxon_kraken","1","2"])
datakraken10 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRHYe0R7d5WYmKNbyo13egj8ORiKqWwI1GEVaG5Nzp7xN3RjkIV6vnHUweKYpidborNBf4-IEWbk0ZD/pub?output=csv',header=None, names=["c-clasificado", "read","taxon_kraken","1","2"])
# Se tomaron las 10 primeras lineas de el output de kaiju
# datakaiju10 = pd.read_csv('data/10lineas_kaiju',sep='\t',header=None, names=["c-clasificado", "read","taxon_kaiju"])
datakaiju10 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRuQ78ZkMRkMz61t0mbMBf4GGsd1ydGxXCl7p2Y8UzgXflkK6w4RCr6lPWXc9oxUXq94qeUJKouCMHp/pub?output=csv',header=None, names=["c-clasificado", "read","taxon_kaiju"])
# Se tomaron las 10 ultimas lineas de el output de kraken
# datakraken10c = pd.read_csv('data/10lineascola_kraken',sep='\t',header=None, names=["c-clasificado", "read","taxon_kraken2","1","2"])
datakraken10c = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQJ7psycVzaws-XI_z1itUnxCI3eXBGqK4q57B4gE1YYCVCn_GkvNUZClHPMtrHANy3JUIDpqaW_r0u/pub?output=csv',header=None, names=["c-clasificado", "read","taxon_kraken2","1","2"])
# Se tomaron las 10 ultimas lineas de el output de kaiju
#datakaiju10c = pd.read_csv('data/10lineascola_kaiju',sep='\t',header=None, names=["c-clasificado", "read","taxon_kaiju2"])
datakaiju10c = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-etvzQ8vKI0Xwggc_RvqWboa39GcRdMBw_dSa4-_mx5k9PvaMtfuaqUGvpBM3zUKLDbVkiJ3udybC/pub?output=csv',header=None, names=["c-clasificado", "read","taxon_kaiju2"])


# identificar tipo de datos**(Kraken o Kaiju) para automatizar el In3

# In[4]:


datakraken10


# In[3]:


# Eliminamos las columnas no necesarias
datakraken101 = datakraken10.drop(['c-clasificado','1', '2'], axis=1)
datakaiju101 = datakaiju10.drop(['c-clasificado'], axis=1)
datakraken102 = datakraken10c.drop(['c-clasificado','1','2'], axis=1)
datakaiju102 = datakaiju10c.drop(['c-clasificado'], axis=1)


# Funcion para los parametros de entrada

# In[4]:


lOutputs = [datakraken101, datakaiju101, datakraken102, datakaiju102] # lista de dataframes
# Funcion para unir los outputs en un solo dataframe, tomando como referencia la columna 'read'
def function(lOutputs):
    DFfusion = lOutputs[0]
    for i in lOutputs:
        DFfusion = pd.merge(DFfusion, i, how='outer')
   
    return DFfusion

DFfusion = function(lOutputs)    
DFfusion


# ## Tomando la totalidad de los datos

# In[5]:


datakraken = pd.read_csv('data/EG1BMAA_kraken.tsv',sep='\t',header=None, names=['c-clasificado',"read","taxon_kraken",'1','2']) 
datakaiju = pd.read_csv('data/EG1BMAA_kaiju.tsv',sep='\t',header=None, names=['c-clasificado',"read","taxon_kaiju"])


# In[6]:


datakrakenall = datakraken.drop(['c-clasificado','1', '2'], axis=1)
datakaijuall = datakaiju.drop(['c-clasificado'], axis=1)


# In[7]:


allOutputs = [datakrakenall, datakaijuall] #lista de dataframe
DFfusion = function(allOutputs)    
DFfusion


# In[8]:


DFfusion['measure'] = np.where((DFfusion['taxon_kraken'] == DFfusion['taxon_kaiju']) , 1, np.nan)
DFfusion


# In[11]:


import argparse, os               
import pandas as pd 
def get_full_lineages(otus):

	#### makes the full lineage file (lineages.tsv). Requires ete3 ####

	#Input: list of the otus in the table obtained from the get_otus function
	#Output: makes the full_lineages.tsv file 
    
    from ete3 import NCBITaxa
    ncbi = NCBITaxa()
    
    lineages = {}
    
    print("hello")


# In[13]:


get_full_lineages(5)

#llamar la funcion....




