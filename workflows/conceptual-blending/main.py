from ell import ell
from typing import List, Tuple
from openai import OpenAI
import random
import numpy as np


def get_text_embedding(input_text: str, model: str = "text-embedding-3-small"):
    client = OpenAI()
    response = client.embeddings.create(input=input_text, model=model)
    return response.data[0].embedding


class ConceptualBlender:
    def __init__(self, model: str = "gpt-4o-mini"):
        self.client = OpenAI()
        self.model = model
        ell.init(store="./logdir")

    @ell.complex(model="gpt-4o-mini")
    def blend_concepts(
        self,
        concept1: str,
        concept2: str,
        creativity_level: int = 5,
        detail_level: int = 3,
    ):
        system = f"""You are a conceptual blending assistant. Blend the following two concepts into a creative or novel insight.
        Creativity level: {creativity_level}/10 (1 being conservative, 10 being highly imaginative)
        Detail level: {detail_level}/5 (1 being brief, 5 being very detailed)

        Follow these steps:
        1. Identify key characteristics of each concept
        2. Find common elements or potential connections
        3. Create a novel combination that preserves important aspects of both concepts
        4. Explain how the blended concept relates to the original concepts
        5. Suggest potential applications or implications of the new concept"""
        prompt = f"Concept 1: {concept1}\nConcept 2: {concept2}\n\nPlease provide a blended concept explanation according to the specified creativity and detail levels."
        return [ell.system(system), ell.user(prompt)]

    def calculate_blend_score(self, blend: str, concept1: str, concept2: str) -> float:
        blend_embedding = get_text_embedding(blend)
        concept1_embedding = get_text_embedding(concept1)
        concept2_embedding = get_text_embedding(concept2)

        # Calculate cosine similarity
        def cosine_similarity(a, b):
            return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

        similarity_to_concept1 = cosine_similarity(blend_embedding, concept1_embedding)
        similarity_to_concept2 = cosine_similarity(blend_embedding, concept2_embedding)

        # We want the blend to be similar to both concepts, but not too similar to either
        balance_score = 1 - abs(similarity_to_concept1 - similarity_to_concept2)
        novelty_score = 1 - max(similarity_to_concept1, similarity_to_concept2)

        return (balance_score + novelty_score) / 2

    def generate_multiple_blends(
        self, concept1: str, concept2: str, num_blends: int = 3
    ) -> List[Tuple[str, float]]:
        blends = []
        for _ in range(num_blends):
            creativity = random.randint(1, 10)
            detail = random.randint(1, 5)
            blend = self.blend_concepts(concept1, concept2, creativity, detail)

            score = self.calculate_blend_score(blend.text, concept1, concept2)
            blends.append((blend.text, score))

        return sorted(blends, key=lambda x: x[1], reverse=True)


# Example usage:
blender = ConceptualBlender()
concept1 = "Artificial Intelligence"
concept2 = "Art"
blended_concepts = blender.generate_multiple_blends(concept1, concept2)
best_blend, score = blended_concepts[0]
print(f"Best blend (score: {score}):\n{best_blend}")
