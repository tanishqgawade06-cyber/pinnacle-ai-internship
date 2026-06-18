from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Autocorrect API")

# 1. Load the model on startup up so it's ready to go
print("Spinning up the AI Engine...")
unmasker = pipeline('fill-mask', model='distilbert-base-uncased')

# 2. Define the expected JSON payload format
class TextPayload(BaseModel):
    sentence: str

# 3. Create the endpoint to receive text and return predictions
@app.post("/predict")
async def get_correction(payload: TextPayload):
    # Pass the incoming sentence to the AI
    predictions = unmasker(payload.sentence)
    
    # Format the AI's output into a clean list
    suggestions = []
    for p in predictions:
        suggestions.append({
            "word": p['token_str'],
            "confidence": round(p['score'] * 100, 2)
        })
        
    return {
        "original_text": payload.sentence,
        "top_suggestions": suggestions
    }