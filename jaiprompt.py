import streamlit as st
from groq import Groq

# Enter your Groq API Key
client = Groq(api_key="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")

st.set_page_config(page_title="AI Code Explainer", page_icon="🤖")

st.title("🤖 AI Code Explainer")
st.write("Paste your source code below to get an explanation.")

language = st.selectbox(
    "Programming Language",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "HTML",
        "CSS",
        "PHP",
        "SQL",
        "Other"
    ]
)

code = st.text_area("Paste Code Here", height=300)

if st.button("Explain Code"):

    if code.strip() == "":
        st.warning("Please enter some code.")

    else:

        prompt = f"""
You are an expert programming tutor.

Programming Language: {language}

Code:
{code}

Provide:

1. Simple Explanation
2. Line-by-line Explanation
3. Time Complexity
4. Space Complexity
5. Possible Improvements
6. Optimized Version (if applicable)

Keep the explanation beginner-friendly.
"""

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.subheader("📖 Explanation")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Check your Groq API key and internet connection.")