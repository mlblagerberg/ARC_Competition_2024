"""Project: Define Initial Algebras
Start: July 1st, 2024
Last touched: July 1st, 2024
Author: Madeleine L.
"""

import os
import json
import numpy as np


def square(matrix):
    return matrix.shape[0] == matrix.shape[1]


def load_puzzle(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    return data


def matrix_features(matrix):
    matrix = np.array(matrix)
    features = []
    features.append(np.sum(matrix))
    features.append(np.mean(matrix))
    features.append(np.std(matrix))
    features.append(np.sum(matrix, axis=0))  # Column sums
    features.append(np.sum(matrix, axis=1))  # Row sums
    features.append(np.diag(matrix))
    features.append(np.diag(np.fliplr(matrix)))
    if square(matrix):
        features.append(np.linalg.det(matrix))
    else:
        features.append('None')

    return features


json_dir = os.path.expanduser("~/GitHub/arc_2024/data/ARC-AGI/data/training/")

for file in os.listdir(json_dir):
    if file.endswith(".json"):
        puzzle = load_puzzle(os.path.join(json_dir, file))