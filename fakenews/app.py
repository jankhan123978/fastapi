from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import pickle
import re

app = FastAPI()

# Allow all origins for development; restrict in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

with open("model/model.pkl", 'rb') as f:
    model = pickle.load(f)

with open("model/vectorizer.pkl", 'rb') as f:
    vectorizer = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

def lower(text):
    return text.lower()

def clean_text(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def transform(text):
    return vectorizer.transform([lower(clean_text(text))])

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    text = data.get('text', '')
    prediction = model.predict(transform(text))
    result = "Fake News" if prediction[0] == 0 else "Real News"
    return JSONResponse(content={"prediction": result})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
