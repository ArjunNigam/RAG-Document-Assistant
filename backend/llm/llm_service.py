from backend.llm.groq_provider import GroqProvider
from config.config import Config


class LLMService:

    def __init__(self):
        match Config.LLM_PROVIDER:
            case "groq":
                self.provider = GroqProvider()

            case _:
                raise ValueError(
                    f"Unsupported LLM provider: {Config.LLM_PROVIDER}"
                )

    def invoke(self, context: str, question: str) -> str:
        return self.provider.invoke(
            context=context,
            question=question
        )