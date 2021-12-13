import pandas as pd
import streamlit as st
import plotly.express as px

st.title('scatter 3D for car coating')

upfile = st.file_uploader('select file')
if upfile is not None:
  df = pd.read_csv(upfile)
  print('setting')
  fig = px.scatter_3d(df, x='A-2deg-L', y='A-2deg-a', z='A-2deg-b', color='part')
  print('show')
  st.plotly_chart(fig, use_container_width=True)
