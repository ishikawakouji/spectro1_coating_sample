import pandas as pd
import streamlit as st
import plotly.figure_factory as ff

st.title('scatter 3D for car coating')

upfile = st.file_uploader('select file')
if upfile is not None:
  df = pd.read_csv(upfile)
  st.write(df)

fig = ff.create_scatterplotmatrix(df, index=['A-2deg-L', 'A-2deg-a', 'A-2deg-b'])
st.plotly_chart(fig, use_container_width=True)
