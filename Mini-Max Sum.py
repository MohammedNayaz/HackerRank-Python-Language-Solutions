#Mini-Max Sum
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
num = [int(x) for x in input().strip().split(' ')]
print(sum(num) - max(num), sum(num) - min(num))