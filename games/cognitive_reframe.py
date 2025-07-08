# games/cognitive_reframe.py

import streamlit as st

def play_cognitive_reframe():
    st.subheader("🧠 Cognitive Reframe Game")
    st.markdown("Let's challenge negative thoughts and practice positive thinking.")

    reframe_prompts = [
        {
            "negative": "I'm not good enough.",
            "options": ["I'm learning and improving every day.", "Others are better than me."],
            "correct": "I'm learning and improving every day."
        },
        {
            "negative": "I always mess things up.",
            "options": ["Mistakes help me grow.", "I can't do anything right."],
            "correct": "Mistakes help me grow."
        },
        {
            "negative": "No one understands me.",
            "options": ["I can find support from someone who listens.", "I should just stay quiet."],
            "correct": "I can find support from someone who listens."
        },
        {
            "negative": "Things will never get better.",
            "options": ["Change takes time, and things can improve.", "I give up."],
            "correct": "Change takes time, and things can improve."
        },
    ]

    if "reframe_index" not in st.session_state:
        st.session_state.reframe_index = 0
        st.session_state.reframe_score = 0

    if st.session_state.reframe_index < len(reframe_prompts):
        prompt = reframe_prompts[st.session_state.reframe_index]
        st.markdown(f"💭 **Negative Thought:** *{prompt['negative']}*")

        choice = st.radio("🧠 Choose a way to reframe:", prompt["options"], key=st.session_state.reframe_index)

        if st.button("Submit Reframe"):
            if choice == prompt["correct"]:
                st.success("✅ Great! That's a healthy way to reframe.")
                st.session_state.reframe_score += 1
            else:
                st.error("❌ Try again. That thought might not be helpful.")
            st.session_state.reframe_index += 1
            st.rerun()
    else:
        st.success("🎉 You've completed the Reframe Game!")
        st.markdown(f"**Score:** {st.session_state.reframe_score} out of {len(reframe_prompts)}")
        if st.button("Play Again"):
            st.session_state.reframe_index = 0
            st.session_state.reframe_score = 0
            st.rerun()
