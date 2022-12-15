import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favorites')

streamlit.text('\U0001F44D Omega 3 & Bueberry Oatmel')
streamlit.text('🦻 Kale, Spinach & Rocket Smoothy')
streamlit.text('🧠 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)),['Avocado','Strawberries'])
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#,['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('FruityVice Fruit Advise')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon" + fruit_choice)
#streamlit.text(fruityvice_response.json())

# write your own comment 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("Select * from fruit_load_list")
my_data_row2 = my_cur.fetchall()
streamlit.header("The Fruit List Contains")
streamlit.dataframe(my_data_row2)
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
my_cur.add(fruit_load_list_2,add_my_fruit  )
streamlit.write('Thanks For Adding ', add_my_fruit)

#insert into fruit_load_list_2 (FRUIT_NAME) select  'jackfruit';
