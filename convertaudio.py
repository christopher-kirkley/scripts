#!/usr/bin/env python3

import os
import re
from pathlib import Path
import sys

print(len(sys.argv))
print(str(sys.argv))

in_type = sys.argv[1]
out_type = sys.argv[2]

path = os.path.abspath(os.getcwd())

for filename in os.listdir(path):
    if re.search('wav$|aac$|ogg$|mp3$|mpeg$', filename):
        root = (Path(filename).stem)
        os.system(f'ffmpeg -i "{filename}" "{root}"."{out_type}"')
    else:
        pass
# for filename in os.listdir(path):
#     if re.search('{in_type}$|aac$|ogg$|mp3$|mpeg$', filename):
#         root = (Path(filename).stem)
#         os.system(f'ffmpeg -i "{filename}" "{root}".wav')
#     else:
#         pass
