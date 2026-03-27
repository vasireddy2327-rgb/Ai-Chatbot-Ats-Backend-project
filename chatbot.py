from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

print("API KEY:", api_key)  # for debugging

# Initialize LLM
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant"
)

def get_chat_response(user_input):
    try:
        messages = [
            SystemMessage(content="You are a helpful AI assistant."),
            HumanMessage(content=user_input)
        ]

        response = llm.invoke(messages)
        return response.content

    except Exception as e:
        return f"Error: {str(e)}"