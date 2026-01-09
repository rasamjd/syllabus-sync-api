from fastapi import FastAPI, UploadFile, File
from services.llm import extract_deadlines
from fastapi.middleware.cors import CORSMiddleware
from services.pdf_parser import pdf_bytes_to_text 
from services.window_extractor import extract_windows

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:8081"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.post("/parse_syllabus")
async def parse_syllabus(file: UploadFile = File(...)):

  content = await file.read()
  text = pdf_bytes_to_text(content)
   
  windows = extract_windows(text)
  windows.insert(0, text[:2000]) # Primary information -- e.g. course name
  
  data = " - ".join(windows)
  
  deadlines = await extract_deadlines(data)  
  return { "deadlines": deadlines }

@app.get("/")
def welcome():
  return { "message": "Hi! This is a test message." } 