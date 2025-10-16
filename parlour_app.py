import streamlit as st
import pickle
import numpy as np
import pandas as pd
model = pickle.load(open("parlour_model.pkl","rb"))
st.header("Nidhi's Beauty Parlour")


st.set_page_config( layout="wide")
Service = st.sidebar.selectbox("Services", ["Home","Haircut", "Eyebrow", "Facial", "Makeup","Contact Us"])
if Service == "Home":
   
    st.subheader("Turn Your Face and Mind Glorious")
    st.image("parlour.jpg")
    st.write("""
    Nidhis Beauty Parlour Provide Best Service in Best Rate as  Well
    """)
    st.header("Content List")
    data = {
    "Service": ["Facial", "Eyebrow", "Makeup","Haircut"],
    "A":["Golden Facial","Simple Eyebrow","Simple Makeup","Simple Haircut"],
    "B":["Silver Facial","with point Eyebrow","Bridal Makeup","Three step"],
    "Price": [50, 30, 200,500],
   
}

# Create a DataFrame
    df = pd.DataFrame(data)

# Display as table
    st.table(df)   

    st.success("Book your Services today and get 10% off on your first booking!")
elif Service == "Haircut":
    st.subheader("Hair's Section")
    col1,col2 = st.columns(2)
    with col1:
        st.image("curly.jpg")
        st.write("""Curly Haircut """)
        st.success(" Curly Haircut Charge : Rs..250")
    with col2:
        st.image("long.webp")

elif Service == "Eyebrow":
    st.header("Eyebrow Section")
    st.write(""" Nidhi's Beauty Parlour Focuses  on  shape, size, color, texture, symmetry, grooming, and emotional expression of your eyes.""")

    col1,col2= st.columns(2)
    with col1:
        st.image("thick.webp")
        st.write("Thick Eyebrow")
        st.success("Price Rs..60")
    with col2:
        st.image("Thin.webp",width=390)
        st.write("Thin Eyebrow")
        st.success("Price Rs..100") 
   
elif Service == "Facial":
   elif Service == "Facial":
    st.header("Facial Section")
    col1,col2 = st.columns(2)
    with col1:
        st.image("Facial1.jpg")
        st.success("Price Rs..200")
    with col2:
        st.image("Facial2.jpg")
        st.success("Price Rs 500")

elif Service == "Makeup":
    st.header("Makeup Section")
    col1,col2 = st.columns(2)
    with col1:
        st.image("spa.webp")
        st.success("Price Rs...200")
    with col2:
        st.image("plain.jpg",width=300)
        st.success("Price Rs...300")
elif Service == "Contact Us":
    st.header("📞 Contact Us")
    st.write("""
    **Nidhi's Beauty Parlour**  """)
    st.write("📍 Bedi nagar ,Jabalpur Mp ")
    st.write("📧 nidhisparlour@gmail.com")
    st.write("☎️ +91 7999566956")
    
    
    st.info("We are open 24/7 for your service!")















Haircut = st.number_input("Enter the price of Haircut",min_value=100)
Facial = st.number_input("Enter the price of Facial",min_value=100)
Makeup = st.number_input("Enter the price of Makeup",min_value=100)
Eyebrows = st.number_input("Enter the price of Eyebrows",min_value=100)
if st.button("Predict"):
    features =np.array([[Haircut,Facial,Makeup,Eyebrows]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Price:Rs... {prediction:,.2f}")

