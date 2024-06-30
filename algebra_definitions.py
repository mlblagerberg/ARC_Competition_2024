"""Project: Define Initial Algebras
Start: June 28th 2024
Last touched: June 28th, 2024
Author: Madeleine L.
"""

import json
import os
import numpy
import abstract_algebra as aa


with open(os.path.expanduser("~/GitHub/arc_2024/data/ARC-AGI/data/training/0a938d79.json"), 'r') as data:
    data = json.load(data)

print(data)

