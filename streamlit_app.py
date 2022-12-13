import streamlit
import pandas
import requests

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Favorites')

streamlit.text('\U0001F44D Omega 3 & Bueberry Oatmel')
streamlit.text('🦻 Kale, Spinach & Rocket Smoothy')
streamlit.text('🧠 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)),['Avocado','Strawberries'])
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#,['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

