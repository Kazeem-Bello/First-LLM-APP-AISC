import groq
import os
from fastapi import FastAPI, requests
from dotenv import load_dotenv

load_dotenv()

# set API_Key
GROQ_API_KEY =  os.environ.get("GROQ_API_KEY")

print(type(GROQ_API_KEY))