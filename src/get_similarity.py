import spacy
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class PosSimilarity:
    def __init__(self, text1, text2, text3):
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self._similarities = None

    def _get_pos_string(self, nlp, text):
        doc = nlp(text)
        return " ".join([token.pos_ for token in doc])

    def _compute_similarities(self):
        if self._similarities is not None:
            return self._similarities
        nlp = spacy.load("en_core_web_sm")
        pos_corpus = [self._get_pos_string(nlp, text) for text in [self.text1, self.text2, self.text3]]
        vectorizer = CountVectorizer(ngram_range=(1, 2))
        matrix = vectorizer.fit_transform(pos_corpus)
        full = cosine_similarity(matrix)
        self._similarities = (full[0, 1], full[0, 2], full[1, 2])
        return self._similarities

    def get_cosine_similarity(self):
        return self._compute_similarities()

    def get_similarity_matrix(self):
        s12, s13, s23 = self._compute_similarities()
        matrix = np.ones((3, 3))
        matrix[0, 1] = matrix[1, 0] = s12
        matrix[0, 2] = matrix[2, 0] = s13
        matrix[1, 2] = matrix[2, 1] = s23
        return matrix

    def __str__(self):
        s12, s13, _ = self._compute_similarities()
        return f"Similarity between text1 and text2: {s12}, Similarity between text1 and text3: {s13}\nSimilarity Matrix: {self.get_similarity_matrix()}"
