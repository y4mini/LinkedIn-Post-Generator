from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os


load_dotenv()

llm=ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model_name="llama-3.2-90b-vision-preview")

if __name__=="__main__":
    response=llm.invoke("What are the 2 main ingredients of pizza")
    print(response.content)
