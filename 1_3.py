# https://www.youtube.com/watch?v=Iu-HLy9hICg, 21:25
import os
from collections import Counter
extensions = Counter([file.split('.')[-1] for file in os.listdir("Data")])
print(extensions)
