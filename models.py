from pydantic import BaseModel

class Deadline(BaseModel):
  course: str
  title: str
  due_date: str # ISO format
  type: str