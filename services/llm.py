import os
from groq import Groq
from utils.prompt import SYLLABUS_PROMPT 

client = Groq(
  api_key=os.environ.get("QROQ_API_KEY") # should change to GROQ (but since QROQ is saved on my device, this works)
)

async def extract_deadlines(syllabys_text: str):
  
  chat_completion = client.chat.completions.create(
    messages=[
      {
        "role": "user",
        "content": SYLLABUS_PROMPT.format(SYLLABUS_TEXT=syllabys_text[:10000]),
      }
    ],
    model="llama-3.3-70b-versatile",
  )
  
  deadlines = chat_completion.choices[0].message.content

  return deadlines