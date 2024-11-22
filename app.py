import streamlit as st
import random
import google.generativeai as genai

health_tips = ["Get moving","Eat more whole foods (and less processed food)","if you drink alcohol, do so responsibly","Make preventive care a priority","If you smoke, try to quit","Make sleep a priority","Stay hydrated"]

#css loader
with open('styles.css', "r") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# Setting up the model engine
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-001")

# Initialize session state for messages
if "conversation" not in st.session_state:
    st.session_state.conversation = []  # Single list to maintain the timeline

# Display a header

st.image("logolarge.jpg",use_container_width=False)

# Capturing the user input
user_input = st.chat_input("Enter your message here...")

# Process user input and generate bot response
if user_input:
    # Add user's message to the conversation
    st.session_state.conversation.append({"role": "user", "content": user_input})

    # Generate response from the bot
    response = model.generate_content(user_input)
    if response and response.text:
        # Add bot's response to the conversation
        st.session_state.conversation.append({"role": "ai", "content": response.text})

# Display messages in an alternate fashion (timeline)
for message in st.session_state.conversation:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.sidebar.title("Health Tips")
st.sidebar.subheader(random.choice(health_tips))
