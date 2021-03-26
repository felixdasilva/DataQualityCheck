#importing all the packages

import pandas as pd
import streamlit as st
import openpyxl
import numpy as np
from datetime import datetime

#Timeliness
st.header("Official Date Picker")
LastRefresh=st.date_input('Last Refresh Date')
NextRefresh=st.date_input('Next Refresh Date')
st.write(date.today()) 


#Importing and reading the file
def main():
  data_file = st.file_uploader("Upload CSV or Excel File",type=['csv','xlsx'])
  
  if data_file is not None:
    try:
      df = pd.read_csv(data_file)
    except:
      df = pd.read_excel(data_file, engine='openpyxl')
      
#Global Numbers
      TotalRows = len(df.index)
      TotalColumns = len(df.columns)
      
#Completeness
      st.text(TotalRows)
      st.text(TotalColumns)
      Empty = df.isnull().sum()
      PercentageEmpty = Empty/TotalRows
      st.text(PercentageEmpty)
      OverallEmpty = df.isnull().sum().sum()
      CompletenessScore = (OverallEmpty/(TotalRows*TotalColumns))
      st.subheader('Completeness Score')
      st.text(CompletenessScore)
      
#Uniqueness
     
      Uniqueness = len(df.drop_duplicates())
      UniquenessScore = Uniqueness / TotalRows
      st.subheader('Uniqueness Score')
      st.text(UniquenessScore)

#consistency
      
      st.subheader("Consistency")
      st.text(df.dtypes)
      df.loc[:, df.dtypes == 'object'] = df.select_dtypes(['object']).apply(lambda x: x.astype('category'))
      st.text(df.dtypes)
      c1 = st.selectbox('Select column 1', df.columns)
      c1 = df[c1]
      c2 = st.selectbox('Select column 2', df.columns)
      c2 = df[c2]
      #Consistency = abs(c1.corr(c2))
      Consistency = df.apply(lambda x : pd.factorize(x)[0]).corr(method='pearson', min_periods=1)
      st.table(Consistency)
  
      
#the page

if __name__ == '__main__':
  main()
