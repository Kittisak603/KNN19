from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------
# ตั้งค่าหน้าตาแอป
# ---------------------------
st.set_page_config(
    page_title="KNN - Iris Classification",
    page_icon="🌸",
    layout="centered"
)

# ---------------------------
# หาตำแหน่งไฟล์รูปแบบไม่หลงทาง
# ---------------------------
BASE = os.path.dirname(__file__)

# ---------------------------
# Title & Header
# ---------------------------
st.markdown(
    "<h1 style='text-align:center; color:#7b2cbf;'>KNN Classification - Iris Dataset</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center; color:#ff6f61;'>น้องกิตติศักดิ์ เองครับ 👋</h3>",
    unsafe_allow_html=True
)

# ---------------------------
# แสดงรูปโปรไฟล์กลางหน้า
# ---------------------------
st.image(
    os.path.join(BASE, "img/1704165478897.jpg"),
    use_column_width=True
)

st.markdown(
    "<hr style='border: 1px solid #ccc;'>",
    unsafe_allow_html=True
)

# ---------------------------
# แสดงรูปทั้ง 3 แบบ
# ---------------------------
st.markdown(
    "<h3 style='text-align:center; color:#2979ff;'>ประเภทดอก Iris ทั้ง 3 แบบ</h3>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🌿 Versicolor")
    st.image(os.path.join(BASE, "img/iris1.jpg"))

with col2:
    st.subheader("🌸 Virginica")
    st.image(os.path.join(BASE, "img/iris2.jpg"))

with col3:
    st.subheader("🌼 Setosa")
    st.image(os.path.join(BASE, "img/iris3.jpg"))

st.markdown(
    "<hr style='border: 1px solid #ccc;'>",
    unsafe_allow_html=True
)

st.success("✨ หน้านี้พร้อมใช้งานแล้ว สามารถเพิ่มฟังก์ชันทำนาย KNN ต่อได้เลย")

