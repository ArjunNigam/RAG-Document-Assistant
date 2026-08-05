from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from backend.llm.base import BaseLLMProvider
from config.config import Config

load_dotenv()


class GroqProvider(BaseLLMProvider):

    def __init__(self):
        self.model = ChatGroq(
            api_key=Config.GROQ_API_KEY,
            model=Config.MODEL_NAME,
            temperature=Config.TEMPERATURE
        )

        self.prompt = ChatPromptTemplate.from_template("""
You are a helpful PDF assistant. Answer the question using ONLY the context below.

If the context doesn't contain the answer, say "I couldn't find that in the document."

After your answer, list the page numbers you used as:
Sources: page X, page Y.

Context:
{context}

Question:
{question}
""")

    def invoke(self, context: str, question: str) -> str:
        chain = self.prompt | self.model

        return chain.invoke(
            {
                "context": context,
                "question": question
            }
        ).content