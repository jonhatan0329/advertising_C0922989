import streamlit as st
import pickle 
import pandas as pd

st.title('Advertising Sales Prediction')
#st displays all we want
st.write('This web app predicts **Sales Revenue** generated after the deployment of an advertising campaing.')

#to read the model from the pickle file
with open('model_lr_ad_c0922989.pkl', 'rb') as file:
    model_cp = pickle.load(file)

#get the input from the users
tv_value=st.number_input('**TV**')
radio_value=st.number_input('**Radio**')
newspaper_value=st.number_input('**Newspaper**')


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