import pandas as pd
import streamlit as st
import plotly.express as px

st.title('scatter 3D for car coating')

labelhead = 'A-2deg'

xl = labelhead + '-L'
yl = labelhead + '-a'
zl = labelhead + '-b'

def plot_plotly(df):
  st.write(labelhead)
  fig = px.scatter_3d(df, x=xl, y=yl, z=zl, color='part')
  st.plotly_chart(fig, use_container_width=True)


upfile = st.sidebar.file_uploader('select file')

if upfile is not None:
  df = pd.read_csv(upfile)
  plot_plotly(df)
  
labelhead = st.sidebar.selectbox('select', ('A-2deg', 'A-10deg'))
xl = labelhead + '-L'
yl = labelhead + '-a'
zl = labelhead + '-b'
plot_plotly(df)
