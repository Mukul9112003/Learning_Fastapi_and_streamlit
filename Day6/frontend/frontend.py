import streamlit as st
import requests
st.title("Patient ")
st.header("hospital ")
st.image("https://cdn.pixabay.com/photo/2025/02/04/23/03/fish-9382908_1280.jpg")
st.video("https://www.bing.com/videos/riverview/relatedvideo?q=code+with+harry+webdev&mid=9DF4B5D3EF6C933AF5679DF4B5D3EF6C933AF567&churl=https%3a%2f%2fwww.youtube.com%2fchannel%2fUCeVMnSShP_Iviwkknt83cww&FORM=VIRE")
if st.button("create_patient"):
    age=st.number_input("Enter your age")
    name=st.text_input("Enter your name")
    photo=st.camera_input("Enter photo")
    data={
        "name":name,
        "age":age
    }
    response=requests.post("127.0.0.1/create_patient:54812",json=data)