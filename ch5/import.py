from collections import Counter
import random

random.seed()
a = list()
for i in range(10):
    a.append(random.randrange(10) + 1)

print(a)
print(Counter(a).most_common())
