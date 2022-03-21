import streamlit as st
st.header("hello world") 
st.text("from Brixen")
import streamlit as st
genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")
     
     
APIkey = 319af15e7367c7b87e592b7c6d84197e
location = 'london'

