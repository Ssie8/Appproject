import streamlit as st
st.header("hello world") 
st.text("from Brixen")
import streamlit as st
genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")
     
     
     
     APIkey = https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key} 
location = 'london'

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey
response = requests.get(url)
weatherData = json.loads(response.text)
print(weatherData['main']['temp_max'])
