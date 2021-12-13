import pandas as pd
import streamlit as st
import plotly.express as px

st.title('scatter 3D for car coating')

labelhead = 'A-2deg'


def plot_plotly(df):
  labelhead = st.selectbox('select', ('A-2deg', 'A-10deg', 'D50-2deg', 'D50-10deg', 'D65-2deg', 'D65-10deg', 'F2-2deg', 'F2-10deg'))
  xl = labelhead + '-L'
  yl = labelhead + '-a'
  zl = labelhead + '-b'
  
  parts = []
  if st.sidebar.checkbox('hood', value=True):
    parts = parts + ['hood']
  if st.sidebar.checkbo('roof', value=True):
    parts = parts + ['roof']
  if st.sidebar.checkbo('trunk', value=True):
    parts = parts + ['trunk']

  if st.sidebar.checkbox('左前F', value=True):
    parts = parts + ['左前F']    
  if st.sidebar.checkbox('左前D', value=True):
    parts = parts + ['左前D']

  if st.sidebar.checkbox('左後D', value=True):
    parts = parts + ['左後D']
  if st.sidebar.checkbox('左後F', value=True):
    parts = parts + ['左後F'] 

  if st.sidebar.checkbox('右前F', value=True):
    parts = parts + ['右前F']    
  if st.sidebar.checkbox('右前D', value=True):
    parts = parts + ['右前D']

  if st.sidebar.checkbox('右後D', value=True):
    parts = parts + ['右後D']
  if st.sidebar.checkbox('右後F', value=True):
    parts = parts + ['右後F'] 
  
  ret = df[df['part'].isin(parts)]
    
  fig = px.scatter_3d(ret, x=xl, y=yl, z=zl, color='part')
  st.plotly_chart(fig, use_container_width=True)

upfile = st.sidebar.file_uploader('select file')

if upfile is not None:
  df = pd.read_csv(upfile)
  plot_plotly(df)
  

