import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# ⚠️ Set your API KEY:

# This line forces Python to read your new .env file!
load_dotenv()

# Fetch the API key safely
my_key = os.environ.get("API_KEY")

# Pass that variable into the client
client = OpenAI(api_key=my_key)



def generate_grammar_exercise():
    # Using OpenAI to generate a grammar exercise
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a language teacher. Your job is to teach people English grammar via fun and interesting short exercises by sharing with them some fill-in-the-blanks or multiple-choice questions. Please give one question only."},
            {"role": "user", "content": "Create a fun grammar exercise (fill in the blanks or multiple choice) based on the English language. Please give one question only."}
        ]
    )
    return completion.choices[0].message.content.strip()


def check_answer(question, user_answer):
    # Using OpenAI to check the user's answer and provide feedback
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a language teacher. Your job is to teach people English grammar. You will be given a question and an answer, both by the user. You have to evaluate it and share feedback. Please be supportive and helpful."},
            {"role": "user", "content": f"Question: {question}\nAnswer: {user_answer}\nEvaluate the correctness of the answer and provide feedback:"}
        ]
    )
    return completion.choices[0].message.content.strip()


# --- STREAMLIT UI WRAPPED IN APP() ---
def app():
    st.header('Grammar and Fun 📝')
    st.write('Sharpen your grammar skills with these exercises.')

    # State management for exercise generation
    if 'exercise' not in st.session_state:
        st.session_state.exercise = None

    # Generate exercise button
    if st.button('Start / Get New Question'):
        with st.spinner("Generating a fun question..."):
            st.session_state.exercise = generate_grammar_exercise()

    # Only show the question and input if an exercise exists
    if st.session_state.exercise:
        st.subheader('Exercise:')
        st.write(st.session_state.exercise)

        # User input for response
        user_response = st.text_input('Your answer:', key="user_input")

        if st.button('Check Answer'):
            if user_response:
                with st.spinner("Grading your answer..."):
                    feedback = check_answer(st.session_state.exercise, user_response)
                    st.subheader('Feedback:')
                    st.info(feedback)
            else:
                st.error("Please enter an answer before checking.")