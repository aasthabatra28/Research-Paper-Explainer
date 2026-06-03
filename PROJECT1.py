from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
load_dotenv()
st.set_page_config(
    page_title="Research Paper Explainer",
    page_icon="📚",
)
st.title("📚 Research Paper Explainer")
st.write("Generate easy-to-understand summaries of famous AI research papers.")
paper_input = st.selectbox(
    "Select Research Paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)
style_input = st.selectbox(
    "Explanation Style",
    ["Beginner-Friendly", "Technical", "Professional", "Casual"],
)
length_input = st.selectbox(
    "Content Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (Detailed)",
    ],
)
if st.button("Generate Summary"):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or api_key == "ADD_YOUR_API_KEY_HERE":
        st.error("Please add your Google API key in the .env file.")
        st.stop()
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.3,
    )
    prompt_template = PromptTemplate(
        input_variables=["paper", "style", "length"],
        template="""
You are an AI research expert.
Explain the research paper: "{paper}"
Explanation Style: {style}
Explanation Length: {length}
Include:
1. Main Idea
2. Key Contributions
3. How It Works
4. Real-World Applications
5. Why It Matters
Keep the explanation clear and engaging.
""",
    )
    prompt = prompt_template.format(
        paper=paper_input,
        style=style_input,
        length=length_input,
    )
    response = model.invoke(prompt)
    st.subheader("Generated Summary")
    st.write(response.content)