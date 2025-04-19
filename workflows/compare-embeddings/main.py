from openai import OpenAI
import numpy as np
from typing import List


class Embedding:
    def __init__(self, model: str = "text-embedding-3-small"):
        self.client = OpenAI()
        self.model = model

    @classmethod
    def get_text_embedding(cls, input_text: str) -> List[float]:
        client = OpenAI()
        response = client.embeddings.create(input=input_text, model=cls().model)
        return response.data[0].embedding

    @staticmethod
    def subtract_embeddings(
        embedding1: List[float], embedding2: List[float]
    ) -> np.ndarray:
        return Embedding.normalize_embedding(
            np.array(embedding1) - np.array(embedding2)
        )

    @staticmethod
    def normalize_embedding(embedding: List[float]) -> np.ndarray:
        return embedding / np.linalg.norm(embedding)

    @staticmethod
    def add_embeddings(embedding1: List[float], embedding2: List[float]) -> np.ndarray:
        return Embedding.normalize_embedding(
            np.array(embedding1) + np.array(embedding2)
        )

    @staticmethod
    def cosine_similarity(embedding1: List[float], embedding2: List[float]) -> float:
        return np.dot(embedding1, embedding2) / (
            np.linalg.norm(embedding1) * np.linalg.norm(embedding2)
        )


# Example usage:
# embedding_instance = Embedding()
# king = embedding_instance.get_text_embedding("King")
# queen = embedding_instance.get_text_embedding("Queen")
# man = embedding_instance.get_text_embedding("Man")
# woman = embedding_instance.get_text_embedding("Woman")

# print(Embedding.subtract_embeddings(king, man))


king = Embedding.get_text_embedding("King")
man = Embedding.get_text_embedding("Man")
woman = Embedding.get_text_embedding("Woman")
queen = Embedding.get_text_embedding("Queen")

print(f"King - Man: {Embedding.cosine_similarity(king, man)}")
print(f"King - Woman: {Embedding.cosine_similarity(king, woman)}")
print(f"King - Queen: {Embedding.cosine_similarity(king, queen)}")
print(
    f"(King - man + woman) - Queen: {Embedding.cosine_similarity(Embedding.add_embeddings(Embedding.subtract_embeddings(king, man), woman), queen)}"
)


def get_text_embedding(input_text: str, model: str = "text-embedding-3-small"):
    client = OpenAI()
    response = client.embeddings.create(input=input_text, model=model)
    return response.data[0].embedding


# Export the function
__all__ = ["get_text_embedding"]
