from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

from chatbot import get_chat_response
from ats import calculate_ats_score
from utils import extract_text_from_pdf

app = FastAPI()
app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running "}
# -------- CHAT --------
class ChatRequest(BaseModel):
    query: str

@app.post("/chat")
async def chat(request: ChatRequest):
    return {"response": get_chat_response(request.query)}

# -------- ATS --------
@app.post("/ats", response_class=PlainTextResponse)
async def ats(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    resume_text = extract_text_from_pdf(resume.file)
    result = calculate_ats_score(resume_text, job_description.lower())

    return str(result["analysis"])