from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config( layout="centered")
st.title('KNN Classification - Iris Dataset')
st.header('น้องกิตตฺศักดิ์เองครับ')

st.image("./img/1704165478897.jpg")


col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Versicolor")
    st.image("./img/iris1.jpg")

with col2:
    st.subheader("Virginica")
    st.image("./img/iris2.jpg")

with col3:
    st.subheader("Setosa")
    st.image("./img/iris3.jpg")


