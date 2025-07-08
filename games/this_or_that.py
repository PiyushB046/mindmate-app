# games/this_or_that.py

import streamlit as st
import random

def play_this_or_that():
    st.subheader("🤔 This or That Game")
    st.markdown("Choose the option that resonates more with your current mood or state of mind.")

    # Define pairs of questions
    question_pairs = [
        ("Sleep all day", "Party all night"),
        ("Talk to a friend", "Write in a journal"),
        ("Watch a movie", "Go for a walk"),
        ("Stay in bed", "Take a shower"),
        ("Listen to music", "Meditate in silence"),
        ("Stay home alone", "Go out with people"),
        ("Read a book", "Watch funny videos"),
        ("Eat comfort food", "Cook something new"),
        ("Cry it out", "Distract yourself"),
        ("Express emotions", "Bottle it up"),
    ]

    if "this_that_index" not in st.session_state:
        st.session_state.this_that_index = 0
        st.session_state.this_that_answers = []
        random.shuffle(question_pairs)
        st.session_state.this_that_questions = question_pairs

    # Get current question
    if st.session_state.this_that_index < len(st.session_state.this_that_questions):
        left, right = st.session_state.this_that_questions[st.session_state.this_that_index]
        st.write(f"**Q{st.session_state.this_that_index + 1}:** Which would you choose right now?")
        col1, col2 = st.columns(2)

        if col1.button(left):
            st.session_state.this_that_answers.append(left)
            st.session_state.this_that_index += 1
            st.rerun()

        if col2.button(right):
            st.session_state.this_that_answers.append(right)
            st.session_state.this_that_index += 1
            st.rerun()
    else:
        st.success("✅ You've completed the game!")
        st.markdown("### Your Choices:")
        for i, choice in enumerate(st.session_state.this_that_answers, start=1):
            st.markdown(f"**Q{i}:** {choice}")

        if st.button("Play Again"):
            st.session_state.this_that_index = 0
            st.session_state.this_that_answers = []
            random.shuffle(question_pairs)
            st.session_state.this_that_questions = question_pairs
            st.rerun()
