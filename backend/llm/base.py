from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):

    @abstractmethod
    def invoke(self, context: str, question: str) -> str:
        pass