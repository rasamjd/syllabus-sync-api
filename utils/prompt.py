SYLLABUS_PROMPT = '''
You are an information extraction system.

Extract ALL academic deadlines from the syllabus text below.

For each deadline, return an object with:
- course: string (course name or code if available, otherwise "Unknown." e.g., CS 2212, MATH 103)
- title: short descriptive title (e.g., "Homework 2", "Midterm Exam")
- due_date: ISO 8601 datetime string (YYYY-MM-DDTHH:MM:SS)
- type: one of ["exam", "hw", "project", "quiz", "other"]

Rules:
- Return ONLY valid JSON.
- The response must be a JSON array.
- Do NOT include explanations, comments, or markdown.
- If a due time is missing, assume 23:59.
- If a due date is missing or unclear, do NOT include that item.
- Convert all dates and times to ISO format.

Syllabus text:
{SYLLABUS_TEXT}
'''