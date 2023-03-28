# CREATE.PY

# ~~~~~~~~~~
# Create a New Zettelkasten
# ~~~~~~~~~~

# Python Imports
# Read time to create Unique ID
# Input Thought
# Input Title
# Create file_name from Uniq ID
# Write File
# Print confirmation

# ~~~~~~~~~
# Code
# ~~~~~~~~~

# Python Imports
from datetime import datetime
import os

# Read time to create Unique ID
x = datetime.now()
UniqID = x.strftime('%Y%m%d%H%M%S')
print(UniqID)

# Input Thought
Thought = input("Thought: ")

# Input Title
Title = input("Title: ")

# Create file_name from Uniq ID
file_name = UniqID + '.md'

# Write file
path = r'/home/blackbeard/zettelkasten/zettels'
f = open(os.path.join(path, file_name), "a")
file_contents = ('\n'.join([UniqID, '\n', Title, Thought, '\n', file_name]))
f.write(file_contents)
f.close()

# Print confirmation
print('\n' + 'Success!')

