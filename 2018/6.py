#!/usr/bin/env python3

import numpy as np

# name = input("Specify name (which in-file to be used):")
# file_name = "6_%s.in" % name if name else "6.in"
with open("6.in", "r") as f:
    coordinates = f.read().splitlines()


