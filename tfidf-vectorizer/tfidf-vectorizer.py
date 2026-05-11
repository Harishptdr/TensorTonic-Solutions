import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    def tokenize(text):
        return text.lower().split()

    tokenized = [tokenize(doc) for doc in documents]
    N = len(documents)

    all_terms = sorted({term for doc in tokenized for term in doc})
    vocabulary = {term: idx for idx, term in enumerate(all_terms)}
    V = len(vocabulary)

    df = Counter(term for doc in tokenized for term in set(doc))
    idf = {term: math.log(N / df[term]) for term in all_terms}

    tfidf_matrix = np.zeros((N, V))

    for i, tokens in enumerate(tokenized):
        total = len(tokens)
        counts = Counter(tokens)
        for term, count in counts.items():
            if term in vocabulary:
                tf = count / total
                tfidf_matrix[i][vocabulary[term]] = tf * idf[term]

    return tfidf_matrix, vocabulary