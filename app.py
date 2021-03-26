#importing all the packages

import pandas as pd
import streamlit as st
import openpyxl
import numpy as np
from datetime import date
import re

#Regex Types
Emailregex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

st.header("Objective Data Quality Score Calculator")

#Timeliness
with st.sidebar.beta_expander("Timeliness", expanded=False):
  st.sidebar.subheader("Timeliness")
  LastRefresh=st.sidebar.date_input('Last Refresh Date')
  NextRefresh=st.sidebar.date_input('Next Refresh Date')
#st.write(date.today())
  Numerator = date.today() - LastRefresh
  Numerator = Numerator.days
  Denominator = NextRefresh - LastRefresh
  Denominator = Denominator.days


if Denominator !=0:
  Timeliness = (1-Numerator/Denominator)*100
else:
  Timeliness = 0
st.subheader(Timeliness)
#st.subheader(Timeliness)


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
      st.markdown('No. of Rows', TotalRows)
      st.markdown('No. of Columns', TotalColumns)
      
      st.subheader("Completeness")
#Completeness
      st.subheader('Completeness Score')
      Empty = df.isnull().sum()
      PercentageEmpty = (1-Empty/TotalRows)*100
      st.text(PercentageEmpty)
      OverallEmpty = df.isnull().sum().sum()
      CompletenessScore = (1-(OverallEmpty/(TotalRows*TotalColumns)))*100
      st.subheader('Overall Completeness Score')
      st.text(CompletenessScore)
      
#Uniqueness
 #Add option for user to ignore / select columns
  
      Uniqueness = len(df.drop_duplicates())
      UniquenessScore = Uniqueness / TotalRows
      st.subheader('Uniqueness Score')
      st.text(UniquenessScore)

#Validity
      st.subheader("Validity")
      v1 = st.selectbox('Select the column you want to check', df.columns)
      regexcheck = st.selectbox('What validation would you like to apply?', 'Email')
      #x = re.search(Emailregex, v1)
      #if x:
        #print("YES! We have a match!")
     # else:
      #  print("No match")
      #count = 0
      #while True:
          #match = re.search(Emailregex, v1)
          #count += 1
      #st.write(count)

    
    
#consistency
      
      #st.subheader("Consistency")
      #st.text(df.dtypes)
      #df.loc[:, df.dtypes == 'object'] = df.select_dtypes(['object']).apply(lambda x: x.astype('category'))
      #st.text(df.dtypes)
      #c1 = st.selectbox('Select column 1', df.columns)
      #c1 = df[c1]
      #c2 = st.selectbox('Select column 2', df.columns)
      #c2 = df[c2]
      #Consistency = abs(c1.corr(c2))
      #Consistency = df.apply(lambda x : pd.factorize(x)[0]).corr(method='pearson', min_periods=1)
      #st.table(Consistency)
  
      
#the page

if __name__ == '__main__':
  main()
