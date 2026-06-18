from transformers import pipeline

# 1. Download and load the AI model
print("Loading AI Model (this takes a moment the first time)...")
unmasker = pipeline('fill-mask', model='distilbert-base-uncased')

# 2. Give the AI a sentence with the confusing word replaced by [MASK]
sentence = "I bought a new [MASK] of shoes."
print(f"Analyzing sentence: '{sentence}'\n")

# 3. Ask the AI to predict the most logical words
predictions = unmasker(sentence)

print("The AI mathematically predicts the word should be:")
for p in predictions:
    # We print the top guesses and their confidence scores
    print(f"- {p['token_str']} (Confidence: {round(p['score'] * 100, 2)}%)")