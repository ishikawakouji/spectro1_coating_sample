import pandas as pd
import streamlit as st
import plotly.express as px

st.title('scatter 3D for car coating')

upfile = st.file_uploader('select file')
if upfile is not None:
  df = pd.read_csv(upfile)
  st.write(df)

fig = px.scatter_3d(df, x='A-2deg-L', y='A-2deg-a', z='A-2deg-b', color='part')
fig.show()
