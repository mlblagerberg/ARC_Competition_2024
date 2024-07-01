"""Project: Define Initial Algebras
Start: June 28th 2024
Last touched: July 1st, 2024
Author: Madeleine L.
"""

import json
import os
import numpy
import numpy as np

import abstract_algebra as aa


with open(os.path.expanduser("~/GitHub/arc_2024/data/ARC-AGI/data/training/0a938d79.json"), 'r') as data:
    data = json.load(data)

# print(data["train"][0])


def addition(input_matrix, value):
    return input_matrix + value


def multiplication(input_matrix, value):
    return input_matrix * value


def transpose(input_matrix):
    return np.transpose(input_matrix)


def rotate_90(input_matrix):
    return np.rot90(input_matrix)


def reflect_vertical(input_matrix):
    return np.flipud(input_matrix)


def reflect_horizontal(input_matrix):
    return np.fliplr(input_matrix)


def color_inverse(input_matrix):
    return 9 - input_matrix


def scale_tile(input_matrix, scale_factor):
    input_matrix = np.array(input_matrix)
    output_matrix = np.tile(input_matrix, (scale_factor, scale_factor))
    return output_matrix


def reshape_matrix(input_matrix, new_shape):
    input_matrix = np.array(input_matrix)
    output_matrix = np.reshape(input_matrix, new_shape)
    return output_matrix


symmetry_operations = [rotate_90, reflect_vertical, reflect_horizontal]

in_matrix = data["train"][0]["input"]
in_matrix = np.array(in_matrix)
print(f"Shape of input matrix: {np.shape(in_matrix)}")

out_matrix = data["train"][0]["output"]
out_matrix = np.array(out_matrix)

transformed_matrix = in_matrix
for operation in symmetry_operations:
    transformed_matrix = operation(transformed_matrix)

print(f"Input matrix: \n{in_matrix}")
print(f"Output matrix: \n{out_matrix}")
print(f"Transformed matrix: \n{transformed_matrix}")

