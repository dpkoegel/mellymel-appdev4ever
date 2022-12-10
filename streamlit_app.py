import streamlit
import pandas

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Favorites')

streamlit.text('\U0001F44D Omega 3 & Bueberry Oatmeal')
streamlit.text('🦻 Kale, Spinach & Rocket Smoothy')
streamlit.text('🧠 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)

