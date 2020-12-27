#importing all the packages

import pandas as pd
import streamlit as st
import openpyxl

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
      OverallPercentageEmpty = (OverallEmpty/(TotalRows*TotalColumns))
      st.text(OverallPercentageEmpty)
  
      
#the page

if __name__ == '__main__':
  main()
