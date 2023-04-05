import openai
import streamlit as st
import yaml

# OpenAI API 인증 정보를 yaml 파일에서 읽어옴
with open("openai.yaml", "r") as f:
    config = yaml.safe_load(f)

# OpenAI API 인증 정보를 설정
openai.api_key = config["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"]

# GPT-3 모델을 사용하여 텍스트 생성
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text
    return message

# 스트림릿 앱 구현
st.title("OpenAI GPT-3 텍스트 생성기")

user_input = st.text_input("문장을 입력하세요.", value="", key="input_text")
if user_input:
    output_text = generate_text(user_input)
    st.write(output_text)
