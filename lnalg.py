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
