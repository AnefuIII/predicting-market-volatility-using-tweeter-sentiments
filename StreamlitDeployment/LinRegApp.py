# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 23:52:28 2021

@author: ANEFU PETER
"""


import pickle
import streamlit as st
import pandas as pd
import numpy as np
import math 

from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
import streamlit as st



pickle_in = open('LinReg.pkl', 'rb')
model = pickle.load(pickle_in)

#Year	Month	Day	StockName	Positive	Negative	Neutral	Total Tweets	Volume	Open	High	Low	Day_of_week
def predict_close_price(Year, Month, Day, StockName, Positive, Negative, Neutral, TotalTweets,
                        Volume, Open, High, Low, Day_of_week):
    
    # input options for slider
    #'STOCKNAME:0 for apple, 1 for microsoft, 2 for Nvidia, 3 for paypal, 4 for tesla'
    
    if StockName == 'apple':
        StockName = 0
    elif StockName == 'microsoft':
        StockName = 1
    elif StockName == 'nvidia':
        StockName = 2
    elif StockName == 'paypal':
        StockName = 3
    elif StockName == 'tesla':
        StockName = 4
    else:
        print()
        
        
    #Day of week
    #Day of week:0: friday, 1: monday, 2: saturday, 3 for sunday,4: thursday, 5: tuesday, 6 for wednesday
    if Day_of_week == 'sunday':
        Day_of_week = 4
    elif Day_of_week == 'monday':
        Day_of_week = 1
    elif Day_of_week == 'tueday':
        Day_of_week = 5
    elif Day_of_week == 'wednesday':
        Day_of_week = 6
    elif Day_of_week == 'thursday':
        Day_of_week = 4
    elif Day_of_week == 'friday':
        Day_of_week = 0
    elif Day_of_week == 'saturday':
        Day_of_week = 2
    else:
        print()
        
    #prediction
    prediction = model.predict([[Year, Month, Day, StockName, Positive, Negative, Neutral, TotalTweets,
                                 Volume, Open, High, Low, Day_of_week]])
    print(prediction)
    return prediction


def main():
    
    st.title('GROUP D')
    
    html_temp = """
    
    <div style = "background-color:blue;padding:10px">
    <h2 style = "color:white;text-align:center;">VOLATILITY USING MACROHEADLINES APP</h2>
    </div>
    
    """
    
    st.markdown(html_temp, unsafe_allow_html = True)
    
    #Year	Month	Day	StockName	Positive	Negative	Neutral	Total Tweets
    
    Year = st.number_input('Year', min_value=2019, max_value=2099, step = 1)
    Month = st.number_input('Month', min_value=1, max_value=12, step = 1)
    Day = st.number_input('Day',min_value=1, max_value=31, step = 1)
    #st.write('STOCKNAME:0 for apple, 1 for microsoft, 2 for Nvidia, 3 for paypal, 4 for tesla')
    #StockName = st.number_input('StockName', min_value=0, max_value=4, step = 1)
    StockName = st.selectbox('StockName',('apple', 'microsoft', 'nvidia', 'paypal', 'tesla'))
    Positive = st.text_input('Positive')#, min_value=0, max_value=50, step = 1
    Negative = st.text_input('Negative')#, min_value=0, max_value=50, step = 1
    Neutral = st.text_input('Neutral')#, min_value=0, max_value=50, step = 1
    TotalTweets = st.text_input('Total Tweets')#, min_value=0, max_value=150, step = 1
    
    
    #Volume = st.text_input('Volume', min_value=1, max_value=150, step = 1)
    #Open = st.text_input('Open', min_value=1, max_value=150, step = 1)
    #High = st.text_input('High', min_value=1, max_value=150, step = 1)
    #Low = st.text_input('Low', min_value=1, max_value=150, step = 1)
    #Day_of_week = st.text_input('Day_of_week', min_value=1, max_value=150, step = 1)
    
    Volume = st.text_input('Volume value')
    Open = st.text_input('Open value')
    High = st.text_input('High value')
    Low = st.text_input('Low value')
    #st.write('Day of week:0: friday, 1: monday, 2: saturday, 3 for sunday,4: thursday, 5: tuesday, 6 for wednesday')
    #Day_of_week = st.text_input('Day_of_week', 'value')
    Day_of_week = st.selectbox('Day of week', ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'))
    
    result =""
    
    # when predict button is clicked, make predictions and store it
    
    if st.button('PREDICT CLOSE PRICE'):
        result = predict_close_price(Year, Month, Day, StockName, Positive, Negative, Neutral, TotalTweets,
                                     Volume, Open, High, Low, Day_of_week)
    
    st.success('the predicted price is {}'.format(result))
    
    if st.button('ABOUT'):
        st.text('Predicting Volatility in Equity Markets Using Macroeconomic News (Twitter)')
        
        
if __name__ == '__main__':
    main()
        

