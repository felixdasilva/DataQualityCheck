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
      st.text("Are any of the following columns related to each other?")
      CorrTable = df.corr().abs()
      #st.text(CorrTable)
      s = CorrTable.unstack()
      so = s.sort_values(kind="quicksort")
      so = so[0:5]
      st.text(so)
      st.text(so.shape)
      st.multiselect('Which ones?',so,default=None)
      #Column1 = st.selectbox('Select column 1', df.columns)
      #st.text(Column1)
      #Column1 = Column1.cat.codes
      #Column2 = st.selectbox('Select column 2', df.columns)
      #st.text(Column2)
      #Consistency = df[Column1].corr(df[Column2])
      #st.text(Consistency)
      
#the page

if __name__ == '__main__':
  main()
