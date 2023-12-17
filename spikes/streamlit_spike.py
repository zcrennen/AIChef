import streamlit as st

##################
# Run this file in the terminal with the following line
# streamlit run .\streamlit_spike.py
##################

# Define the Streamlit app
def main():
    # Set the title and a greeting message
    st.title('Greeting App')
    st.header('Hello, world!')

    # Create a text input field
    user_name = st.text_input('Enter your name:')
    
    # Display a personalized greeting
    if user_name:
        st.write(f'Hello, {user_name}!')

# Run the Streamlit app
if __name__ == '__main__':
    main()
