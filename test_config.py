

from config import llm

# Send a test message to Groq
response = llm.invoke("Say hello and tell me you are Llama 3.1 8B running on Groq!")

# Print the response
print(response.content)

