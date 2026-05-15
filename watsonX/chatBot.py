import gradio as gr
from dotenv import load_dotenv
import os 
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

apiKey = os.getenv("WATSONX_API_KEY")
project_id = os.getenv("WATSONX_PROJECT_ID")
watsonx_ai_url = os.getenv("WATSONX_URL")

credentials = Credentials(
        url = f"{watsonx_ai_url}",
        api_key = f"{apiKey}",
    )
client = APIClient(credentials)

model = ModelInference(
    model_id="ibm/granite-4-h-small",
    api_client=client,
    project_id=f"{project_id}",
    params = {
        "max_tokens": 2000
    }
)

# watsonx api 요청
def chatBot(message, history):

    messages = [
        {"role": "user", "content": message},
    ]

    generated_response = model.chat(messages=messages)

    print(generated_response)
    # print(generated_response['choices'][0]['message']['content'])
    return generated_response['choices'][0]['message']['content']

# gradio 설정
demo = gr.ChatInterface(
    fn=chatBot, 
    examples=["된장찌개 레시피 알려줘.", "치킨 레시피 알려줘.", "피자 레시피 알려줘."], 
    title="Watsonx Granite Chatbot"
)

demo.launch()