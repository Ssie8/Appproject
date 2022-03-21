import streamlit as st
st.header("hello world") 
st.text("from Brixen")
import streamlit as st
genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")
     
     
 url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + 319af15e7367c7b87e592b7c6d84197e
response = requests.get(url)
weatherData = json.loads(response.text)
print(weatherData['main']['temp_max'])


