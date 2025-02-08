import streamlit as st
import pickle 
import pandas as pd

st.title('Advertising Sales Predictior')
#st displays all we want
st.write('This web app predicts the revenue an advertising campaign will generate based on TV, Radio, and Newspaper budgets. Adjust your strategy to maximize your ROI!.')

#to read the model from the pickle file
with open('model_lr_ad_c0922989.pkl', 'rb') as file:
    model_cp = pickle.load(file)

#get the input from the users
st.write('Enter your advertising budget (in $1000s)')
tv_value=st.number_input('**TV Advertising Budget:**')
radio_value=st.number_input('**Radio Advertising Budget:**')
newspaper_value=st.number_input('**Newspaper Advertising Budget:**')


#with this code we can request the input but we need to convert those inputs into dataframes
#to do that we would need to use pandas
#convert the user input to a dataframe
ad_data=pd.DataFrame({'TV':tv_value, 'Radio':radio_value, 'Newspaper':newspaper_value},index=[0])
#Keys should be the same as column names and also the sequence should be the same

#Predict the house price
prediction=model_cp.predict(ad_data)

#display the result
if st.button('Predict'):
    formatted_prediction = f"${prediction[0]:,.2f}"
    st.write(f'The predicted sales value is {formatted_prediction}')


st.write('**Insights:**' )
st.write('- TV has the strongest correlation with sales. ') 
st.write('- Radio is cost-effective with a notable impact.')  
st.write('- Newspaper ads have minimal influence on sales.')