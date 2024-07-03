import streamlit as st
import requests

# For the Add Generator #########
from hugchat import hugchat
from hugchat.login import Login
#################################


# Page title
st.write("# Calculate the Market Price of your Apartment in 2024?")

# Text fields:
ap_size = st.text_input(label="Surface in square meters", value = 0, max_chars = 3)

ap_bathrooms = st.text_input(label="Number of bathrooms", value = 1, max_chars = 1)

ap_year_built = st.text_input(label = "Year built", value = 2000)

## Store the predicted price here to use the value in the next button (prompt)
if 'predicted_price' not in st.session_state:
    st.session_state.predicted_price = None

# Button to calculate price
pred_price = st.button(label = "Calculate Price")

# Convert my input data into a request to pass to the api
user_input = {"size":int(ap_size), "year_built":int(ap_year_built), "bathrooms":int(ap_bathrooms)}
api_prediction = requests.post('http://localhost:8000/estimate', json = user_input)

if pred_price:
    st.write("## Market Price: ")
    predicted_price = api_prediction.json()["price"]
    st.session_state.predicted_price = predicted_price
    st.write(f"### {predicted_price} Euros")
    #calculate price
else:
    st.write("Press to calculate the price.")

##############################################################
def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot                        
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)


custom_prompt = f"You are a professional real estate agent. Your task is to create adds for selling apartments.\
    These are the characteristics of the apartment: price in euros: {st.session_state.predicted_price}, the year the building was constructed: {ap_year_built},\
    number of bathrooms: {ap_bathrooms}, the size of the apartment: {ap_size}. Include all information in the add."
# Button to generate Add Text
create_add = st.button(label = "Create Advertising Text")
if create_add:
    with st.spinner("Thinking..."):
        response = generate_response(custom_prompt, st.secrets["user"], st.secrets["password"])
        st.write(response)
else:
    st.write("Press to generate add.")