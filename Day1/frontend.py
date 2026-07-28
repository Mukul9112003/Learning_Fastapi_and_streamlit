import requests
import streamlit as st
st.title("My First app")
st.header("I am Mukul Mehta ")
st.subheader("I am very happy to share with you that i am going to make my first step to my future")
st.text("Feeling good ")
response=requests.get("http://localhost:8000")
st.write(response.status_code)
st.write(response.content)
st.write("Response:", response.json())
st.markdown("### My backend code")
st.markdown("**good to start**")
st.markdown("**good**")
c='''from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def show():
    return {
        "message":"This is my first fastapi "
    }
'''
st.code(c,language="python")
