import streamlit as st
st.set_page_config(page_title='Flowers')
st.header("Types of Flowers")

col1,col2,col3=st.columns(3)
with col1:
  st.subheader("Rose")
  st.image("./ros2.jpg",caption="Rose",width=300,use_column_width=True)
  st.write("Roses are red")
with col2:
  st.subheader("Jasmine")
  st.image("./jas2.jpg",caption="Jasmine",width=300,use_column_width=True)
  st.write("Jasmines are pleasant")
with col3:
  st.subheader("Tulip")
  st.image("./tulip2.jpg",caption="Tulip",width=300,use_column_width=True)
  st.write("Tulips are beautiful")
