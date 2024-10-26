from collections import Counter, defaultdict, namedtuple

counts = Counter("abracadabra")
print(counts)

dd = defaultdict(list)
dd["key"].append(1)
dd["key"].append(2)
dd["foo"] = 3
print(dd)
print(dd["key"])
print(dd["foo"])

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p)
print(p.x)
print(p.y)

import logging

logging.basicConfig(level=logging.INFO)
logging.info("Informational message")
logging.error("An error occurred")
