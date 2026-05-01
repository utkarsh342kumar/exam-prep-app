import streamlit as st
from mcq_generator import generate_mcqs
from styles import apply_styles

# Page config
st.set_page_config(page_title="Exam Prep Generator", page_icon="📚")

# Apply styles
st.markdown(apply_styles(), unsafe_allow_html=True)

# Title
st.title("📚 Exam Prep Question Generator")
st.write("Generate MCQs instantly from your text ✨")

# Input
text = st.text_area("Paste your paragraph here:")

difficulty = st.selectbox("Select Difficulty Level", ["Easy", "Medium", "Hard"])

# Button
if st.button("Generate Questions 🚀"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text!")
    else:
        mcqs = generate_mcqs(text, difficulty)

        st.success("✅ Questions Generated!")

        for i, q in enumerate(mcqs):
            st.markdown(f"### Q{i+1}: {q['question']}")

            for opt in q["options"]:
                st.write(f"- {opt}")

            st.markdown(f"**Answer:** {q['answer']}")
            st.markdown("---")
