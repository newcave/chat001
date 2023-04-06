import openai
import streamlit as st
# from streamlit_chat import message
import os 
from dotenv import load_dotenv



# # load_dotenv('api_key.env')
# openai.api_key = os.environ.get('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')

# def generate_response(prompt):
#     completion=openai.Completion.create(
#         engine='text-davinci-003',
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.6,
#     )
#     message=completion.choices[0].text
#     return message


# st.title("ChatGPT-like Web App")
# #storing the chat
# if 'generated' not in st.session_state:
#     st.session_state['generated'] = []
# if 'past' not in st.session_state:
#     st.session_state['past'] = []
# user_input=st.text_input("You:",key='input')
# if user_input:
#     output=generate_response(user_input)
#     #store the output
#     st.session_state['past'].append(user_input)
#     st.session_state['generated'].append(output)
# if st.session_state['generated']:
#     for i in range(len(st.session_state['generated'])-1, -1, -1):
#         message(st.session_state["generated"][i], key=str(i))
#         message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


#################################################################################################

import streamlit as st
import openai
openai.api_key = "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"
# GPT-3 모델 ID
model_engine = "text-davinci-002"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

def main():
    st.title("Chat GPT")
    st.write("간단한 대화를 나누어 보세요.")

    message = st.text_input("사용자: ", "")
    if st.button("전송"):
        st.write("Chat GPT: ", generate_text(message))

if __name__ == "__main__":
    main()
