# Test
import openai
import os


# Set up your API key
openai.api_key = "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"

abs_path = os.path.abspath('scrape.txt')
# Load the contents of the document
with open(abs_path, "r", encoding="utf-8") as f:
    doc_contents = f.read()

# Create the prompt in Hebrew
prompt = (
    "האם בטקסט הבא יש החלטה או אינפורמציה שעלולה לפגוע בקהילה הגאה?:"
    f"\n{doc_contents}"
)

# Make a request
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=5,
    n=1,
    stop=None,
    temperature=0.5
)

print(response.choices[0].text)

