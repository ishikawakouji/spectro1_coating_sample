import pandas as pd
import streamlit as st
import plotly.express as px

st.title('scatter 3D for car coating')

upfile = st.file_uploader('select file')
if upfile is not None:
  df = pd.read_csv(upfile)
  st.write(df)

