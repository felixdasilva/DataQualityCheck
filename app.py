import pandas as pd
import streamlit as st

#The component
def main():
  #st.header("Data Quality Profling Tool")
  data_file = st.file_uploader("Upload CSV or Excel File",type=['csv','xlsx'])
  
  if data_file is not None:
    try:
      df = pd.read_csv(data_file)
    except:
      df = pd.read_excel(data_file, engine='openpyxl')
      
#the page

if __name__ == '__main__':
  main()
