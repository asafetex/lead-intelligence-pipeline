import openai

def classify_lead(message):
    openai.api_key = "your-api-key"
    prompt = f"Classify the lead message: '{message}'\nExtract: name, product, urgency (low/medium/high), and a score from 0 to 100."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    with open("sample_input.txt", "r") as f:
        msg = f.read()
    result = classify_lead(msg)
    print("Classification Result:\n", result)
