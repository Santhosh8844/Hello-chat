import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyAXC0lxfvHXGcqjdGuYaLn0y2HCdhDwWbg")

# Custom CSS for background, font color, input box styles, and text
# Custom CSS for background, font color, input box styles, and text
st.markdown(
    """
    <style>
    body {
        background-color: #000000; /* Black background */
        color: #D9D9D9; /* Lighter shade of gray text */
    }
    .stApp {
        background-color: #000000; /* Black background for the app area */
    }
    .red-text {
        color: red;
    }
    .dark-blue-text {
        color: #003366; /* Dark blue color */
    }
    .stTextInput input {
        background-color: #333333; /* Dark gray background for input box */
        color: #D9D9D9; /* Light gray text color in the input box */
        border: 1px solid #444444; /* Slightly lighter border for the input box */
    }
    .stTextInput input::placeholder {
        color: #FFFFFF; /* White placeholder text color */
        opacity: 1; /* Ensure the placeholder text is not transparent */
    }
    .white-text {
        color: white; /* White text color for output */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# App title and header description
st.markdown('<h1 class="dark-blue-text">💬 Welcome to HELLO Chat</h1>', unsafe_allow_html=True)
st.markdown('<h4 class="dark-blue-text">Powered by Google\'s Gemini AI</h4>', unsafe_allow_html=True)

# Create columns for better layout
col1, col2, col3 = st.columns([1, 2, 1])

# Center the input field
with col2:
    text = st.text_input("Enter your question")

# Check if input is given
if text:
    with st.spinner("Generating response..."):
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat(history=[])
        response = chat.send_message(text)

        # Display the response with white text
        st.markdown(f'<p class="white-text">AI Response: {response.text}</p>', unsafe_allow_html=True)
