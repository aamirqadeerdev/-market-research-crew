import os
import time
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

# Set environment variables
os.environ["OPENAI_API_KEY"] = "dummy-key-not-used"
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Use Groq with Llama
llm = "groq/llama-3.3-70b-versatile"