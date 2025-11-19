from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('KNN Classification - Iris Dataset')
st.header('Kittisak')

# แสดงรูปหลัก
st.image("./img/1704165478897.jpg")

# แสดงรูปทั้ง 3 แบบ แบ่งเป็นคอลัมน์
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
