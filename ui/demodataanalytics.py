import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
#import dtale as dt


@st.cache
def load_dataset():
    df = pd.read_excel(r'E:\360digit\Canada.xlsx',
            sheet_name='Canada by Citizenship',
            skiprows=20,
            skipfooter=2)
    return preprocess(df)

def preprocess(df):
    #step1 drop columns 
    cols_to_drop = ['Type','Coverage','AREA','REG','DEV']
    df.drop(columns=cols_to_drop, inplace=True)

    #step2 rename columns
    df.rename({
    'OdName': 'Country',
    'AreaName': 'Continent',
    'RegName': 'Region',
    'DevName': 'Status',
    }, axis=1, inplace=True)

    #step3 col as string 
    df.columns=df.columns.astype(str)

    #step4 add a total column
    years = list(map(str,range(1980,2014)))
    df['Total'] = df[years].sum(axis=1)

    #step5 set country as index
    df.set_index('Country', inplace=True)
    return df 

#loading the data

canadadf=load_dataset()

st.header("Canada immigration data analysis of 30 years")

if st.checkbox("View raw dataset"):   #this line adds a option on view 
    st.write(canadadf)

menu_choices=["Visualize country Immigrants","compare countries",'About']
choice=st.sidebar.radio("Slect an option from the menu",menu_choices)
years=list(map(str,range(1980,2014)))
if choice== menu_choices[0]:
    country_list=canadadf.index.tolist()
    country=st.selectbox('select a country',country_list)
    graph= st.radio('select a graph',['Bar chart','Line chart','Area chart'],horizontal=True)
    
    data=canadadf.loc[country,years]
    if graph == "Bar chart":
        st.bar_chart(data)
    elif graph == "Line chart":
        st.line_chart(data)
    elif graph== "Area chart":
        st.area_chart(data)
    
elif choice== menu_choices[1]:
    country_list=canadadf.index.tolist()
    countries=st.multiselect('select a country',country_list)
    graph= st.radio('select a graph',['Bar chart','Line chart','Area chart'],horizontal=True)
    data=canadadf.loc[countries,years].T
    if not len(countries)>=1:
        st.warning("error")
    elif graph=="Bar chart":
        fig=px.bar(data,x=years,y=countries)
        st.plotly_chart(fig)
    elif graph== "Line chart":
        fig=px.line(data,x=years,y=countries,title="Comparing Countries ")
        st.plotly_chart(fig)
    elif graph=="Area chart":
        fig=px.area(data,x=years,y=countries)
        st.plotly_chart(fig)

    
else:
    st.header("About")
    st.markdown('''
    ###this is a data data analysis app for Canada
    - this data is from United Nations 
    - its from the year 1980 to 2013
    - it contain data of 195 countries
    ''' )

