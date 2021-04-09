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
    if Interpretability == 0:
        Int_Descr = "This measure is not applicable"
    elif Interpretability <5:
        Int_Descr = "You will likely need someone to explain this data to you."
    elif Interpretability < 8:
        Int_Descr = "You can understand it with some documentation."
    else:
        Int_Descr = "The data is self explanatory."

                                                         
              

with st.sidebar.beta_expander("Believability", expanded=False):
    st.write("The data is trusted")
    Believability = st.slider('Do you believe in this data?', 0, 10, 1)
    st.text("0 = N/A")
    st.text("1 = No, absolutely not.")
    st.text("5 = Useable but beware.")        
    st.text("10 = I'll bet my house on it.")
    if Believability == 0:
        Bel_Descr = "This measure is not applicable"
    elif Believability <5:
        Bel_Descr = "Useable but understand the gaps."
    elif Believability < 8:
        Bel_Descr = "You can reliable use this data."
    else:
        Bel_Descr = "Complete trust in this data."
    

with st.sidebar.beta_expander("Objectivity", expanded=False):
    st.write("The source of the data is believed to be impartial")
    Objectivity = st.slider('Is this data objective?', 0, 10, 1)
    st.text("0 = N/A")
    st.text("1 = Completely biased data.")
    st.text("5 = Useable but beware.")        
    st.text("10 = Free from any bias.")
    if Objectivity == 0:
        Obj_Descr = "This measure is not applicable"
    elif Objectivity <5:
        Obj_Descr = "Bias in the data."
    elif Objectivity < 8:
        Obj_Descr = "Minimal bias in the data."
    else:
        Obj_Descr = "Compeltely objective."

with st.sidebar.beta_expander("Scarcity", expanded=False):
    st.write("The probability that other organizations also have the same data")
    Scarcity = st.slider('Is this data rare?', 0, 10, 1)
    st.text("0 = N/A")
    st.text("1 = Very common and duplicated data.")
    st.text("5 = Might exist elsewhere.")        
    st.text("10 = This is the only source.")
    if Scarcity == 0:
        Sca_Descr = "This measure is not applicable"
    elif Scarcity <5:
        Sca_Descr = "This data is common and duplicated."
    elif Scarcity < 8:
        Sca_Descr = "Hard to find but there might be others like this."
    else:
        Sca_Descr = "Only copy known in the universe."

with st.sidebar.beta_expander("Multifunctionality", expanded=False):
    st.write("The number of business processes that use or rely from this type of data")
    Multifunctionality = st.slider('Do other business areas rely on this?', 0, 10, 1)
    st.text("0 = N/A")
    st.text("1 = Only we use this data.")
    st.text("5 = A few businesses use this.")        
    st.text("10 = Everyone uses this data.")
    if Multifunctionality == 0:
        Mul_Descr = "This measure is not applicable"
    elif Multifunctionality <5:
        Mul_Descr = "Few if any business relies on this data."
    elif Multifunctionality < 8:
        Mul_Descr = "Many business processes rely on this."
    else:
        Mul_Descr = "Business critical data."
    
with st.sidebar.beta_expander("Usability", expanded=False):
    st.write("The data is helpful in performing a business function")
    Usability = st.slider('How useful is this data to perform business functions?', 0, 10, 1)
    st.text("0 = N/A")
    st.text("1 = Not useful but it's the best we have.")
    st.text("5 = Good enough most of the time.")        
    st.text("10 = Very useful and critical to day to day.")
    if Usability == 0:
        Usa_Descr = "This measure is not applicable"
    elif Usability <5:
        Usa_Descr = "This data has a very narrow purpose."
    elif Usability < 8:
        Usa_Descr = "Other areas might be able to use this."
    else:
        Usa_Descr = "Everyone should find this data useful."
        
Subj_Score = (Interpretability+Believability+Objectivity+Scarcity+Multifunctionality+Usability)/6

#Sujbective Quality Display

st.header("Subjective Data Quality")
st.write("The Overall Subjective Data Quality Score is: ", Subj_Score)
st.write("Subjective Data Quality measures what the users believe to be true. It depends on the user’s prior experience with the data and the task which the data need to solve.")
st.write("Different users looking at the same data set can come to different conclusions on the quality of the data. These are user input solicited scores.")



dfsubjective = pd.DataFrame(np.array([["Interpretability",Interpretability, Int_Descr], ["Believability", Believability, Bel_Descr], ["Objectivity", Objectivity, Obj_Descr], ["Scarcity", Scarcity, Sca_Descr],["Multifunctionality", Multifunctionality, Mul_Descr],["Usability", Usability, Usa_Descr]]),
                   columns=['Measure', 'Score', 'Description'])
st.table(dfsubjective)

#Objective Sidebar


st.sidebar.subheader("Objective Data Quality")


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



#Display Objective


#st.header("Objective Data Quality")
#st.write("Objectve Data Quality measures are rated consistently, irrespective of the end users' perception.") 
#st.write("Different users looking at the same data should come to the same conclusion on the quality of the data. These are programatically calculated scores.")


#dfobjective = pd.DataFrame(np.array([["Completeness",CompletenessScore, "PlaceHolder"], ["Timeliness", Timeliness, Bel_Descr], ["Uniqueness", Objectivity, Obj_Descr], ["Scarcity", Scarcity, Sca_Descr],["Multifunctionality", Multifunctionality, Mul_Descr],["Usability", Usability, Usa_Descr]]),
                   #columns=['Measure', 'Score', 'Description'])
#st.table(dfsubjective)

#Global Numbers
def main():
    TotalRows = len(df.index)
    TotalColumns = len(df.columns)
    #st.markdown(TotalRows)
    #st.markdown(TotalColumns)
    #st.subheader("Completeness")
    

#Completeness
    #st.subheader('Completeness Score')
    Empty = df.isnull().sum()
    PercentageEmpty = (1-Empty/TotalRows)*100
    #st.table(PercentageEmpty)
    OverallEmpty = df.isnull().sum().sum()
    CompletenessScore = (1-(OverallEmpty/(TotalRows*TotalColumns)))*100
    #st.subheader('Overall Completeness Score')
    #st.text(CompletenessScore)
    
#Timeliness
   # st.subheader("Timeliness")
    #st.subheader(Timeliness)
      
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


#Display Objective


    st.header("Objective Data Quality")
    st.write("Objectve Data Quality measures are rated consistently, irrespective of the end user's perception.") 
    st.write("Different users looking at the same data should come to the same conclusion on the quality of the data. These are programatically calculated scores.")


    dfobjective = pd.DataFrame(np.array([["Completeness",CompletenessScore, "PlaceHolder"], ["Timeliness", Timeliness, "Place"], ["Uniqueness", UniquenessScore, "PlaceHolder"]]),
                    columns=['Measure', 'Score', 'Description'])
    st.table(dfobjective)
    
    st.subheader('Completeness')
    st.write("All data entry fields must be complete and data sets should not be missing any important fields or data.")
    st.write("The Overall Completness Score is:", CompletenessScore)
    st.write("The Completeness Score per column is:", PercentageEmpty)
    
    st.subheader("Timeliness")
    st.write("Time between the last refresh date to the next refresh date. The 'freshness' of the data.")
    st.write(LastRefresh, date.today(), NextRefresh)
    st.write("The Timeliness Score is : ", Timeliness)
    
    
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
