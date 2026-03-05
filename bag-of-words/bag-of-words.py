import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    word_to_idx = {word: i for i, word in enumerate(vocab)}
    vector = np.zeros(len(vocab), dtype=int)
    
    for token in tokens:
        if token in word_to_idx:
            idx = word_to_idx[token]
            vector[idx] += 1
            
    return vector