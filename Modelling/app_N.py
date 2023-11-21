%%writefile app.py

import pickle
import streamlit as st

pickle_in = open('GBDT_MODEL.pkl', 'rb')
model = pickle.load(pickle_in)

def predict_close_price(Year, Month, Day, StockName, Positive, Negative, Neutral, TotalTweets):
    
    prediction = model.predict([[Year, Month, Day, StockName, Positive, Negative, Neutral, TotalTweets]])
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
    
    Year = st.text_input('Year', 'type here')
    Month = st.text_input('Month', 'type here')
    Day = st.text_input('Day', 'type here')
    StockName = st.text_input('StockName', 'type here')
    Positive = st.text_input('Positive', 'type here')
    Negative = st.text_input('Negative', 'type here')
    Neutral = st.text_input('Neutral', 'type here')
    Total_Tweets = st.text_input('Total Tweets', 'type here')
    
    result =""
    
    # when predict button is clicked, make predictions and store it
    
    if st.button('PREDICT CLOSE PRICE'):
        result = predict_close_price(Year, Month, Day, StockName, Positive, Negative, Neutral, TotalTweets)
    
    st.success('the predicted price is {}'.format(result))
    
    if st.button('ABOUT'):
        st.text('Predicting Volatility in Equity Markets Using Macroeconomic News (Twitter)')
        

if __name__ == '__main__':
    main()