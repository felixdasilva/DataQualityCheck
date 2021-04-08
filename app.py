#importing all the packages

import pandas as pd
import streamlit as st
import openpyxl
import numpy as np
from datetime import date
import re

#configs
st.set_page_config(layout="centered")
st.sidebar.title("Data Quality Score Tool")
ReportTitle=st.sidebar.text_input('What is the dataset name?') + " Data Quality Scorecard"
#ReportTitle = ReportTitle + " Data Quality Scorecard"
st.title(ReportTitle)
df = pd.DataFrame([1,1])

#Regex Types
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")



#Subjective data Quality
st.sidebar.subheader("Subjective Data Quality")
with st.sidebar.beta_expander("Interpretability", expanded=False):
    st.write("The data has a meaning and is easy to understand")
    Interpretability = st.slider('How easy is your dataset is to understand?', 0, 10, 1)
    st.text("0 = N/A")
    st.text("1 = Needs to be explained by expert")
    st.text("5 = Needs documentation to understand")        
    st.text("10 = Complete understanding")
If Interpretability = 0:
    Int_Descr = "No"
    Else:
        "Yes"

                                                         
              

with st.sidebar.beta_expander("Believability", expanded=False):
    st.write("The data is trusted")
    Believability = st.slider('Do you believe in this data?', 0, 10, 1)
    st.text("0 = N/A")
    st.text("1 = No, absolutely not.")
    st.text("5 = Useable but beware.")        
    st.text("10 = I'll bet my house on it.")
    

with st.sidebar.beta_expander("Objectivity", expanded=False):
    st.write("The source of the data is believed to be impartial")
    Objectivity = st.slider('Is this data objective?', 0, 10, 1)
    st.text("0 = N/A")
    st.text("1 = Completely biased data.")
    st.text("5 = Useable but beware.")        
    st.text("10 = Free from any bias.")

with st.sidebar.beta_expander("Scarcity", expanded=False):
    st.write("The probability that other organizations also have the same data")
    Scarcity = st.slider('Is this data rare?', 0, 10, 1)
    st.text("0 = N/A")
    st.text("1 = Very common and duplicated data.")
    st.text("5 = Might exist elsewhere.")        
    st.text("10 = This is the only source.")

with st.sidebar.beta_expander("Multifunctionality", expanded=False):
    st.write("The number of business processes that use or rely from this type of data")
    Multifunctionality = st.slider('Do other business areas rely on this?', 0, 10, 1)
    st.text("0 = N/A")
    st.text("1 = Only we use this data.")
    st.text("5 = A few businesses use this.")        
    st.text("10 = Everyone uses this data.")
    
with st.sidebar.beta_expander("Usability", expanded=False):
    st.write("The data is helpful in performing a business function")
    Multifunctionality = st.slider('How useful is this data to perform business functions?', 0, 10, 1)
    st.text("0 = N/A")
    st.text("1 = Not useful but it's the best we have.")
    st.text("5 = Good enough most of the time.")        
    st.text("10 = Very useful and critical to day to day.")

#Sujbective Quality Display

st.subheader("Subjective Data Quality Scores")
st.write("Subjectve Data Quality Scores measures what the users beleive to be true about the data. These are non programmatically measured scores.")



dfsubjective = pd.DataFrame(np.array([["Interpretability",Interpretability, Int_Descr], ["Believability", Believability, 6], ["Objectivity", Objectivity, 9]]),
                   columns=['Measure', 'Score', 'Description'])
st.table(dfsubjective)

col1, col2, col3 = st.beta_columns(3)
with col1:
    st.markdown('**Interpretability**')
    st.subheader(Interpretability)
with col2:
    st.markdown('**Believability**')
    st.subheader(Believability)
with col3:
    st.markdown('**Objectivity**')
    st.subheader(Objectivity)    





st.sidebar.subheader("Objective Data Quality")

#Importing and reading the file
st.write('Upload your file to calculate your scores.')

#Step 1: Upload File
with st.sidebar.beta_expander("1. Upload your dataset (or a sample)", expanded=False):
    data_file = st.file_uploader("Upload CSV or XLSX File",type=['csv','xlsx'])
    if data_file is not None:
        try:
            df = pd.read_csv(data_file)
        except:
            df = pd.read_excel(data_file, engine='openpyxl')
            
#step 2: Refresh Time
with st.sidebar.beta_expander("2. Provide Refresh Dates", expanded=False):
    LastRefresh=st.date_input('Last Refresh Date')
    NextRefresh=st.date_input('Next Refresh Date')
    Numerator = date.today() - LastRefresh
    Numerator = Numerator.days
    Denominator = NextRefresh - LastRefresh
    Denominator = Denominator.days
    if Denominator !=0:
        Timeliness = (1-Numerator/Denominator)*100
    else:
        Timeliness = 0


#Step 3: Select Unique Columns
with st.sidebar.beta_expander("3. Select Unique Columns", expanded=False):
    Columns_Selected = st.multiselect('Select Unique Columns', df.columns)

#Step 4: Select Unique Columns
with st.sidebar.beta_expander("4. Apply Validation Rules", expanded=False):
    emails_selected = st.selectbox('Select an Email Column', df.columns)

#Timeliness
#with st.sidebar.beta_expander("Timeliness", expanded=False):
    #st.sidebar.subheader("Timeliness")
    #LastRefresh=st.date_input('Last Refresh Date')
    #NextRefresh=st.date_input('Next Refresh Date')
#st.write(date.today())






st.subheader("Objective Data Quality")

#Importing and reading the file
#def main():
  #data_file = st.file_uploader("Upload CSV or Excel File",type=['csv','xlsx'])
  
  #if data_file is not None:
    #try:
      #df = pd.read_csv(data_file)
    #except:
      #df = pd.read_excel(data_file, engine='openpyxl')
      
      #st.subheader("About Your Data")
      
#Global Numbers
def main():
    TotalRows = len(df.index)
    TotalColumns = len(df.columns)
    st.markdown(TotalRows)
    st.markdown(TotalColumns)
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
    
#Timeliness
    st.subheader("Timeliness")
    st.subheader(Timeliness)
      
#Uniqueness
 #Add option for user to ignore / select columns
  
    Uniqueness = len(df.drop_duplicates())
    UniquenessScore = Uniqueness / TotalRows
    st.subheader('Uniqueness Score')
    st.text(UniquenessScore)
    st.markdown('**Column Uniqueness Score**')
    st.text(Columns_Selected)
    for column in df[Columns_Selected]:
        Column_Unique = len(df[column])-len(df[column].drop_duplicates())
        st.write(column)
        st.write('No of duplicates:',Column_Unique)
        column_unique_score = ((TotalRows-Column_Unique)/TotalRows)*100
        st.write('Column Unique Score:', column_unique_score)

#Validity
    st.subheader("Validity")
    df['Email_Column'] = df[emails_selected].astype(str)
    df['isemail'] = df['Email_Column'].apply(lambda x: True if pattern.match(x) else False)
    st.table(df[['Email_Column','isemail']])

     # st.subheader("Validity")
      #v1 = st.selectbox('Select the column you want to check', df.columns)
      #regexcheck = st.selectbox('What validation would you like to apply?', 'Email')
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
