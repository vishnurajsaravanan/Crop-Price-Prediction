import streamlit as st
from RF_predict import *
st.title('Crop Yield Prediction')


with st.form("my_form"):
   st.write("Inside the form")
   crop = st.selectbox('Select District', dist_list)
   dist = st.selectbox('Select Crop', crop_list)
   area = st.number_input('Enter area')
   soil = st.selectbox('Select soil type', soil_list)
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
        pred = "The predicted YIELD for given attributes is approximately:  " + str(pred(crop,dist,area,soil)) + " tons"
        st.write(pred)


# d = pred()