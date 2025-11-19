from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

st.title('KNN Classification - Iris Dataset')
st.header('น้องกิตติศักดิ์ เองครับ')

# ใช้ os เพื่อป้องกันปัญหา path ไม่เจอ
BASE = os.path.dirname(__file__)

# รูปหลัก
st.image(os.path.join(BASE, "img/1704165478897.jpg"))

# แสดงรูป 3 แบบใน 3 คอลัมน์
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Versicolor")
    st.image(os.path.join(BASE, "img/iris1.jpg"))

with col2:
    st.subheader("Virginica")
    st.image(os.path.join(BASE, "img/iris2.jpg"))

with col3:
    st.subheader("Setosa")
    st.image(os.path.join(BASE, "img/iris3.jpg"))

