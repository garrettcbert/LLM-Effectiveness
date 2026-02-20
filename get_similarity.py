import spacy
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class PosSimilarity:
    def __init__(self, text1, text2, text3):
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3

    def get_pos_string(self, nlp, text):
        doc = nlp(text)
        return " ".join([token.pos_ for token in doc])
    
    def get_cosine_similarity(self):
        nlp = spacy.load("en_core_web_sm")
        pos_corpus = [self.get_pos_string(nlp, text) for text in [self.text1, self.text2, self.text3]]

        vectorizer = CountVectorizer(ngram_range=(1, 2))
        matrix = vectorizer.fit_transform(pos_corpus)

        similarity_1_2 = cosine_similarity(matrix[0], matrix[1])[0][0]
        similarity_1_3 = cosine_similarity(matrix[0], matrix[2])[0][0]
        similarity_2_3 = cosine_similarity(matrix[1], matrix[2])[0][0]

        return similarity_1_2, similarity_1_3, similarity_2_3
    
    def get_similarity_matrix(self):
        matrix = np.ones((3, 3))
        matrix[0, 1] = matrix[1, 0] = self.get_cosine_similarity()[0]
        matrix[0, 2] = matrix[2, 0] = self.get_cosine_similarity()[1]
        matrix[1, 2] = matrix[2, 1] = self.get_cosine_similarity()[2]
        return matrix
    
    def __str__(self):
        return f"Similarity between text1 and text2: {self.get_cosine_similarity()[0]}, Similarity between text1 and text3: {self.get_cosine_similarity()[1]}\nSimilarity Matrix: {self.get_similarity_matrix()}"

    