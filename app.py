import streamlit as st
import pandas as pd
import joblib
model_data = joblib.load(open('whole_data.pkl','rb'))
model = joblib.load(open('model5.pkl', 'rb'))
st.title('Autism Prediction')
model_input_data = model_data .drop('Class/ASD', axis=1)
input_data = []
for column in model_input_data.columns:
    if column == 'age' :
        value=(st.slider(f"Enter value for {column}:", min_value=0, max_value=100, step=1))/100
        if value == 0:
            st.error(f"Please enter a valid value for {column}.")
    elif column == 'gender':
        value = st.selectbox(f"Enter value for {column}:", ['male', 'female'])
        if value == 'male':
            value = 1
        else:
            value = 0
    elif column == 'A1_Score':
        value = st.selectbox("Do you avoid or struggle with eye contact?", ['yes', 'no'])
        if value == 'yes':
            value = 1
        else:
            value = 0
    elif column == 'A2_Score':
        value = st.selectbox("Do you have delayed speech or difficulty in conversations?", ['yes', 'no'])
        if value == 'yes':
            value = 1
        else:
            value = 0
    elif column == 'A3_Score':
        value = st.selectbox("Do you not respond when your name is called?", ['yes', 'no'])
        if value == 'yes':
            value = 1
        else:
            value = 0
    elif column == 'A4_Score':
        value = st.selectbox("Do you show repetitive actions (e.g., hand flapping, lining objects)?", ['yes', 'no'])
        if value == 'yes':
            value = 1
        else:
            value = 0
    elif column == 'A5_Score':
        value = st.selectbox("Are you overly focused on specific interests or objects?", ['yes', 'no'])
        if value == 'yes':
            value = 1
        else:
            value = 0
    elif column == 'A6_Score':
        value = st.selectbox("Do you struggle to understand others’ emotions or facial expressions?", ['yes', 'no'])
        if value == 'yes':
            value = 1
        else:
            value = 0
    elif column == 'A7_Score':
        value = st.selectbox("Are you overly sensitive to sound, light, touch, or textures?", ['yes', 'no'])
        if value == 'yes':
            value = 1
        else:
            value = 0
    elif column == 'A8_Score':
        value = st.selectbox("Do you avoid pretend or imaginative play?", ['yes', 'no'])
        if value == 'yes':
            value = 1
        else:
            value = 0
    elif column == 'A9_Score':
        value = st.selectbox("Do you get upset with changes in routine?", ['yes', 'no'])
        if value == 'yes':
            value = 1
        else:
            value = 0
    elif column == 'A10_Score':
        value = st.selectbox("Do you prefer to play alone and avoid social interaction?", ['yes', 'no'])
        if value == 'yes':
            value = 1
        else:
            value = 0
    else:
        value = st.selectbox(f"are u have  jaundice", ['yes', 'no'])
        if value == 'yes':
            value = 1
        else:
            value = 0
    input_data.append(value)

new_data=pd.DataFrame([input_data],
                      columns=['A1_Score','A2_Score','A3_Score','A4_Score','A5_Score','A6_Score','A7_Score','A8_Score','A9_Score','A10_Score','age','gender','jaundice'])
if st.button('Predict'):
    prediction = model.predict(new_data)
    if prediction[0] == 0:
        st.success("The person does not have autism.")
    else:
        st.error("you is likely to have autism.")
