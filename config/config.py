import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile"
    )

    TEMPERATURE = float(
        os.getenv("TEMPERATURE", "0")
    )