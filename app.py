import streamlit as st
from utils import load_questions, load_this_or_that_questions
from ml_model import predict_label
from chatbot_llama import chatbot_reply, reframe_negative_thought

st.set_page_config(page_title="MindMate", page_icon="🧠")
st.title("🧠 MindMate - Your Mental Health Companion")

# === TOP-LEVEL TABS ===
main_tab, game_tab = st.tabs(["💬 Chatbot", "🎮 Games"])

# =======================
# 💬 CHATBOT TAB
# =======================
with main_tab:
    st.subheader("💬 Talk to MindMate")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", key="chat_input")

    if user_input:
        ai_response = chatbot_reply(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("MindMate", ai_response))

    for sender, message in reversed(st.session_state.chat_history):
        st.markdown(f"**{sender}:** {message}")

# =======================
# 🎮 GAME TAB
# =======================
with game_tab:
    st.subheader("🎮 Choose a Game")

    game_choice = st.selectbox(
        "🕹️ Select a game to play:",
        ("🎯 Trivia Game", "🟰 This or That", "💭 Cognitive Reframe")
    )

    # --- 🎯 Trivia Game ---
    if game_choice == "🎯 Trivia Game":
        st.subheader("🎯 Mental Health Trivia")
        questions = load_questions()

        if "question_index" not in st.session_state:
            st.session_state.question_index = 0
            st.session_state.user_answers = []
            st.session_state.predictions = []

        if questions and st.session_state.question_index < len(questions):
            current_q = questions[st.session_state.question_index]
            st.markdown(f"**Q{st.session_state.question_index + 1}:** {current_q['question']}")
            answer = st.text_input("Your answer:", key=f"trivia_{st.session_state.question_index}")

            if st.button("Next Question"):
                if not answer.strip():
                    st.warning("⚠️ Please enter an answer.")
                else:
                    label = predict_label(answer)
                    st.session_state.user_answers.append(answer)
                    st.session_state.predictions.append(label)
                    st.session_state.question_index += 1
                    st.rerun()

        elif questions:
            st.success("✅ You've completed the trivia!")
            st.markdown("### Your Responses & Insights:")
            for i, (q, a, p) in enumerate(zip(questions, st.session_state.user_answers, st.session_state.predictions)):
                st.markdown(f"**Q{i+1}:** {q['question']}")
                st.markdown(f"🗨️ Your response: *{a}*")
                st.markdown(f"🧠 Predicted label: **{p}**")
                st.write("---")

            if st.button("Restart Quiz"):
                st.session_state.question_index = 0
                st.session_state.user_answers = []
                st.session_state.predictions = []
                st.rerun()

    # --- 🟰 This or That ---
    elif game_choice == "🟰 This or That":
        st.subheader("🟰 This or That Game")
        questions = load_this_or_that_questions()

        if "this_index" not in st.session_state:
            st.session_state.this_index = 0
            st.session_state.this_answers = []
            st.session_state.this_predictions = []

        if questions and st.session_state.this_index < len(questions):
            q = questions[st.session_state.this_index]
            st.markdown(f"**Q{st.session_state.this_index + 1}:** {q['question']}")

            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"🅰️ {q['option_a']}"):
                    label = predict_label(q["option_a"])
                    st.session_state.this_answers.append(q["option_a"])
                    st.session_state.this_predictions.append(label)
                    st.session_state.this_index += 1
                    st.rerun()

            with col2:
                if st.button(f"🅱️ {q['option_b']}"):
                    label = predict_label(q["option_b"])
                    st.session_state.this_answers.append(q["option_b"])
                    st.session_state.this_predictions.append(label)
                    st.session_state.this_index += 1
                    st.rerun()

        elif questions:
            st.success("🎉 You've completed the 'This or That' Game!")
            st.markdown("### Your Choices & Emotion Insights:")
            for i, (q, a, p) in enumerate(zip(questions, st.session_state.this_answers, st.session_state.this_predictions)):
                st.markdown(f"**Q{i+1}:** {q['question']}")
                st.markdown(f"🟰 You chose: *{a}*")
                st.markdown(f"🧠 Predicted emotion: **{p}**")
                st.write("---")

            if st.button("Play Again"):
                st.session_state.this_index = 0
                st.session_state.this_answers = []
                st.session_state.this_predictions = []
                st.rerun()

    # --- 💭 Cognitive Reframe ---
    elif game_choice == "💭 Cognitive Reframe":
        st.subheader("💭 Cognitive Reframe Game")

        if "reframe_history" not in st.session_state:
            st.session_state.reframe_history = []

        user_thought = st.text_area("😔 Enter a negative thought you'd like to reframe:", key="user_reframe_input")

        if st.button("🔁 Reframe with AI"):
            if user_thought.strip():
                reframed = reframe_negative_thought(user_thought)
                st.session_state.reframe_history.append((user_thought, reframed))
                st.rerun()
            else:
                st.warning("⚠️ Please enter a thought before clicking reframe.")

        if st.session_state.reframe_history:
            st.markdown("### 🌟 Reframed Thoughts:")
            for i, (neg, pos) in enumerate(st.session_state.reframe_history):
                st.markdown(f"**#{i+1}**")
                st.markdown(f"🧠 You said: _{neg}_")
                st.markdown(f"💡 Reframed: **{pos}**")
                st.write("---")

            if st.button("🔄 Reset Reframe History"):
                st.session_state.reframe_history = []
                st.rerun()
