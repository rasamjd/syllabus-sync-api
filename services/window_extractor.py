import re

# This method extracts the windows from text in which a date and most likely a deadline is mentioned
# The purpose of this approach is to reduce the waste of tokens over useless data in text

PATTERNS = [
  r"\bMon(day)?\b", r"\bTue(sday)?\b", r"\bWed(nesday)?\b",
  r"\bThu(rsday)?\b", r"\bFri(day)?\b",
  r"\bJan(uary)?\b", r"\bFeb(ruary)?\b", r"\bMar(ch)?\b",
  r"\bApr(il)?\b", r"\bMay\b", r"\bJun(e)?\b",
  r"\bJul(y)?\b", r"\bAug(ust)?\b", r"\bSep(tember)?\b",
  r"\bOct(ober)?\b", r"\bNov(ember)?\b", r"\bDec(ember)?\b",
]

def extract_windows(text, window=150):
  
  windows = []
  for pattern in PATTERNS:
    for m in re.finditer(pattern, text, re.IGNORECASE):
      start = max(0, m.start() - window)
      end = min(len(text), m.end() + (window - 100))
      windows.append(text[start:end])
  return windows