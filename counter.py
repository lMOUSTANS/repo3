words = []
with open("loubna.txt", "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
top6 = counts.most_common(5)
print(top6)
