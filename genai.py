from openai import OpenAI
import openai
import streamlit as st
import json

f= open(r"C:\\Users\\Shashikanth\\OneDrive\\Documents\\Mentoring\\Data Science\\Internship\\weekly Projects\\key\\.API_key.txt")
key = f.read()
client = OpenAI(api_key = key)

st.snow()

##################################
st.title("🎑Python Code Debugger")
st.subheader("🪄Review your code here.")
##################################

prompt = st.text_area("🏁Enter your python code🏁")

if st.button("⚡Generate") == True:
        st.balloons()

        response = client.chat.completions.create(
                model='gpt-3.5-turbo-16k-0613',
                message=[
                    {
                    "role": "system",
                    "content": """You are a helpful AI assistant for Python code debugging.
                                The user will provide a Python code for you to review.
                                Your job is to find any bugs in the code and provide corrected code.
                                Your output should be in the format: {"bug": "description of the error", "fixed_code": "corrected code"}."""
                },
                {"role": "user", "content": f"explain the Bugs and Fixed_code: {prompt}"}
            ],
            temperature=0.5
        )

        corrected_code = (response.choices[0].message.content)
        
        st.write(corrected_code)