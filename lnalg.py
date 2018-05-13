import pandas as pd
import numpy as np

def occurence_matrix(bag, sentences):
    all_words = list(bag)
    occur_matrix = pd.DataFrame(columns=all_words)
    zeros = pd.DataFrame([[0]*len(bag)], columns=all_words)
    for sentence in sentences:
        occur_matrix = occur_matrix.append(zeros, ignore_index=True)
        for word in sentence:
            occur_matrix.loc[len(occur_matrix.index)-1, word] = 1
    return occur_matrix


def cooccurence_matrix(occur_matrix):
    comatrix = occur_matrix.T.dot(occur_matrix)
    np.fill_diagonal(comatrix.values, 0)
    return comatrix


def comatrix(bag, sentences, window=None):
    if not window:
        return cooccurence_matrix(occurence_matrix(bag, sentences))
    
    all_words = list(bag)
    comatrix = pd.DataFrame([[0]*len(bag) for _ in range(len(bag))],
                            columns=all_words,
                            index=all_words)
    
    for s in sentences:
        for w_idx, w in enumerate(s):
            left_edge = w_idx - window
            right_edge = w_idx + window
            if left_edge < 0:
                left_edge = 0
            if right_edge > len(s) - 1:
                right_edge = len(s) - 1
            for left_idx in range(left_edge, w_idx):
                comatrix.loc[w, s[left_idx]] += 1
            for right_idx in range(w_idx + 1, right_edge + 1):
                comatrix.loc[w, s[right_idx]] += 1
                
    return comatrix
            