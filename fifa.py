import streamlit as st
import pandas as pd
import numpy as np

fifa = pd.read_csv('fifa_eda.csv')

st.title("fifa")
st.write(''' j jhsfdjhh sjshfh s jfsdhfhh sjhshfhg, 
             jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjfff''')
                   
                   
st.subheader("top 5 value players")
st.write(fifa.nlargest(5,'Value')[['Name','Value']])

top_players_dict = (fifa.nlargest(5, 'Value')[['Name','Value']]).set_index('Name').to_dict()
for name,value in top_players_dict['Value'].items():
          st.markdown(f"+{name}:{value}")


        
                   

