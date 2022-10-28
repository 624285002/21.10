import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.header("Kittitorn")
st.subheader("Chantana")

html_8="""
<div style="background-color:#EE9513;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>เกณฑ์การให้คะแนน 4</h5></center>
</div>
"""
st.markdown(html_8,unsafe_allow_html=True)
st.markdown("")
dx=pd.read_excel('./data/gen.xlsx')
st.dataframe(dx)

dz=pd.read_csv('./data/iris.csv')
st.dataframe(dz)

dy=dz.head(10)
st.bar_chart(dy)
st.balloons()

st.sidebar.markdown("# วิเคราห์รายบุคคล")
