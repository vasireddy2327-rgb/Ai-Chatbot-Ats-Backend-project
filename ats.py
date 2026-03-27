from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

print("ATS API KEY:", api_key)  # Debug check

def calculate_ats_score(resume_text, job_desc):
    try:
        llm = ChatGroq(
            groq_api_key=api_key,
            model_name="llama-3.1-8b-instant"
        )

        prompt = f"""
        You are an ATS system.

        Compare resume and job description.

        Resume:
        {resume_text}

        Job Description:
        {job_desc}

        Give:
        1. ATS Score (0-100)
        2. Missing Skills
        3. Suggestions
        """

        response = llm.invoke(prompt)
        return {"analysis": response.content}

    except Exception as e:
        return {"analysis": f"Error: {str(e)}"}