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
      TotalRows = Len(df)
      
#Completeness
      st.text(TotalRows)
      Empty = df.isnull().sum()
      st.text(Empty)
  
      
#the page

if __name__ == '__main__':
  main()
