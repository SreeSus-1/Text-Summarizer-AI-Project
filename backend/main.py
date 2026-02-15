from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class SummarizeRequest(BaseModel):
    text: str

@app.post("/summarize/")
def summarize(req: SummarizeRequest):
    ollama_payload = {
        "model": "llama2",
        "prompt": f"Summarize the following text in 2-3 sentences:\n\n{req.text}",
        "stream": False
    }

    r = requests.post("http://localhost:11434/api/generate", json=ollama_payload)

    # If Ollama is down or returns non-200, show it clearly
    if r.status_code != 200:
        return {"error": f"Ollama error {r.status_code}", "details": r.text}

    data = r.json()

    # Ollama returns either {"response": "..."} or {"error": "..."}
    if "error" in data:
        return {"error": "Ollama returned an error", "details": data["error"]}

    summary = (data.get("response") or "").strip()
    if not summary:
        return {"error": "Empty summary returned from Ollama", "details": data}

    return {"summary": summary}
