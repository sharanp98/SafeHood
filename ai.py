import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Create a chat completion request
completion = client.chat.completions.create(
    model="gpt-4o-mini",  # Ensure this is the correct model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

# Print the message from the completion
print(completion.choices[0].message.content)  # Use dot notation to access content
