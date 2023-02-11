from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

model = pipeline("summarization",max_length=50)


from fastapi import Request, Body

@app.post("/summarize")
async def summarize(request:Request,text: str = Body(..., embed=True)):
    summary = model(text)

    return  {"summary":summary[0]["summary_text"]}