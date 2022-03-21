import streamlit as st
st.header("hello world") 
st.text("from Brixen")
import streamlit as st
genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")
     
st.write('weather',
import json, requests  
        
APIkey = 319af15e7367c7b87e592b7c6d84197e
import streamlit as st
location = st.radio("what's the weather in"),('London', 'Madrid', 'Sydney'))
st.write('the weather for today')
st.write('the temperature of' location)
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + &units=metric
response = request.get(url)
weatherData = json.loads(response.text)
st.write('max temperature', weatherData [] )

print(weatherData['main']['temp_max'])
