import streamlit as st
import openai as ai

st.set_page_config(page_title = "Financial Literacy Chatbot", layout = "wide")

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

try:
  ai.api_key = st.secrets["secret_openai_key"]
except:
  st.text('Add API Key')

def chatgpt_call(prompt, model, temperature):
  completion = ai.ChatCompletion.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    temperature=temperature
  )
  return completion['choices'][0]['message']['content']

st.header('WealthWhiz :money_with_wings: :money_with_wings:')
st.subheader("Learn about all aspects of finance!")
st.write(
  """
  Financial literacy has become imperative to successfully navigate through life. As high schoolers, we feel as though we are not exposed to financial literacy, leaving us with limited knowledge about managing money effectively. We have designed an AI financial assistant to help high schoolers, like us, as well as other individuals; this chatbot is completely accessible, and it is not biased toward one ethnic or cultural group. It takes into account various financial situations.
""")
  
  
topic = st.text_input('What would you like to know about financial literacy?')
model = 'gpt-3.5-turbo'
temperature = 0.5
st.sidebar.markdown("This app uses OpenAI's generative AI. Please use it carefully and check any output.")

prompt = f"You are an expert teacher in financial literacy. If the topic entered does not have to do with financial literacy or finance in general, please reply with: Sorry, this topic does not have to do with financial literacy or finance. For example, if the user asked about world war 2, please answer with: Sorry, this topic does not have to do with financial literacy or finance. Make sure that the user only asks about finance related questions, and reprompt the user if they ask about something else. Please ask me a more relevant question. Explain the topic as if you were talking to a high schooler who is eager to learn more about financial literacy: {topic}"

explanation = chatgpt_call(prompt, model, temperature)

generate = st.button('Generate Response')

if generate:
  st.markdown(explanation)
  st.balloons()
