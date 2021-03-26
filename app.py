#importing all the packages

import pandas as pd
import streamlit as st
import openpyxl
import numpy as np
from datetime import date
import re

st.header("Objective Data Quality Score Calculator")

#Timeliness
st.subheader("Timeliness Score")
LastRefresh=st.date_input('Last Refresh Date')
NextRefresh=st.date_input('Next Refresh Date')
st.write(date.today())
Numerator = date.today() - LastRefresh
Numerator = Numerator.days
Denominator = NextRefresh - LastRefresh
Denominator = Denominator.days

Timeliness = (1-Numerator/Denominator)*100
st.write(Timeliness)


st.subheader("Objective Data Quality")

#Importing and reading the file
def main():
  data_file = st.file_uploader("Upload CSV or Excel File",type=['csv','xlsx'])
  
  if data_file is not None:
    try:
      df = pd.read_csv(data_file)
    except:
      df = pd.read_excel(data_file, engine='openpyxl')
      
st.subheader("About Your Data")
      
#Global Numbers
      TotalRows = len(df.index)
      TotalColumns = len(df.columns)
      st.markdown('# of Rows', TotalRows)
      st.markdown('# of Columns',TotalColumns)
      
#Completeness
      Empty = df.isnull().sum()
      PercentageEmpty = Empty/TotalRows
      st.text(PercentageEmpty)
      OverallEmpty = df.isnull().sum().sum()
      CompletenessScore = (OverallEmpty/(TotalRows*TotalColumns))
      st.subheader('Completeness Score')
      st.text(CompletenessScore)
      
#Uniqueness
 #Add option for user to ignore / select columns
  
      Uniqueness = len(df.drop_duplicates())
      UniquenessScore = Uniqueness / TotalRows
      st.subheader('Uniqueness Score')
      st.text(UniquenessScore)

#Validity

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
