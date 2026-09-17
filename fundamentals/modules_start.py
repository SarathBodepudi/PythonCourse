from tabulate import tabulate
from math import pi

import math
import random as r
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", None, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

print(tabulate(data, headers="firstrow", tablefmt="grid", stralign="center",
                numalign="center", showindex="always", colalign=("center", "center", "center"),
                missingval="N/A", floatfmt=".2f"))

print("\nThe value of pi is approximately: {:.2f}".format(pi))

print(r.randint(100,200))